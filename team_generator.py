import math
import random


def create_teams(message):
    players = message.content.replace("!teams ", "").split(" ")
    team_one = []
    return_str = "\nTEAM 1: \n"

    if bool(random.getrandbits(1)):
        team_one_size = math.floor(len(players) / 2)
    else:
        team_one_size = math.ceil(len(players) / 2)

    for i in range(int(team_one_size)):
        player = random.choice(players)
        team_one.append(player)
        players.remove(player)

    for player in team_one:
        return_str += f"{player}, "

    return_str += "\n\nTEAM 2: \n"

    for player in players:
        return_str += f"{player}, "

    return "```" + return_str + "```"
