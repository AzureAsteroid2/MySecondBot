"""Handles Jokes"""
from random import randint
class Jokes:
  def __init__(self):
    self.joke = ""
    
  def joke_handler(self):
    with open('Modules/Text_Files/jokes.txt', 'r') as temp:
      for line in temp:
        all_jokes = (line.split('`'))
    amount = len(all_jokes)
    result = all_jokes[(randint(0, amount))]
    return result
    
  async def joke_adder(self, ctx, message):
    message = " ".join(message)
    message = message.replace("`", "")
    with open('Modules/Text_Files/jokes.txt', 'a') as temp:
      temp.write(f"`'{message}' - {ctx.author}.")
      temp.close()