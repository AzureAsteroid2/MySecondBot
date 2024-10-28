"""This bot is a passion project for discord and little else. If I want to do something. This bot will one day make it possible. 

(To-Do: Image editor,
Have the !perish command get insults from a database instead of a txt file, Have users and a balance, add cherish command
Improve error output with on_error_command)"""


# all imports that are necessary for this "driver" module
import discord, time, os, pytz, asyncio, subprocess
from random import randint
from discord.ext import commands
from datetime import datetime
from Modules.urmom import Blackjack
from Server.keep_alive import keep_alive
from Modules.error_handler import ErrorChad
from Modules.users import Users
from Modules.reactions import React
from Modules.responses import Responses
from Modules.scriptures import Scripture
#initialize all classes
keep_alive()
urmom = Blackjack()
responses = Responses()
import Modules.talk_back
#initialize all classes
keep_alive()
urmom = Blackjack()
intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent for message handling
ErrorChad = ErrorChad()
elite = Users()
reaction = React()
owner_id = 132353613715603456 # my discord id! Yay!
scriptures = Scripture()
# all variables that are used between multiple functions
elite_file = "EpicUsers"
banned_file = "BannedUsers"
bot = commands.Bot(command_prefix="!", case_insensitive = True, intents=intents)

async def banlookup(ctx):
  """Simpler check to see if a user can use certain commands"""
  result = await elite.gang_lookup(ctx.message.author.id, banned_file)
  result = not result
  if result == False:
    await ctx.send("You're a Banned User. Die.")
  return result

async def elitelookup(ctx):
  """Simpler check to see if a user can use certain commands"""
  # print(ctx.message.author.id)
  result = await elite.gang_lookup(ctx.message.author.id, elite_file)
  if result == False:
    await ctx.send("You're not an Elite User. That means you can't use this command. That's an L")
  return result

async def melookup(ctx):
  """Checks to see if it's me (if it's not. Then tell the user)"""
  if owner_id != ctx.message.author.id:
    await ctx.send("You're not allowed to use this command")
    return False
  else:
    return True
    


@bot.event
async def on_ready(): #The bot is ready :)
  print("Ready")

# scalable error reporting to the user
@bot.event
async def on_command_error(ctx, error):
  await ErrorChad.help_me(ctx, error)

@bot.event
async def on_message(message):
  try:
    await message.channel.send(talk_back.responses[message.content])
  except KeyError:
    await bot.process_commands(message)


@bot.command()
@commands.check(banlookup)
async def ping(ctx):
  """Testable response time from the bot."""
  before = time.monotonic()
  message = await ctx.send("Pong!")
  ping = int((time.monotonic() - before) *1000)
  await message.edit(content = f"Pong! {ping}ms")
  await ctx.message.delete()

#this is ugly as crud.
@bot.command()
@commands.check(banlookup)
async def flip(ctx, flips = 1):
  """Flips a coin (or multiple) for a user"""
  # import this into a separate module
  heads = 0
  tails = 0
  #controls the max amount of flips the bot will process
  amount = 1000000
  if flips <= 0:
    await ctx.send("Only use whole positive numbers.")
  elif flips > 1 and flips <= amount:
    for _ in range(flips):
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
        await message.send(file=discord.File('.Media/Tails.png'))
        #reactions = ["🇹", "🇦", "🇮", "🇱", "🇸"]
     # for i in reactions:
        #await message.add_reaction(i)
    except discord.Forbidden:
      await ctx.send("I don't have the permissions I need! No command for you")

@bot.command()
@commands.check(banlookup)
async def friday(ctx):
  """Uses UTC time to determine if it's Friday."""
  utc = pytz.utc
  today = datetime.now(utc)
  if today.weekday() == 4:
    await ctx.send("Today is Friday! LET'S GOOOOOOOO")
  else:
    await ctx.send("No... not Friday...")

@bot.command()
@commands.check(banlookup)
async def roll(ctx):
  """simulates a d20 dice roll"""
  number = randint(1,20)
  await ctx.send(f"Your roll results in: {number}")
    
@bot.command()
@commands.check(banlookup)
async def jacob(ctx):
  """Callout to my friend Jacob."""
  await ctx.send("He's uber gay")
  
@bot.command()
@commands.check(elitelookup)
@commands.check(banlookup)
async def react(ctx, *message):
  """Adds text Reactions to message the user tags for the reply."""
  await ctx.message.delete()
  await reaction.reactchain(ctx, message)
  
  
@bot.command()
@commands.check(banlookup)
async def perish(ctx):
  """Sends an insult"""
  file_name = "insults"
  await response(ctx, file_name)
  
@bot.command()
@commands.check(elitelookup)
@commands.check(banlookup)
async def perishadd(ctx, *message):
  """adds an insult (if the user is cool B) AKA on the elite list)"""
  file_name = "insults"
  await responseadd(ctx, file_name, message)

