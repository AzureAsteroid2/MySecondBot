"""Compliments you with a list of compliments. Fun times"""
from random import randint
class Compliments:
  def __init__(self):
    self.compliment = ""
    
  def compliment_handler(self):
    with open('Text_Files/compliments.txt', 'r') as temp:
      for line in temp:
        all_compliments = (line.split('`'))
    amount = len(all_compliments)
    result = all_compliments[(randint(0, amount))]
    return result
    
  async def compliment_adder(self, ctx, message):
    message = " ".join(message)
    message = message.replace("`", "")
    with open('Text_Files/compliments.txt', 'a') as temp:
      temp.write(f"`'{message}' - {ctx.author}.")
      temp.close()