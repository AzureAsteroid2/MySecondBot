import discord
"""Manages users and currency that they have. Along with anything else
I may want to add in the future"""
class EliteUsers():
  def __init__(self):
    self.present = False
  async def elite_gang(self, ctx):
    """finds the user in the list (if they're present)"""
    self.present = False
    all_users = []
    with open('Modules/Text_Files/EpicUsers.txt', 'r') as temp:
      for line in temp:
        all_users = (line.split('`'))
      for i in all_users:
        i = int(i)
        if i == ctx:
          self.present = True
      """
      if f'ctx' in all_users:
        return self.present
      """
    return self.present

  async def elite_add(self, ctx, userid):
    await self.elite_gang(userid)
    if self.present == False:
      with open('Modules/Text_Files/EpicUsers.txt', 'a') as temp:
        temp.write(f"`{userid}")
        temp.close()
    return
    
  async def elite_remove(self, ctx, userid):
    await self.elite_gang(userid)
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

  async def elite_list(self, ctx, bot):
    """lists all of the users by their tags (not number ids)"""
    with open('Modules/Text_Files/EpicUsers.txt', 'r') as temp:
      for line in temp:
        all_users = (line.split('`'))
        user_tags = []
        for user in all_users:
          user = await bot.fetch_user(user)
          user_tags.append(user)
    return user_tags
    