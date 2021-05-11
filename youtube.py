import discord
from discord.ext import commands
from pytube import YouTube

bot = commands.Bot(command_prefix=("!"))

@bot.event
async def on_ready():
    print('----------------------------')
    print(f'{bot.user.name} Olarak Giriş Yapıldı')
    print(f'Discord Versiyonu {discord.__version__}')
    print('----------------------------')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f"!indir"))

@bot.command()
async def indir(ctx, url):
    path = ("assets")
    url = (f"{url}")
    yt = YouTube(f"{url}")

    try:
        YouTube(url).streams.first().download(path)
        await ctx.send(f"**📥 Video Şu Dizine İndiriliyor:** `{path}`")
        await ctx.send(f"**🎉 Video Adı:** `{yt.title}`")
        await ctx.send(f"**👍 Video başarıyla belirtilen dizine indirdildi.**")
    except:
        await ctx.send(f"**👎 Video indirilemedi. Bir hata ile karşılaşıldı.**")


bot.run('TOKEN')       
