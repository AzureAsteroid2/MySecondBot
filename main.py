import discord, time, os, pytz, urmom, asyncio
from datetime import datetime
from Modules.insults import Insults
from Server.keep_alive import keep_alive
keep_alive()
urmom = urmom.Blackjack()
insults = Insults()
client = discord.Client()
@client.event
async def on_ready(): #The bot is ready :)
  print("Ready")
@client.event
async def on_message(m): #actions when a discord message is sent
  before = time.monotonic()
  m.content = m.content.lower() 
  if m.content.startswith("!ping"): #gives you the ping for the response
    message = await m.channel.send("Pong!")
    ping = int((time.monotonic() - before) *1000)
    await message.edit(content = f"Pong! {ping}ms")
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
    await m.channel.send(file=discord.File('Media/hello_mario.mp3')) #sends mp3 of "hello mario"
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
          await msg.edit(content= result[0])
        else:
          await msg.edit(content= result)
        if (type(result) is list) is True:
          await m.channel.send("kill me")
          break
        else:
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
            break
          else:
            if reaction.emoji == reaction1: 
              result = urmom.hit()
            elif reaction.emoji == reaction2:
              result = urmom.end()
          try: #tries to remove the user's reactions. ignores it if it doesn't have permission.
            await msg.remove_reaction(reaction1, m.author.id)
            await msg.remove_reaction(reaction2, m.author.id)
          except discord.Forbidden:
            pass
  if m.content.startswith("!moon"): #not done yet
    pass
client.run(os.environ['token'])

