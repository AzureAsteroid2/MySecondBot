"""Handles the LARGE data from this program."""
from random import randint
class Blackjack:
  def __init__(self):
    self.unumber = 0 #user number
    self.bnumber = 0 #bot number
    self.ace = False
    self.run = True
  def start(self, user):
    if self.run == False:
      return "You cannot play rn. Wait your turn or finish your game"
    else:
      self.run = False
    self.unumber = (randint(2,21))
    self.bnumber = (randint(2,21))
    if self.unumber in [2, 3]:
      self.unumber += 10
    while self.bnumber <= 13:
      self.bnumber += (randint(1,10))
    if self.bnumber > 21:
      result = [f"I'm stupid You:{self.unumber} Me: {self.bnumber}", "end"]
      self.run = True
      return result
    if self.unumber == 21:
      result = f"Wow you won!... cheater You:{self.unumber} Me:{self.bnumber}"
      self.run = True
      return result
    else:
      result = f"You have {self.unumber}. Do you want a hit?"
      return result
  def hit(self):
    temp = randint(1,10)
    if self.unumber + temp > 21 and self.ace is False:
      self.unumber += temp
      self.ace = False
      self.run = True
      return [f"You failed. Perish. You:{self.unumber} Me:{self.bnumber}", "end"]
    elif self.unumber + temp > 21 and self.ace is True:
      self.unumber += temp - 10
      self.ace = False
      return f"Saved by your ace! Want another hit? Score:{self.unumber}"
    elif temp == 1 and self.unumber < 11: #ace but lower than 11
      self.unumber += temp + 10
      self.ace = True
      return f"You got an ace! Want another hit? Score:{self.unumber}"
    elif self.unumber + temp <= 21 and self.unumber + temp >= 11 and temp == 1: #ace but 11 or higher
      self.unumber += temp
      self.ace = False #false as it being true would ruin bust logic
      return f"You got an ace! Want another hit? Score:{self.unumber}"
    else:
      self.unumber += temp
      return f"Nice. Want another hit? Score:{self.unumber}"

  def end(self):
    self.run = True
    if self.bnumber >= self.unumber:
      return [f"You lost loser. You:{self.unumber}. Me:{self.bnumber}", "end"]
    else:
      return [f"You won! You:{self.unumber}, Me:{self.bnumber}", "end"]
  