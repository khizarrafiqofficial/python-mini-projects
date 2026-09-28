from random import choice
subjects = [
    "A group of donkeys",
    "The flying Elephant",
    "Fish on land",
    "Ishowspeed",
    "MrBeast",
    "Angry bird",
    "The happy poor man",
    "Ronaldo",
]

actions = [
    "launches",
    "celebrate",
    "playing",
    "eating",
    "seeking",
    "sleeping",
    "drops",
    "working",
]

places_or_things = [
    "at street food",
    "during PSL match",
    "at data darbar",
    "at spaceX",
    "a birthday",
    "inside basement",
    "in public",
    "a cup of icecream",
]

while True:
    subject = choice(subjects)
    action = choice(actions)
    place_or_thing = choice(places_or_things)

    news = (f"BREAKING NEWS: {subject} {action} {place_or_thing}.")
    print("\n" + news)

    user = input("\nDo you want to continue (Yes/No): ").strip().lower()
    if user == "no":
        break

print("Good Byee! Have a fun day.")
