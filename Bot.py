import discord 
from discord.ext import commands
import datetime
from ruamel.yaml import YAML 
import os
import requests 
import random

yaml = YAML ()

with open("./Config.yml", "r", encoding = "utf-8") as file: 
    config = yaml.load(file)



TOKEN = 'NzMzMjExNTYzODI5MzYyNzc4.XxGfrA.xMRL685c1zolCu9luiQ0PZx6hjg'

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
    embed.set_thumbnail(url="https://estparts.ru/upload/medialibrary/15f/imagem_png_online_2.png")

    bot.log_channel = bot.get_channel(log_channel_id)
    await bot.log_channel.send(embed = embed)

@bot.command(name = ":restart", aliases = ["restart", "r"], help = "Restarts the bot")
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
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTDQMpcOgY1JYMCe51Ybxm_r_M_VZV-VX6Z9Q&usqp=CAU")
    await bot.log_channel.send(embed = embed)
    await ctx.message.add_reaction('👍')
    await bot.close()

def setup(bot):
    bot.add_Cog(General(bot))

@bot.command(name = ":write", aliases = [], help = "Sends what you send")
async def write(ctx, *args):
    for arg in args:
        await ctx.send(arg)

@bot.command(name = ":wfm", aliases = ["wfm"], help = "Sends what you sent and deletes your message")
async def wfm(ctx,*arg, **kwargs):
    args = ' '.join(arg)
    await ctx.send(args)
    await ctx.message.delete()

@bot.command(name = ":del", aliases = ["del"], help = "Deletes the specified amount of messages")
async def clear(ctx, amount: int):
    await ctx.send("Deleting Messages........")
    await ctx.channel.purge(limit= amount+1)


        
@bot.command(name = ":minecraft", aliases = ["mc"], help = "Get minecraft server statuses from MineHut")
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

@bot.command(name = ":devil", aliases = ["devil"], help = "The truth about my relationsip with Devil")
async def coolrat(ctx): 
    urlone = "https://w7.pngwing.com/pngs/379/973/png-transparent-pentagram-pentacle-cartoon-barn-s-text-logo-devil.png"
    urltwo = "https://i7.pngguru.com/preview/533/989/263/pentagram-satanism-sigil-of-baphomet-devil.jpg"
    urlthree = "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcS26r4ZkaOVK_EjysvMVilyw2mMp7m8P8d1cA&usqp=CAU"
    urlfour = "https://images.hdqwalls.com/wallpapers/demon-daughter-nightcore-devil-3c.jpg"
    urlfive = "https://image.shutterstock.com/image-vector/devil-resides-anyones-soul-this-260nw-1405318610.jpg"
    rurl = [urlone, urltwo, urlthree, urlfour, ]
    urll = random.choice(rurl)
    embed = discord.Embed(
        title = 'Devil is the best!',
        description = f"{ctx.author.name} loves Devil!",
        color = discord.Color.from_rgb(255,255,0)
    )
    embed.set_thumbnail(url=urll)

    await ctx.send(embed=embed)
    await ctx.message.add_reaction('😈')

@bot.command(name = ":rey", aliases = ["rey"], help = "A command for the one and only Rey!" )
async def Ey(ctx, *arg, **kwargs): 
    urlone = "https://cdn.discordapp.com/attachments/682810697759195181/733638976451248128/unknown.png"
    urltwo = "https://images.wsj.net/im-144607?width=620&size=1"
    urlthree = "https://townsquare.media/site/366/files/2020/01/Cannibal-Corpse.jpg?w=980&q=75"
    rurl = [urlone, urltwo, urlthree]
    urll = random.choice(rurl)
    args = ' '.join(arg)
    embed = discord.Embed(
        title = 'Rey.....', 
        description = f"is {args}", 
        color = discord.Color.from_rgb(0,0,0)
    )
    embed.set_thumbnail(url=urll)

    await ctx.send(embed=embed)
    await ctx.message.add_reaction('❤️')   


