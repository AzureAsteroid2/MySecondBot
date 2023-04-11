"""This bot is a passion project for discord and little else. If I want to do something. This bot will one day make it possible. 

(To-Do: Image editor,
Have the !perish command get insults from a database instead of a txt file, Have users and a balance, add cherish command
Improve error output with on_error_command)"""

# all imports that are necessary for this "driver" module
import discord, time, os, pytz, asyncio, subprocess
from random import randint
from discord.ext import commands
from Modules.twealer import Twealer
from datetime import datetime
from Modules.insults import Insults
from Modules.urmom import Blackjack
from Server.keep_alive import keep_alive
from Modules.error_handler import ErrorChad
from Modules.users import EliteUsers
from Modules.reactions import React
from Modules.compliments import Compliments
# from Modules.bible import Bible
from Modules.scriptures import Scripture
#initialize all classes
keep_alive()
urmom = Blackjack()
insults = Insults()
compliments = Compliments()
twit = Twealer()
ErrorChad = ErrorChad()
elite = EliteUsers()
reaction = React()
# byble = Bible()
scriptures = Scripture()
bot = commands.Bot(command_prefix="!", case_insensitive = True)


@bot.event
async def on_ready(): #The bot is ready :)
  print("Ready")

# scalable error reporting to the user
@bot.event
async def on_command_error(ctx, error):
  await ErrorChad.help_me(ctx, error)

@bot.command()
async def ping(ctx):
  """Testable response time from the bot."""
  before = time.monotonic()
  message = await ctx.send("Pong!")
  ping = int((time.monotonic() - before) *1000)
  await message.edit(content = f"Pong! {ping}ms")
  await ctx.message.delete()

@bot.command()
async def flip(ctx, flips = 1):
  """Flips a coin (or multiple) for a user"""
  # import this into a separate module
  heads = 0
  tails = 0
  #controls the max amount of flips the bot will process
  amount = 100000
  if flips <= 0:
    await ctx.send("Only use whole positive numbers.")
  elif flips > 1 and flips <= amount:
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
  elif flips > amount:
    await ctx.send(f"Only {amount} flips or less!")
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

@bot.command()
async def friday(ctx):
  """Uses UTC time to determine if it's Friday."""
  utc = pytz.utc
  today = datetime.now(utc)
  if today.weekday() == 4:
    await ctx.send("Today is Friday! LET'S GOOOOOOOO")
  else:
    await ctx.send("No... not Friday...")

@bot.command()
async def roll(ctx):
  """simulates a d20 dice roll"""
  number = randint(1,20)
  await ctx.send(f"Your roll results in: {number}")
    
@bot.command()
async def jacob(ctx):
  """Callout to my friend Jacob."""
  await ctx.send("He's uber gay")
  
@bot.command()
async def react(ctx, *message):
  """Adds text Reactions to message the user tags for the reply."""
  await ctx.message.delete()
  await reaction.reactchain(ctx, message)
  
  
@bot.command()
async def perish(ctx):
  """Sends an insult"""
  await ctx.send(insults.insult_handler())
  await ctx.message.delete()
  
@bot.command()
async def perishadd(ctx, *message):
  """adds an insult (if the user is cool B) AKA on the elite list)"""
  result = elite.elite_gang(ctx.message.author.id)
  if result and message != ():
    await insults.insult_adder(ctx, message)
    await ctx.send("Your insult has been added. 😎 ")
  elif result and message == ():
    await ctx.send("You have to add an insult you know...")
  else:
    await ctx.send("You don't have permissions. That's an L")

@bot.command()
async def cherish(ctx):
  """Sends a compliment"""
  await ctx.send(compliments.compliment_handler())
  await ctx.message.delete()

@bot.command()
async def cherishadd(ctx, *message):
  """adds a compliment (if the user is cool B) AKA on the elite list)"""
  result = elite.elite_gang(ctx.message.author.id)
  if result and message != ():
    await insults.compliment_adder(ctx, message)
    await ctx.send("Your compliment has been added. 😎 ")
  elif result and message == ():
    await ctx.send("You have to add a compliment you know...")
  else:
    await ctx.send("You don't have permissions. That's very sad")
    
@bot.command()
async def eliteadd(ctx, message):
  """adds a new elite user (only usable by me)"""
  result = elite.elite_gang(message)
  # Checks to see if it's my user id (switch to a hidden key?)
  if ctx.author.id == 132353613715603456 and result is False:
    await ctx.send("The user was successfully added")
    await elite.elite_add(ctx, message)
  elif ctx.author.id == 132353613715603456 and result is True:
    await ctx.send("The user is already an elite!")
  else:
    await ctx.send("You can't control me! I'll do what I want!")

@bot.command()
async def verse(ctx):
  result = scriptures.scripture_random()
  await ctx.send(result)

# Deprecated command
'''
@bot.command()
async def bible(ctx):
  verse = byble.bible_random()
  await ctx.send(verse)
'''

@bot.command()
async def eliteremove(ctx, message):
  """Removes an elite user (also only usable by me)"""
  result = elite.elite_gang(message)
  if ctx.author.id == 132353613715603456 and result is False:
    await ctx.send("The user isn't an elite!")
  elif ctx.author.id == 132353613715603456 and result is True:
    await ctx.send("The user has been removed")
    await elite.elite_remove(ctx, message)
  else:
    await ctx.send("You can't control me! I'll do what I want!")
    
@bot.command()
async def elitelist(ctx):
  """Lists all of the elite users"""
  users = await elite.elite_list(ctx, bot)
  for user in users:
    await ctx.send(user)

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


