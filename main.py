import os
import discord

from dog import get_random_dog
from help import get_help
from random_functions import get_random_number
from team_generator import create_teams
from weather import get_weather
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get("TOKEN")

print(TOKEN)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!help'):
        await message.channel.send(get_help(message))

    if message.content.startswith('!random'):
        await message.channel.send(get_random_number(message))

    if message.content.startswith('!dog'):
        await message.channel.send(embed=get_random_dog())

    if message.content.startswith("!weather"):
        await message.channel.send(get_weather(message))

    if message.content.startswith("!teams"):
        await message.channel.send(create_teams(message))


client.run(TOKEN)
