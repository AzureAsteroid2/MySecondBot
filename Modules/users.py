"""Manages users and currency that they have. Along with anything else
I may want to add in the future"""
class EliteUsers():
  def __init__(self):
    self.permission = False
  def elite_gang(self, ctx):
    self.permission = False
    with open('Modules/Text_Files/EpicUsers.txt', 'r') as temp:
      for line in temp:
        all_users = (line.split('`'))
      if f'{ctx.message.author.id}' in all_users:
        self.permission = True
    return self.permission