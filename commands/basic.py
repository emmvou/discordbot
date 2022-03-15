# coding: utf-8
import os
import random
from _csv import reader

import discord

from prompt import *

print("basic cmds")


@command()
async def hello(ctx):
	"""display 'hello'"""
	await ctx.send("hello")


@command()
async def say(ctx, msg: str):
	"""display msg"""
	await ctx.send(msg)


@command()
async def add(ctx, a: int, b: int):
	"""add two integers"""
	await ctx.send(str(a + b))


# @command()
# async def getuser(ctx, user: discord.Member, message):
#    """sends a dm to user"""
#    await user.send("message")


@command()
async def participatesecretsanta(ctx):
	"""stores participation in secret santa, whishlist is optional"""
	if os.path.exists("secret_santa.csv"):
		file = open("secret_santa.csv", 'a', encoding="utf-8")
	else:
		file = open("secret_santa.csv", 'w', encoding="utf-8")
		file.write("id,name")
	file.write(f"\n{str(ctx.message.author.id)},{str(ctx.message.author.name)}")
	file.close()
	await ctx.send("you are now registered")


@command()
async def gosecretsanta(ctx):
	"""starts secret santa and sends dm to every registered participant"""
	with open("secret_santa.csv") as file:
		csv_reader = reader(file)
		participants = list()
		for row in csv_reader:
			participants.append(row)
	participants.pop(0)
	random.shuffle(participants)
	for index, elem in enumerate(participants):
		user = await bot.fetch_user(elem[0])
		nxt = participants[(index + 1) % len(participants)]
		nxtuser = await bot.fetch_user(nxt[0])
		await user.send("Tu vas devoir offrir ton cadeau à : " + str(nxtuser.name))
	await ctx.send("Secret santa is starting now!")
