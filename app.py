import discord
from bottoken import BOTTOKEN
from discord import app_commands
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():    
    print("Syncing (/) Slash commands")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} (/) Slash commands")
        print(f"Logged in as {bot.user}")
    except Exception as e:
        print(e)    

#hybrid command
@bot.hybrid_command(name="ping", description="Check the bots latency")
async def ping(ctx):
    embed = discord.Embed(
        title="Pong!",
        description=f"My ping is {round(bot.latency * 1000)}ms.",
        color=0xe424ef
    )
    
    await ctx.send(embed=embed)



#slash command
@bot.tree.command(name="ping", description="Check the bots latency")
async def ping(ctx: discord.Interaction):
    embed = discord.Embed(
        title="Pong!",
        description=f"My ping is {round(bot.latency * 1000)}ms.",
        color=0xe424ef
    )
    
    await ctx.response.send_message(embed=embed)



#prefixed command
@bot.command()
async def ping(ctx):
    embed = discord.Embed(
        title="Pong!",
        description=f"My ping is {round(bot.latency * 1000)}ms.",
        color=0xe424ef
    )
    
    await ctx.send(embed=embed)

bot.run(BOTTOKEN)