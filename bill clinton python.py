from discord.ext import commands
import os
import dotenv
'''imports stuff needed to run'''
dotenv.load_dotenv("keys.env")
DISCORD_KEY = os.getenv("DISCORD_KEY")

bot = commands.Bot("!", description="Music Bot")
'''messages'''
@bot.event
async def on_ready():
    print("Ready")
    
@bot.command(pass_context=True)
async def monica(ctx):
    await ctx.send("I deeeed nawwt have seckshuuuual relaytions with that wouhman.")

@bot.command(pass_context=True)
async def twentybucks(ctx):
    await ctx.send("Make sure its not counterfeit.")

@bot.command(pass_context=True)
async def Whitewater(ctx):
    await ctx.send("It is a hoax dammit!")

@bot.command(pass_context=True)
async def Hillary(ctx):
    await ctx.send("Where are my divorce papers.")

@bot.command(pass_context=True)
async def band(ctx):
    await ctx.send("You know, I played saxophone in high school.")

@bot.command(pass_context=True)
async def Esptein(ctx):
    await ctx.send("What a great guy.")

@bot.command(pass_context=True)
async def among(ctx):
    await ctx.send("SUS.")


@bot.command(pass_context=True)
async def cocktail(ctx):
    await ctx.send("My friend Bill Cosby has a really good cocktail recipe you should try.")

@bot.command(pass_context=True)
async def woman(ctx):
    await ctx.send("Meet me in my office.")

@bot.command(pass_context=True)
async def kms(ctx):
    await ctx.send("I could do that for you.")

'''key is used to login and run the code as the bot'''
bot.run(DISCORD_KEY)
