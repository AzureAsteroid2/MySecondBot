"""Handles the LARGE data from this program."""
from random import randrange
class Blackjack:
  def __init__(self):
    self.usernumber = 0 #user number
    self.botnumber = 0 #bot number
    self.ace = False
  def start(self, user):
    self.unumber.user = (randint(1,21))
    self.bnumber.user = (randint(1,21))
    while self.bnumber.user <= 13:
      self.bnumber.user += (randint(1,10))
    if self.bnumber.user > 21:
      result = ["I'm stupid", "end"]
    if self.unumber == 21:
      result = "Wow you won!... cheater"
      return result
    else:
      result = f"You have {self.unumber}. Do you want a hit?"
      return result
  def hit(self):
    temp = randint(1,10)
    if self.unumber + temp > 21 and self.ace is False:
      self.unumber += temp
      self.ace = False
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
    if self.bnumber >= self.unumber:
      return [f"You lost loser. You:{self.unumber}. Me:{self.bnumber}", "end"]
    else:
      return [f"You won! You:{self.unumber}, Me:{self.bnumber}", "end"]
  