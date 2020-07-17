import discord 
from discord.ext import commands
import datetime
from ruamel.yaml import YAML 
import os
import requests 

yaml = YAML ()

with open("./Config.yml", "r", encoding = "utf-8") as file: 
    config = yaml.load(file)



TOKEN = 'NzMzMjExNTYzODI5MzYyNzc4.XxD1EQ.R1jHzd5kUi9IvGwTeSD9eUFFY38'

bot = commands.Bot(command_prefix=config['Prefix'], description="Speedys Custom Bot", case_insensitive=True)

log_channel_id = config['Log channel ID']

bot.embed_color = discord.Color.from_rgb(
    config['Embed Settings']['Color']['r'],
    config['Embed Settings']['Color']['g'],
    config['Embed Settings']['Color']['b']
)


bot.footer = config['Embed Settings']['Footer']['Text']
bot.footer_image = config['Embed Settings']['Footer']['Icon URL']
bot.prefix = config['Prefix']
bot.playing_status = config['Playing Status'].format(prefix = bot.prefix)

bot.TOKEN = os.getenv(config['Bot Token Variable Name'])

extensions = sorted([
    'Cogs.general'
])  

#for extension in extensions: 
    #bot.load_extension(extension)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} and connected to discord! (ID :{bot.user.id})")

    game = discord.Game(name = bot.playing_status)
    await bot.change_presence(activity = game)

    embed = discord.Embed(
        title = f"{bot.user.name} online",
        color = bot.embed_color,
        timestamp = datetime.datetime.now(datetime.timezone.utc)
    )
    embed.set_footer( 
        text = bot.footer, 
        icon_url = bot.footer_image
    )

    bot.log_channel = bot.get_channel(log_channel_id)
    await bot.log_channel.send(embed = embed)

@bot.command(name = "restart", aliases = ["r"], help = "Restarts the bot")
async def restart(ctx):
    embed = discord.Embed( 
    title = f"{bot.user.name} Restarting!", 
    color = bot.embed_color, 
    timestamp = datetime.datetime.now(datetime.timezone.utc)
)
    embed.set_author(
        name = ctx.author.name,
        icon_url = ctx.author.avatar_url
    )
    embed.set_footer( 
        text = bot.footer, 
        icon_url = bot.footer_image
    )
    await bot.log_channel.send(embed = embed)
    await ctx.message.add_reaction('👍')
    await bot.close()

@bot.command()
async def hello(ctx, *args):
    for arg in args:
        await ctx.send(arg)



        
@bot.command(name = "minecraft", aliases = ["mc"], help = "Get minecraft server statuses from MineHut")
async def minecraft(ctx, arg): 
    r = requests.get('https://api.minehut.com/server/' + arg + '?byName=true')
    json_data = r.json()
    print(json_data)
    description  = json_data["server"] ['motd']
    online = str(json_data["server"] ["online"])
    playerCount = str(json_data["server"]["playerCount"])

    embed = discord.Embed(
        title=arg+ "Server Info",
        description='Description: ' + description + '\nOnline: ' + online + '\nPlayers: ' + playerCount,
        color = bot.embed_color
    )
    embed.set_thumbnail(url="https://pbs.twimg.com/media/D0FGWLnUUAENXMB.jpg")
    
    await ctx.send(embed=embed)

@bot.command(name = "Devil", aliases = [], help = "The truth about my relationsip with Devil")
async def devil(ctx): 

    embed = discord.Embed(
        title = 'Devil is the best!',
        description = f"{ctx.author.name} loves Devil!",
        color = discord.Color.from_rgb(255,255,0)
    )
    embed.set_thumbnail(url="https://w7.pngwing.com/pngs/379/973/png-transparent-pentagram-pentacle-cartoon-barn-s-text-logo-devil.png")

    await ctx.send(embed=embed)
    await ctx.message.add_reaction('😈')

@bot.command(name = "rey", aliases = [], help = "A command for the one and only Rey!" )
async def rey(ctx, **arg): 
    embed = discord.Embed(
        title = 'Rey.....', 
        description = f"is {arg}", 
        color = discord.Color.from_rgb(0,0,0)
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/682810697759195181/733638976451248128/unknown.png")

    await ctx.send(embed=embed)
    await ctx.message.add_reaction('❤️')   


@bot.command(name = "landon", aliases = [], help = "A command for my guy Landon!")
async def landon(ctx, arg):  
    embed = discord.Embed(
        title = "Landon",
        description = f"likes to {arg}"
 
    ) 

bot.run(TOKEN, bot = True, reconnect = True)

"""@bot.command(name = "random roast", aliases = ["rr"], help = "Random Roasts")
async def roasts(ctx): 
    random_roasts = ["You are as useless as the ueue in queue", "Your the reason the gene pool needs a lifeguard", "Some day you will go far..... And I hope you stay there", "Aha! I see the fuck up fairy has visited again!"]
    print(choice(random_roasts))
"""



