"""Handles all kinds of responses (compliments, insults, jokes, etc)"""
from random import randint
class Responses:
  def __init__(self):
    pass
    
  def response_handler(self, response):
    with open(f'Modules/Text_Files/{response}.txt', 'r') as temp:
      for line in temp:
        all_responses = (line.split('`'))
    amount = len(all_responses)
    result = all_responses[(randint(0, amount))]
    return result
    
  async def response_adder(self, ctx, message, response):
    message = " ".join(message)
    message = message.replace("`", "")
    with open(f'Modules/Text_Files/{response}.txt', 'a') as temp:
      temp.write(f"`'{message}' - {ctx.author}.")
      temp.close()
