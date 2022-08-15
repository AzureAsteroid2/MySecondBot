"""This bot is a passion project for discord and little else. If I want to do something.
This bot will one day make it possible. 

(To-Do: Change commands to be under ctx or @bot.command(), Image editor,
Have the !perish command get insults from a database instead of a txt file, Have users and a balance)"""

import discord, time, os, pytz, asyncio
from discord.ext import commands
from Modules.twealer import Twealer
from datetime import datetime
from Modules.insults import Insults
from Modules.urmom import Blackjack
from Server.keep_alive import keep_alive
#initialize all classes
keep_alive()
urmom = Blackjack()
insults = Insults()
twit = Twealer()
bot = commands.Bot(command_prefix="!", case_insensitive = True)
@bot.event
async def on_ready(): #The bot is ready :)
  print("Ready")
@bot.command()
async def ping(ctx):
  before = time.monotonic()
  message = await ctx.send("Pong!")
  ping = int((time.monotonic() - before) *1000)
  await message.edit(content = f"Pong! {ping}ms")
@bot.command()
async def friday(ctx):
  utc = pytz.utc
  today = datetime.now(utc)
  if today.weekday() == 4:
    await ctx.send("Today is Friday! TGIF!")
  else:
    await ctx.send("No... not Friday...")
@bot.command()
async def jacob(ctx):
  """Callout to Jacob."""
  await ctx.send("He's uber gay")
@bot.command()
async def perish(ctx):
  """Sends an insult"""
  await ctx.send(insults.insult_handler())
@bot.command()
async def james(ctx):
  """Sends an mp3 file for James. He's a cool guy"""
  try:
    message = await ctx.send(file=discord.File('Media/hello_mario.mp3'))
    reactions = ["🇭", "ℹ️", "👀", "🇲", "🇦", "🇷", "🇮", "🇴", "‼️"]
    for i in reactions:
      await message.add_reaction(i)
  except discord.Forbidden:
    await ctx.send("I don't have the permissions I need! No command for you")
@bot.command()
async def blackjack(ctx): #runs and manages a game of blackjack
  await urmom.start(ctx, bot)
  """
  result = urmom.start(ctx.author)
  msg = await ctx.send('loading...')
  if result == "Wow you won!... cheater":  
   await msg.edit(content= result)
  elif (type(result) is list) is True: #if it returns a list. The game has ended
    await msg.edit(content= result[0])
  elif result == "You cannot play rn. Wait your turn or finish your game": #someone else is playing
    await msg.edit(content= result)
  else:
    while True:
      if (type(result) is list) is True:
        await msg.edit(content= f'{result[0]} \n kill me') #end of the game. Sends results
        break
      else: #continues the game.
        await msg.edit(content= result)
        reaction1 = '✅'
        reaction2 = '❎'
        await msg.add_reaction(reaction1)
        await msg.add_reaction(reaction2)
        def check(reaction, user):
          if user == ctx.author:
            if str(reaction.emoji) == reaction1:
              return user == ctx.author and str(reaction.emoji) == reaction1
            if str(reaction.emoji) == reaction2:
              return user == ctx.author and str(reaction.emoji) == reaction2
        try:
          #waits for a reaction. If none is sent. end the game. 
          reaction, user = await bot.wait_for("reaction_add", timeout=60.0, check=check)
        except asyncio.TimeoutError:
          await msg.edit(content="Dang you took too long. Loser")
          urmom.reset() #prevents the game from being unplayable
          break
        else:
          if reaction.emoji == reaction1: 
            result = urmom.hit()
          elif reaction.emoji == reaction2:
            result = urmom.end()
        try: #tries to remove the user's reactions. ignores it if it doesn't have permission.
          await msg.remove_reaction(reaction1, ctx.author)
          await msg.remove_reaction(reaction2, ctx.author)
        except discord.Forbidden:
          pass
          """
@bot.command()
async def tweet(ctx, twitterid = 'mymoonphaseapp'):
  """Posts the tweet using a twitterid (the @name)."""
  await ctx.send(twit.steal(twitterid))

@bot.command()
async def tweet_daily(ctx, twitterid):
  """Sets up daily tweets from whatever twitterid you choose"""
  pass

  
bot.run(os.environ['token'])
"""
@client.event
async def on_message(m): #actions when a discord message is sent
  before = time.monotonic()
  m.content = m.content.lower() 
  
  if m.content.startswith("!ping"): #gives you the ping for the response
    message = await m.channel.send("Pong!")
    ping = int((time.monotonic() - before) *1000)
    await message.edit(content = f"Pong! {ping}ms")
    
  if m.content.startswith("!test"): #replaceable 
    pass
  if m.content.startswith("!friday"): #detects if it's friday or not and sends a message
    utc = pytz.utc
    today = datetime.now(utc)
    if today.weekday() == 4:
      await m.channel.send("Today is Friday! TGIF!")
    else:
      await m.channel.send("No... not Friday...")
  if m.content.startswith("!jacob"): #Jacob is in fact... super gay
    await m.channel.send("He's uber gay")
  if m.content.startswith("!perish"): #sends an insult
    await m.channel.send(insults.insult_handler())
  if m.content.startswith("!james"): #!sends a funny mp3 (consider making it join the vc)
    try:
      await m.channel.send(file=discord.File('Media/hello_mario.mp3')) #sends mp3 of "hello mario"
    except discord.Forbidden:
      await m.channel.send("I don't have the permissions I need! No command for you")
  if m.content.startswith("!blackjack"): #plays a quick game of blackjack with you
    result = urmom.start(m)
    msg = await m.channel.send('loading...')
    if result == "Wow you won!... cheater":  
     await msg.edit(content= result)
    elif (type(result) is list) is True:
      await msg.edit(content= result[0])
    elif result == "You cannot play rn. Wait your turn or finish your game":
      await msg.edit(content= result)
    else:
      while True:
        if (type(result) is list) is True:
          await msg.edit(content= f'{result[0]} \n kill me') #end of the game. Sends results
          break
        else: #continues the game.
          await msg.edit(content= result)
          reaction1 = '✅'
          reaction2 = '❎'
          await msg.add_reaction(reaction1)
          await msg.add_reaction(reaction2)
          def check(reaction, user):
            if user == m.author:
              if str(reaction.emoji) == reaction1:
                return user == m.author and str(reaction.emoji) == reaction1
              if str(reaction.emoji) == reaction2:
                return user == m.author and str(reaction.emoji) == reaction2
          try:
            reaction, user = await client.wait_for("reaction_add", timeout=60.0, check=check)
          except asyncio.TimeoutError:
            await msg.edit(content="Dang you took too long. Loser")
            urmom.reset()
            break
          else:
            if reaction.emoji == reaction1: 
              result = urmom.hit()
            elif reaction.emoji == reaction2:
              result = urmom.end()
          try: #tries to remove the user's reactions. ignores it if it doesn't have permission.
            await msg.remove_reaction(reaction1, m.author)
            await msg.remove_reaction(reaction2, m.author)
          except discord.Forbidden:
            pass
  if m.content.startswith("!moon"): #not done yet
    pass
  await bot.process_commands(m)
client.run(os.environ['token'])
"""
