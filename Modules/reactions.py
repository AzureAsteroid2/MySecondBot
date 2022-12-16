import asyncio

class React:
  def __init__(self):
    #set all emojis (fun)
    self.emojis = {
      'a' : '🇦', 
      'b' : '🇧', 
      'c' : '🇨',
      'd' : '🇩',
      'e' : '🇪',
      'f' : '🇫',
      'g' : '🇬',
      'h' : '🇭',
      'i' : '🇮',
      'j' : '🇯',
      'k' : '🇰',
      'l' : '🇱',
      'm' : '🇲',
      'n' : '🇳',
      'o' : '🇴',
      'p' : '🇵',
      'q' : '🇶',
      'r' : '🇷',
      's' : '🇸',
      't' : '🇹',
      'u' : '🇺',
      'v' : '🇻',
      'w' : '🇼',
      'x' : '🇽',
      'y' : '🇾',
      'z' : '🇿',
      'o2' : '🅾️'
    }
    self.charo = 0
  async def reactchain(self, ctx, message):
    # use ctx.reference to properly grab the reply. Then slap reactions onto it.
    self.charo = 0
    message = ("".join(message)).lower()
    id = ctx.message.reference.message_id
    reply = await ctx.fetch_message(id)
    # await reply.add_reaction(self.emojis.get("a"))
    
    while(message != ""):
      if self.charo == 1 and message[0] == "o":
        await reply.add_reaction(self.emojis.get('o2'))
      await reply.add_reaction(self.emojis.get(message[0]))
      if message[0] == "o":
        self.charo = 1
      message = message[1:]
    
    return
        
    # print(reply)
    # print(message)
    # print('test')
    
    