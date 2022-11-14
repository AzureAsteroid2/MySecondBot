"""This bot is a passion project for discord and little else. If I want to do something.
This bot will one day make it possible. 

(To-Do: Image editor,
Have the !perish command get insults from a database instead of a txt file, Have users and a balance)"""

import discord, time, os, pytz, asyncio, subprocess
from random import randint
from discord.ext import commands
from Modules.twealer import Twealer
from datetime import datetime
from Modules.insults import Insults
from Modules.urmom import Blackjack
from Server.keep_alive import keep_alive
from Modules.error_handler import ErrorChad
#initialize all classes
keep_alive()
urmom = Blackjack()
insults = Insults()
twit = Twealer()
ErrorChad = ErrorChad()
bot = commands.Bot(command_prefix="!", case_insensitive = True)


@bot.event
async def on_ready(): #The bot is ready :)
  print("Ready")

  
@bot.event
async def on_command_error(ctx, error):
  await ErrorChad.help_me(ctx, error)

  
@bot.command()
async def ping(ctx):
  before = time.monotonic()
  message = await ctx.send("Pong!")
  ping = int((time.monotonic() - before) *1000)
  await message.edit(content = f"Pong! {ping}ms")

  
@bot.command()
async def flip(ctx, flips = 1):
  heads = 0
  tails = 0
  if flips <= 0:
    await ctx.send("Only use whole positive numbers.")
  elif flips > 1:
    for i in range(flips):
      number = randint(1,2)
      if number == 1:
        heads += 1
      else:
        tails += 1
    if heads >= tails:
      temp = 'Media/Heads.png'
    else:
      temp = 'Media/Tails.png'
    await ctx.send(f"You had {heads} heads and {tails} tails")
    await ctx.send(file=discord.File(temp))
  else:
    number = randint(1,2)
    message = ctx
    try:
      if number == 1:
         await message.send(file=discord.File('Media/Heads.png'))
        #reactions = ["🇭", "🇪", "🇦", "🇩", "🇸"]
      else:
        await message.send(file=discord.File('Media/Tails.png'))
        #reactions = ["🇹", "🇦", "🇮", "🇱", "🇸"]
     # for i in reactions:
        #await message.add_reaction(i)
    except discord.Forbidden:
      await ctx.send("I don't have the permissions I need! No command for you")

    
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

  
@bot.command()
async def tweet(ctx, twitterid = 'mymoonphaseapp'):
  """Posts the tweet using a twitterid (the @name)."""
  await ctx.send(twit.steal(twitterid))


@bot.command()
async def tweet_daily(ctx, twitterid):
  """Sets up daily tweets from whatever twitterid you choose"""
  pass

  
try:
  bot.run(os.environ['token'])
except:
  print("restarting")
  subprocess.run("kill 1", shell = True)
