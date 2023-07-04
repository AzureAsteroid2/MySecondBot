import asyncio, discord

class ErrorChad():
  def __init__(self):
    pass
  async def help_me(self, ctx, error):
    if isinstance(error, discord.ext.commands.errors.BadArgument):
      if "!flip" in ctx.message.content:
        await ctx.send("Only use whole numbers!")
    print(error)