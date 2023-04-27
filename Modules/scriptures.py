"""Handles verses of the scriptures. (why am I doing this)"""
from random import randint
class Scripture:
  def __init__(self):
    self.user_spot = {}
    with open("Modules/Text_Files/scriptures.txt", "r") as file:
      # declare and set them up here (so it only has to setup the "book" when the bot restarts)
      self.lines = file.readlines()
      self.amount = len(self.lines)
    
  def scripture_random(self, ctx):
    """gets a random verse from the scriptures"""
    index = randint(0,self.amount)
    self.user_spot[ctx.author] = index
    result = self.lines[index]
    return result
    
  def scripture_next(self, ctx):
    index = self.user_spot.get(ctx.author)
    index += 1
    result = self.lines[index]
    self.user_spot[ctx.author] = index
    return result

  def scripture_prev(self, ctx):
    index = self.user_spot.get(ctx.author)
    index -= 1
    result = self.lines[index]
    self.user_spot[ctx.author] = index
    return result
    
      
        