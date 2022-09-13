"""Handles the LARGE data from this program.
Also runs blackjack. (Future endeavors:
multiplayer. Actual cards in the deck)"""
from random import randint
import asyncio, discord
class Blackjack:
  def __init__(self):
    self.users = {}
    self.msg = {}
    self.cards = {}
    self.values = {}
    self.reactions = ['✅','❎']
  async def start(self, ctx, bot):
    if ctx.author in self.users:
      await ctx.send("You're already playing a game! Stupid. I killed your other session because you can't pay attention")
      await self.finish(ctx.author)
    else:
      self.users[ctx.author] = ["question", 0, 0, 0, "no"] #question can be used later
      self.msg[ctx.author] = await ctx.send("loading...")
      await self.deck_setup(ctx)
      await self.game(ctx, bot)
  async def game(self, ctx, bot):
    """The game is played here"""
    def check(reaction, user):
      """helper function that checks if a message was reacted to"""
      if user == ctx.author:
        if str(reaction.emoji) == self.reactions[0]:
          return user == ctx.author and str(reaction.emoji) == self.reactions[0]
        if str(reaction.emoji) == self.reactions[1]:
          return user == ctx.author and str(reaction.emoji) == self.reactions[1]
    m = self.msg.get(ctx.author)
    for i in range(2):
      await self.hit(ctx)
    await m.edit(content=f"you: {self.users[ctx.author][1]} \nThe card you can see from me: {self.users[ctx.author][3]}")
    while True:
      for i in range(2):
        await m.add_reaction(self.reactions[i])
      try:
        reaction, user, = await bot.wait_for("reaction_add", timeout=30.0, check=check)
      except asyncio.TimeoutError:
        await m.edit(content="Dang you took too long. Loser")
        await self.finish(ctx.author, m, ctx)
        break
      else:
          if reaction.emoji == self.reactions[0]: 
            await self.hit(ctx)
            if self.users[ctx.author][1] > 21:
              await self.finish(ctx.author, m, ctx)
              break
            else:
              await m.edit(content=f"you: {self.users[ctx.author][1]} \nThe card you can see from me: {self.users[ctx.author][3]}")
          elif reaction.emoji == self.reactions[1]:
            await self.finish(ctx.author, m, ctx)
            break
            #insert pass logic
      try: #tries to remove the user's reactions. ignores it if it doesn't have permission.
        await m.remove_reaction(self.reactions[0], ctx.author)
        await m.remove_reaction(self.reactions[1], ctx.author)
      except discord.Forbidden:
        pass
  async def deck_setup(self, ctx):
    self.values[ctx.author] = await self.setup(ctx)
  async def hit(self, ctx):
    temp = int(self.values[ctx.author][randint(0, len(self.values[ctx.author]))])
    if self.users[ctx.author][1] < 11 and temp == 1:
      self.users[ctx.author][1] += 11
      self.users[ctx.author][4] == "yes"
    else:
      self.users[ctx.author][1] += temp
    if self.users[ctx.author][1] > 21 and self.users[ctx.author][4] == "yes":
      self.users[ctx.author][1] -= 10
      self.users[ctx.author][4] == "no"
  async def setup(self, ctx):
      temp = []
      loop = -1
      self.cards[ctx.author] = [] #TODO insert emojis of every card
      for i in range(10):
        i += 1
        if i < 10:
          for x in range(4):
            temp.append(i)
        else:
          for x in range(16):
            temp.append(i)
      while True:
        loop += 1
        if loop >= 0 and self.users[ctx.author][2] < 13:
          self.users[ctx.author][2] += temp.pop(randint(0, 51 - loop))
        else:
          break
        if loop == 0:
          self.users[ctx.author][3] += self.users[ctx.author][2]
      return temp
  async def finish(self, author, m = "", ctx = ""):
    if m != "":
      if self.users[author][1] > 21:
        await m.edit(content=f"You busted stupid.\nYou: {self.users[author][1]}\nMe: {self.users[author][2]}\nYour reaction rn:")
      elif self.users[author][1] > self.users[author][2]:
        await m.edit(content=f"Congrats on winning\nYou: {self.users[author][1]}\nMe: {self.users[author][2]}\nMy reaction rn:")
      elif self.users[author][1] <= self.users[author][2]:
        await m.edit(content=f"Loser\nYou: {self.users[author][1]}\nMe: {self.users[author][2]}\nYour reaction rn:")
      await m.clear_reactions()
      await ctx.send("https://cdn.discordapp.com/attachments/938737694631161869/1019084787039875082/kazuma_kiryu_slams_a_desk_and_leaves.gif")
    self.users.pop(author)
    self.msg.pop(author)
    self.cards.pop(author)
    self.values.pop(author)
    
  
  """
  def __init__(self):
    #convert variables to dictionaries
    self.unumber = 0 #user number
    self.bnumber = 0 #bot number
    self.ace = False
    self.run = True
  def start(self, user):
    if self.run == False:
      return "You cannot play rn. Wait your turn or finish your game"
    else:
      self.run = False
    self.unumber = (randint(2,21))
    self.bnumber = (randint(2,21))
    if self.unumber in [2, 3]:
      self.unumber += 10
    while self.bnumber <= 13:
      self.bnumber += (randint(1,10))
    if self.bnumber > 21:
      result = [f"I'm stupid You:{self.unumber} Me: {self.bnumber}", "end"]
      self.run = True
      return result
    if self.unumber == 21:
      result = f"Wow you won!... cheater You:{self.unumber} Me:{self.bnumber}"
      self.run = True
      return result
    else:
      result = f"You have {self.unumber}. Do you want a hit?"
      return result
  def hit(self):
    temp = randint(1,10)
    if self.unumber + temp > 21 and self.ace is False:
      self.unumber += temp
      self.ace = False
      self.run = True
      return [f"You failed. Perish. You:{self.unumber} Me:{self.bnumber}", "end"]
    elif self.unumber + temp > 21 and self.ace is True:
      self.unumber += temp - 10
      self.ace = False
      return f"Saved by your ace! Want another hit? Score:{self.unumber}"
    elif temp == 1 and self.unumber < 11: #ace but lower than 11
      self.unumber += temp + 10
      self.ace = True
      return f"You got an ace! Want another hit? Score:{self.unumber}"
    elif self.unumber + temp <= 21 and self.unumber + temp >= 11 and temp == 1: #ace but 11 or higher
      self.unumber += temp
      self.ace = False #false as it being true would ruin bust logic
      return f"You got an ace! Want another hit? Score:{self.unumber}"
    else:
      self.unumber += temp
      return f"Nice. Want another hit? Score:{self.unumber}"

  def end(self):
    self.run = True
    if self.bnumber >= self.unumber:
      return [f"You lost loser. You:{self.unumber}. Me:{self.bnumber}", "end"]
    else:
      return [f"You won! You:{self.unumber}, Me:{self.bnumber}", "end"]
  def reset(self): #resets the run object if the game ends without input.
    self.run = True
    """