"""Runs the bot"""
import sys
import discord
import responses
import functions

async def send_message(message, user_message, is_private):
    """Gets response from responses.py"""
    try:
        #get response from responses.py get_response
        response = responses.get_response(message, user_message)

        #checks if the response is private
        if is_private is True:
            await message.author.send(response)
        else:
            await message.channel.send(response)

    #catches any exceptions
    except Exception as exception:
        print(exception)

#main func
def run_discord_bot():
    """Connects to Discord"""

    TOKEN = functions.get_token()
    if TOKEN == "":
        print("Nenašel jsem token, brrrr!")
        input()
        sys.exit()

    #important discord stuff
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    #event when running
    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    #event when someone text a message
    @client.event
    async def on_message(message):

        #checks if the autor of the message is not bot
        if message.author == client.user:
            return

        #sets variables
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        #log
        print(f'{username} said: "{user_message}" ({channel})')

        #checks prefixes
        if user_message[:3:] == '!ks': #public
            user_message = user_message[3:]
            await send_message(message, user_message, is_private=False)
        elif user_message[0] == '🐴': #public easter egg
            await send_message(message, user_message, is_private=False)
        #elif user_message[:3:] == '?ks': #private
            #user_message = user_message[3:]
            #await send_message(message, user_message, is_private=True)

    #starter
    try:
        client.run(TOKEN)
    except discord.errors.LoginFailure:
        print("Špatný token, brrrr!")
        input()
    #napovedy
    #embeds
