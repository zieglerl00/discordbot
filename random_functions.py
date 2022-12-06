import random


def get_random_number(message):
    message_arr = str(message.content).lower().split(" ")

    if len(message_arr) < 3:
        return "Format: \n\t!random min_value max_value"

    if message_arr[1] == message_arr[2]:
        return message_arr[1]

    random_number = random.randrange(int(message_arr[1]), int(message_arr[2]))
    return "```" + str(random_number) + "```"

