# coding: utf-8
import os
import random

import discord

from prompt import *

print("guess who cmds")


def fn():
	print("you got into the function")


@command()
async def startguesswho(ctx):
	"""display 'test'"""

	# components = [
	# 	{
	# 		"type": 2,
	# 		"label": "c'est un bouton?",
	# 		"style": 1,
	# 		"custom_id": "bout en train"
	# 	}
	# ]

	# view = discord.ui.View()
	# item = discord.ui.Button(style=discord.ButtonStyle.blurple, label="Click Me", custom_id="clickme")
	# view.add_item(item=item)

	class ViewWithButton(discord.ui.View):
		@discord.ui.button(style=discord.ButtonStyle.blurple, label='Click Me')
		async def click_me_button(self, button: discord.ui.Button, interaction: discord.Interaction):
			print("Yahaha, you clicked me")
			button.label = "you clicked me"

	# https://stackoverflow.com/questions/69524903/how-to-create-a-clickable-button-under-the-message
	await ctx.send("starting guess who", view=ViewWithButton())
