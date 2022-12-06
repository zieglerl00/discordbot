import os
import requests
import json

API_KEY = os.environ.get("API_KEY")


def get_location(content):
    return str(content).split(" ")[1]


def get_weather(message):
    response_api = requests.get(f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={get_location(message.content)}&aqi=no")
    parse_json = json.loads(response_api.text)

    if parse_json["error"]["code"] == 2008:
        return "API Key expired! :("

    return parse_json["current"]["condition"]["text"]
