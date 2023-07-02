import discord
"""Manages users and currency that they have. Along with anything else
I may want to add in the future (change to SQLite)"""
class Users():
  def __init__(self):
    self.present = False
  async def gang_lookup(self, ctx, file):
    """finds the user in the list (if they're present)"""
    self.present = False
    all_users = []
    ctx = int(ctx)
    with open(f'Modules/Text_Files/{file}.txt', 'r') as temp:
      for line in temp:
        all_users = (line.split('`'))
      for i in all_users:
        # if i is nothing. do not try to read it.
        if i != "":
          i = int(i)
          if i == ctx:
            self.present = True
      """
      if f'ctx' in all_users:
        return self.present
      """
    return self.present

  async def gang_add(self, ctx, userid, file):
    await self.gang_lookup(userid, file)
    if self.present == False:
      with open(f'Modules/Text_Files/{file}.txt', 'a') as temp:
        temp.write(f"`{userid}")
        print(temp)
        temp.close()
    return
    
  async def gang_remove(self, ctx, userid, file):
    await self.gang_lookup(userid, file)
    if self.present:
      temp = open(f'Modules/Text_Files/{file}.txt', 'r')
      all_users = temp.read()
      all_users = all_users.split('`')
      if userid in all_users:
        all_users.remove(userid)
      done = "`".join(all_users)
      temp = open(f'Modules/Text_Files/{file}.txt', 'w')
      temp.write(done)
    return

  async def gang_list(self, ctx, bot, file):
    """lists all of the users by their tags (not number ids)"""
    with open(f'Modules/Text_Files/{file}.txt', 'r') as temp:
      for line in temp:
        all_users = (line.split('`'))
        user_tags = []
        for user in all_users:
          if user != "":
            user = await bot.fetch_user(user)
            user_tags.append(user)
    return user_tags
    