"""Handles the LARGE data from this program.
Also runs blackjack. (Future endeavors:
multiplayer. Actual cards in the deck)"""
from random import randint
import asyncio
class Blackjack:
  def __init__(self):
    self.users = {}
    self.msg = {}
    self.cards = {}
    self.values = {}
    self.reactions = ['✅','❎']
  async def start(self, ctx, bot):
    self.users[ctx.author] = ["question", 0, 0, "false"]
    self.msg[ctx.author] = await ctx.send("loading...")
    
  async def game(self, ctx, bot):
    def check(self, reaction, user, author):
      """helper function that checks if a message was reacted to"""
      if user == author:
        if str(reaction.emoji) == self.reactions[0]:
          return user == author and str(reaction.emoji) == self.reactions[0]
        if str(reaction.emoji) == self.reactions[1]:
          return user == author and str(reaction.emoji) == self.reactions[1]
    m = self.msg.get(ctx.author)
    for i in range(2):
      await m.add_reaction(self.reactions[i])
    try:
      reaction, user, ctx.author = await bot.wait_for("reaction_add", timeout=20.0, check=check)
    except asyncio.TimeoutError:
      await m.edit(content="Dang you took too long. Loser")
  async def deck(self, ctx):
    def setup(self):
      temp = []
      self.cards[ctx.author] = [] #TODO insert emojis of every card
      for i in range(9):
        if i < 9:
          for x in range(4):
            temp.append(f"{i}")
        else:
          for x in range(12):
            temp.append(f"{i}")
      return temp
      self.values[ctx.author] = setup()
  async def end(self,ctx,bot):
    pass
  
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