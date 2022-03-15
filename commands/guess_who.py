# coding: utf-8
import os
import random

import discord

from prompt import *

print("guess who cmds")


@command()
async def startguesswho(ctx):
	"""display 'test'"""
	print("mais vazy fonctionne")
	components = [
		{
			"type": 2,
			"label": "c'est un bouton?",
			"style": 1,
			"custom_id": "bout en train"
		}
	]
	await ctx.send("starting guess who", components=components)