@bot.command(name = ":landon", aliases = ["landon"], help = "A command for my guy Landon!")
async def landon(ctx, *arg, **kwargs): 
    urlone = "https://storage.bhs.cloud.ovh.net/v1/AUTH_e70735f8b712454ba568a52e9776e481/autozin/imagesl/027120160814/57b0bbe162f52.jpg"
    urltwo = "https://i.ebayimg.com/images/g/YR8AAOSwd9heThFD/s-l600.jpg"
    rurl = [urlone, urltwo]
    urll = random.choice(rurl)
    args = ' '.join(arg)
    embed = discord.Embed(
        title = "Landon",
        description = f"likes to {args}",
        color = discord.Color.red()
    ) 
    embed.set_thumbnail(url=urll)
    await ctx.send(embed=embed)
    await ctx.message.add_reaction('😎')

@bot.command(name = ":bpfp", aliases = ["bpfp"], help = "The bots Profile Picture")
async def bpfp(ctx): 
    embed = discord.Embed(
        title = f"{bot.user.name}'s' Profile Picture", 
        color = discord.Color.from_rgb(0,0,0)
    )
    embed.set_thumbnail(url=bot.user.avatar_url)

    await ctx.send(embed=embed)
    await ctx.message.add_reaction('🆗')

@bot.command(name = ":pfp", aliases = ["pfp"], help = "Users Profile Picture")
async def pfp(ctx, user: discord.Member = None): 
   if user: 
        embede = discord.Embed(
            title = f"{user.name}'s Profile Picture",
            color = discord.Color.blue()
        )
        embede.set_thumbnail(url=user.avatar_url)
        
        await ctx.send(embed=embede)
        await ctx.message.add_reaction('👌')
   else: 
        embed = discord.Embed(
            title = f"{ctx.author.name}'s Profile Pic",
            color = discord.Color.blue()
        )
        embed.set_thumbnail(url=ctx.author.avatar_url)
        
        await ctx.send(embed=embed)
        await ctx.message.add_reaction('👌')

    

@bot.command(name = ":roast", aliases = ["roast"], help = "Random roasts... Quite self explanitory")
async def aaa(ctx, user: discord.Member = None): 
    randomroasts = ["You are as useless as the ueue in queue", "Your the reason the gene pool needs a lifeguard", "Some day you will go far..... And I hope you stay there", "Aha! I see the fuck up fairy has visited again!"]
    randomroast = random.choice(randomroasts)
    await ctx.message.add_reaction('🔥')
    if user == user: 
        await ctx.send(randomroast)
    elif user == ctx.author.id: 
        await ctx.send("You want to roast yourself? Dummy, go chose something else you are not worth it")
    else: 
        await ctx.send("Who are you even trynna roast?")

