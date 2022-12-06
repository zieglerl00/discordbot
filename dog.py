import discord
import requests
import json


def get_random_dog():
    response_api = requests.get(f"https://dog.ceo/api/breeds/image/random")
    parse_json = json.loads(response_api.text)

    if parse_json["status"] == "success":
        embed = discord.Embed().set_image(url=parse_json["message"])
        return embed

    return "Api call failed..."
