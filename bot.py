"""Runs the bot"""
import sys
import discord
from classes import MyBot
from config import DISCORD_TOKEN

def runDiscordBot():
    """Runs Discord bot"""
    bot: MyBot = MyBot()

    try:
        bot.run(DISCORD_TOKEN)
    except discord.errors.LoginFailure:
        print("Špatný Discord token!")
        input()
        sys.exit()