@bot.command(name= ":NumberTrivia", aliases = ["NumTriv"], help = "Trivia about Numbers")  #Test Stage
async def num(ctx): 
    url = "https://numbersapi.p.rapidapi.com/6/21/date"

    querystring = {"fragment":"true","json":"true"}

    headers = {
        'x-rapidapi-host': "numbersapi.p.rapidapi.com",
        'x-rapidapi-key': "d90907d682mshaf9e3588d13792dp12a0d7jsn4c37662c16a0"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    embed = discord.Embed(
        title = 'Number Trivia',
        description = response.text, 
        color = discord.Color.from_rgb(255,255,0)

    )
    await ctx.send(embed=embed)
    print(response.text)
        
@bot.command(name = ":Emma", aliases = ["emma"], help = "A command for the one and only Emma!")
async def em(ctx, *arg, **kwarg): 
    urlone = "https://res.cloudinary.com/hio22hxcn/image/upload/v1462848158/top59c3sxyutd1bnkjzd.jpg"
    urltwo = "https://www.kitchensanctuary.com/wp-content/uploads/2017/01/Pasta-bake-with-chicken-and-bacon-tall-FS.jpg"
    urlthree = "https://images.squarespace-cdn.com/content/v1/540f9f10e4b04f85eb69113d/1445477559159-JUYHTS3BQYNA9B2Q76G2/ke17ZwdGBToddI8pDm48kKV0nEQLrZCZyN20-sdpYlF7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z4YTzHvnKhyp6Da-NYroOW3ZGjoBKy3azqku80C789l0ivq7Q1ckvJa8MA8qNUlEOZ5IGU-1O_EUPktdRWJqBeswtSHa-_ZlYvzXGRIA25Fyg/The+Bench+Burger.jpg?format=2500w"
    urlfour = "https://media-cdn.tripadvisor.com/media/photo-s/15/7b/7e/56/pannenkoeken-paviljoen.jpg"
    urlfive = "https://pbs.twimg.com/media/DmwvGXZX4AEgQpt.jpg:large"
    urll = [urlone, urltwo, urlthree, urlfour, urlfive]
    rurl = random.choice(urll)
    rcolor = [discord.Color.red(), discord.Color.blue()]
    rrcolor = random.choice(rcolor)
    embed = discord.Embed(
        title = 'Emma...',
        description = '...',
        color = rrcolor
    )
    embed.set_thumbnail(url=rurl)
    await ctx.send(embed=embed)

@bot.command(name = ":GaeRate", aliases = ["gr", "gaerate"], help = "How Gae are You?")
async def gae(ctx, user: discord.Member = None ):
    n = str(random.randint(1,100))
    rcolor = [discord.Color.red(), discord.Color.blue()]
    rrcolor = random.choice(rcolor)
    if user: 
        embed = discord.Embed(
            
            title = f"How gae is {user}",
            description = f"{user} is " + n + "percent gae",
            color = rrcolor 
        )
        embed.set_thumbnail(url = "https://images.vexels.com/media/users/3/150997/isolated/preview/76d7b2457f16f4aa11b77d8926e48ff8-gay-heart-flag-by-vexels.png")
        await ctx.send(embed=embed)
    else: 
        embede = discord.Embed(
            
            title = f"How gae is {ctx.author}",
            description = f"{ctx.author} is " + n + " percent gae",
            color = rrcolor 
        )
        embede.set_thumbnail(url = "https://images.vexels.com/media/users/3/150997/isolated/preview/76d7b2457f16f4aa11b77d8926e48ff8-gay-heart-flag-by-vexels.png")
        await ctx.send(embed=embede)
        
@bot.command(name = ":GamereRate", aliases = ["gmr", "gamerrate"], help = "Are you an epic gamer?")
async def gamer(ctx, user: discord.Member = None ):
    n = str(random.randint(1,100))
    rcolor = [discord.Color.red(), discord.Color.blue()]
    rrcolor = random.choice(rcolor)
    if user: 
        embed = discord.Embed(
            
            title = f"How much of an epic gamer is {user}",
            description = f"{user} is " + n + " percent gamer",
            color = rrcolor 
        )
        if n >= str("50"): 
            embed.set_thumbnail(url="https://tr.rbxcdn.com/8e0e05183dd997d17e3effb0b889b7a6/420/420/Shirt/Png")
        else: 
            embed.set_thumbnail(url="https://www.kindpng.com/picc/m/303-3036589_epic-gamer-png-transparent-png.png")
        
        await ctx.send(embed=embed)
    else: 
        embede = discord.Embed(
            
            title = f"How much of an epic gamer is {ctx.author}",
            description = f"{ctx.author} is " + n + " percent gamer",
            color = rrcolor 
        )
        if n >= str("50"): 
            embede.set_thumbnail(url="https://tr.rbxcdn.com/8e0e05183dd997d17e3effb0b889b7a6/420/420/Shirt/Png")
        else: 
            embede.set_thumbnail(url="https://www.kindpng.com/picc/m/303-3036589_epic-gamer-png-transparent-png.png")
        await ctx.send(embed=embede)
    
@bot.event(name = "verify", aliases = [""])
async def veri(): 
    discord.on_member_join()
    if time.time() - member.created_at.timestamp() < 86400: 
        




bot.run(TOKEN, bot = True, reconnect = True)

"""@bot.command(name = "random roast", aliases = ["rr"], help = "Random Roasts")
async def roasts(ctx): 
    random_roasts = ["You are as useless as the ueue in queue", "Your the reason the gene pool needs a lifeguard", "Some day you will go far..... And I hope you stay there", "Aha! I see the fuck up fairy has visited again!"]
    print(choice(random_roasts))
"""



