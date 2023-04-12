"""Handles verses of the scriptures. (why am I doing this)"""
from random import randint
class Scripture:
  def __init__(self):
    with open("Modules/Text_Files/scriptures.txt", "r") as file:
      # declare and set them up here (so it only has to setup the "book" when the bot restarts)
      self.lines = file.readlines()
      self.amount = len(self.lines)
    
  def scripture_random(self):
    """gets a random verse from the scriptures"""
    result = self.lines[(randint(0,self.amount))]
    return result
     
      
        