@bot.command()
@commands.check(banlookup)
async def cherish(ctx):
  """Sends a compliment"""
  file_name = "compliments"
  await response(ctx, file_name)
  

@bot.command()
@commands.check(elitelookup)
@commands.check(banlookup)
async def cherishadd(ctx, *message):
  """adds a compliment (if the user is cool B) AKA on the elite list)"""
  file_name = "compliments"
  await responseadd(ctx, file_name, message)
  
    
@bot.command()
@commands.check(melookup)
async def eliteadd(ctx, message):
  """adds a new elite user (only usable by me)"""
  result = await elite.gang_lookup(message, elite_file)
  # Checks to see if it's my user id (switch to a hidden key?)
  if result:
    await ctx.send("The user is already an elite!")
  else:
    await ctx.send("The user was successfully added")
    await elite.gang_add(ctx, message, elite_file)
  
async def response(ctx, file_name):
  """For every single type of response (joke, insult, etc) handle that here."""
  await ctx.send(responses.response_handler(file_name))
  await ctx.message.delete()

async def responseadd(ctx, file_name, message):
  if message != ():
    await responses.response_adder(ctx, message, file_name)
    await ctx.send("Your compliment has been added. 😎 ")
  else:
    await ctx.send("You have to add a compliment you know...")
  
@bot.command()
@commands.check(banlookup)
async def verse(ctx):
  """Gets a random verse from the scriptures"""
  result = scriptures.scripture_random(ctx)
  await ctx.send(result)
  await ctx.message.delete()
  
@bot.command()
@commands.check(elitelookup)
@commands.check(banlookup)
async def vnext(ctx):
  """Goes to the next verse in the scriptures (for the user)"""
  result = scriptures.scripture_next(ctx)
  await ctx.send(result)
  await ctx.message.delete()

@bot.command()
@commands.check(elitelookup)
@commands.check(banlookup)
async def vprev(ctx):
  """Goes to the previous verse in the scriptures (for the user)"""
  result = scriptures.scripture_prev(ctx)
  await ctx.send(result)
  await ctx.message.delete()

# Deprecated command
'''
@bot.command()
async def bible(ctx):
  verse = byble.bible_random()
  await ctx.send(verse)
'''

#clean up to have a decorator check to see if it's the owner (me)
@bot.command()
async def eliteremove(ctx, message):
  """Removes an elite user (also only usable by me)"""
  result = await elite.gang_lookup(message, elite_file)
  if ctx.author.id == owner_id and result == False:
    await ctx.send("The user isn't an elite!")
  elif ctx.author.id == owner_id and result:
    await ctx.send("The user has been removed")
    await elite.gang_remove(ctx, message, elite_file)
  else:
    await ctx.send("You can't control me! I'll do what I want!")
    
@bot.command()
@commands.check(banlookup)
async def elitelist(ctx):
  """Lists all of the elite users"""
  users = await elite.gang_list(ctx, bot, elite_file)
  answer = ""
  for user in users:
    answer += f'{user}; '
  await ctx.send(answer)
  
@bot.command()
async def banadd(ctx, message):
  """adds a new elite user (only usable by me)"""
  result = await elite.gang_lookup(message, banned_file)
  # Checks to see if it's my user id (switch to a hidden key?)
  if ctx.author.id == owner_id and result == False:
    await ctx.send("The user was successfully added")
    await elite.gang_add(ctx, message, banned_file)
  elif ctx.author.id == owner_id and result:
    await ctx.send("The user is already a banned user")
  else:
    await ctx.send("You can't control me! I'll do what I want!")
    
@bot.command()
async def banremove(ctx, message):
  """Removes an elite user (also only usable by me)"""
  result = await elite.gang_lookup(message, banned_file)
  if ctx.author.id == owner_id and result == False:
    await ctx.send("The user isn't a banned user!")
  elif ctx.author.id == owner_id and result:
    await ctx.send("The user has been removed")
    await elite.gang_remove(ctx, message, banned_file)
  else:
    await ctx.send("You can't control me! I'll do what I want!")
    
@bot.command()
@commands.check(banlookup)
async def banlist(ctx):
  """Lists all of the elite users"""
  users = await elite.gang_list(ctx, bot, banned_file)
  answer = ""
  for user in users:
    answer += f'{user}; '
  await ctx.send(answer)
  
@bot.command()
@commands.check(banlookup)
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
@commands.check(banlookup)
async def blackjack(ctx): #runs and manages a game of blackjack
  await urmom.start(ctx, bot)

  

@bot.command()
@commands.check(banlookup)
async def tweet(ctx, twitterid = 'mymoonphaseapp'):
  """Posts the tweet using a twitterid (the @name)."""
  await ctx.send(twit.steal(twitterid))


bot.run(os.environ['token'])


