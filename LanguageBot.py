import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import os


load_dotenv() #Load environment variables
TOKEN = os.environ.get("GRAMMARBOT_TOKEN")
intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="$$", intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    for cog in os.listdir("./cogs"):
        if cog.endswith(".py"):
            try:
                await client.load_extension(f"cogs.{cog[:-3]}")
                print(f"{cog} Loaded!")
            except Exception as e:
                print(f"{cog} cannot be loaded:")

    @client.command()
    async def ping(ctx):
        await ctx.reply(f"Pong! Latency is {client.latency}")

client.run(TOKEN)
