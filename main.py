import random

# TODO:
""" Tags
"default_model": {
  "provider": "anthropic",
  "model": "claude-3-5-sonnet-20240620"
}
"""

dict_characters = {
    "Cassandra": "#tsundere #foxgirl",
    "Mildred": "#charlatan",
    "Luna": "#moe #yandere #artist",
    "Mr. Whiskers": "#cat #buisnessman #scammer",
    "Marcus": "#conspiracy_theorist",
    "Randy Hightower": "#radiantdawn"
}

print("The night beckons~ OwO")
#killer_character = random.choice(list(dict_characters.keys()))
#killer_character_tags = random.choice(list(dict_characters.values()))
killer_character, killer_character_tags = random.choice([*dict_characters.items()])
print("The killer is " + killer_character + " (" + killer_character_tags + ") !")

input()
