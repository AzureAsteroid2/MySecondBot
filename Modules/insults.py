"""Insults you with a list of insults. Fun times"""
from random import randint
class Insults:
  def __init__(self):
    self.insult = ""
  def insult_handler(self):
    with open('Modules/Text_Files/insults.txt', 'r') as temp:
      for line in temp:
        all_insults = (line.split('`'))
    amount = len(all_insults)
    result = all_insults[(randint(0, amount))]
    return result
    
    