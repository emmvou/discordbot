# coding: utf-8
import os

from discord.ext import commands
from commands import init_cmds
import prompt
from dotenv import load_dotenv

load_dotenv()

client = prompt.bot
init_cmds()


@client.event
async def on_ready():
	print("We have logged in as {0.user}".format(client))


client.run(os.getenv("DISCORD_TOKEN"))
