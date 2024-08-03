import random

# TODO:
# Tags:
    # #look #item etc
# Knowledge chains (acyclic directed graph):
    # GoindAroundTheWorld -> Got80Days -> ItsABet

dict_characters = {
    "Cassandra": "#tsundere #foxgirl",
    "Mildred": "#charlatan",
    "Luna": "#moe #yandere #artist",
    "Mr. Whiskers": "#cat #buisnessman #scammer",
    "Marcus": "#conspiracy_theorist",
    "Randy Hightower": "#radiantdawn"
}

user_action = ""

#killer_character = random.choice(list(dict_characters.keys()))
#killer_character_tags = random.choice(list(dict_characters.values()))
killer_character, killer_character_tags = random.choice([*dict_characters.items()])
print("The killer is " + killer_character + " (" + killer_character_tags + ") !")

while(user_action != "quit"):
    print("The night beckons~ OwO\n What do you do?")
    print (""" * (talk) with [Cassandra / Mildred / MrWhiskers]
 * (search) for clues""")

    user_action = input()

    if (user_action == "talk"):
        print("You talked")
    elif (user_action == "search"):
        print("You've found an important clue!")
