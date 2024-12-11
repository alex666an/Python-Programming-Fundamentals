heroes = {}

command = input().split()

while command[0] != 'End':
    if command[0] == 'Enroll':
        hero_name = command[1]
        if hero_name not in heroes.keys():
            heroes[hero_name] = []
        else:
            print(f"{hero_name} is already enrolled.")
    elif command[0] == 'Learn':
        hero_name, spell_name = command[1], command[2]
        if hero_name not in heroes.keys():
            print(f"{hero_name} doesn't exist.")
        elif spell_name in heroes[hero_name]:
            print(f"{hero_name} has already learnt {spell_name}")
        else:
            heroes[hero_name].append(spell_name)
    elif command[0] == 'Unlearn':
        hero_name, spell_name = command[1], command[2]
        if hero_name not in heroes.keys():
            print(f"{hero_name} doesn't exist.")
        elif spell_name not in heroes[hero_name]:
            print(f"{hero_name} doesn't know {spell_name}.")
        else:
            heroes[hero_name].remove(spell_name)

    command = input().split()


