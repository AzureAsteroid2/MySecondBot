"""Manages users and currency that they have. Along with anything else
I may want to add in the future"""
class EliteUsers():
  def __init__(self):
    self.present = False
  def elite_gang(self, ctx):
    """finds the user in the list (if they're present)"""
    self.present = False
    with open('Modules/Text_Files/EpicUsers.txt', 'r') as temp:
      for line in temp:
        all_users = (line.split('`'))
      if f'{ctx}' in all_users:
        self.present = True
    return self.present

    
  def elite_add(self, ctx, userid):
    self.elite_gang(userid)
    if self.present == False:
      with open('Modules/Text_Files/EpicUsers.txt', 'a') as temp:
        temp.write(f"`{userid}")
        temp.close()
    return
    
  def elite_remove(self, ctx, userid):
    self.elite_gang(userid)
    if self.present == True:
      temp = open('Modules/Text_Files/EpicUsers.txt', 'r')
      all_users = temp.read()
      all_users = all_users.split('`')
      if userid in all_users:
        all_users.remove(userid)
      done = "`".join(all_users)
      temp = open('Modules/Text_Files/EpicUsers.txt', 'w')
      temp.write(done)
      
    return