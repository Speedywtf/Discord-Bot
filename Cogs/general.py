import discord 
from discord.ext import commands

class General(commands.Cog, name = "General"): 
    def __init__(self, bot):
        self.bot = bot
        print('Loaded General Cog.')

def setup(bot):
    bot.add_Cog(General(bot))