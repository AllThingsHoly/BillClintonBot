from discord.ext import commands
import os
import dotenv

dotenv.load_dotenv("keys.env")
DISCORD_KEY = os.getenv("DISCORD_KEY")

bot = commands.Bot("!", description="Music Bot")

@bot.event
async def on_ready():
    print("Ready")
    
@bot.command(pass_context=True)
async def hello(ctx):
    await ctx.send("hello!")
