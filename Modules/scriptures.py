"""Handles verses of the scriptures. (why am I doing this)"""
from random import randint
class Scripture:
  def __init__(self):
    pass
    
  def scripture_random(self):
    """gets a random verse from the scriptures"""
    with open("Modules/Text_Files/scriptures.txt", "r") as file:
      lines = file.readlines()
      amount = len(lines)
      result = lines[(randint(0,amount))]
      # ignore index 0. use the books dictionary for the string
      return result
     
      
        