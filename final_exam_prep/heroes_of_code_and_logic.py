def playing_game(heroes_dict):

    while True:
        command = input().split(' - ')

        if command[0] == 'End':
            break

        elif command[0] == 'CastSpell':
            hero_name = command[1]
            mana_needed = int(command[2])
            spell_name = command[3]
            if heroes_dict[hero_name][1] >= mana_needed:
                heroes_dict[hero_name][1] -= mana_needed
                print(f"{hero_name} has successfully cast {spell_name} and now has {heroes_dict[hero_name][1]} MP!")
            else:
                print(f"{hero_name} does not have enough MP to cast {spell_name}!")

        elif command[0] == 'TakeDamage':
            hero_name = command[1]
            damage = int(command[2])
            attacker = command[3]
            if heroes_dict[hero_name][0] - damage > 0:
                heroes_dict[hero_name][0] -= damage
                print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes_dict[hero_name][0]} HP left!")
            else:
                del heroes_dict[hero_name]
                print(f"{hero_name} has been killed by {attacker}!")

        elif command[0] == 'Recharge':
            hero_name = command[1]
            amount = int(command[2])

            if heroes_dict[hero_name][1] + amount > 200:
                diff = 200 - heroes_dict[hero_name][1]
                heroes_dict[hero_name][1] += diff
                print(f"{hero_name} recharged for {diff} MP!")
            else:
                heroes_dict[hero_name][1] += amount
                print(f"{hero_name} recharged for {amount} MP!")

        elif command[0] == 'Heal':
            hero_name = command[1]
            amount = int(command[2])

            if heroes_dict[hero_name][0] + amount > 100:
                diff = 100 - heroes_dict[hero_name][0]
                heroes_dict[hero_name][0] += diff
                print(f"{hero_name} healed for {diff} HP!")
            else:
                heroes_dict[hero_name][0] += amount
                print(f"{hero_name} healed for {amount} HP!")

    return heroes_dict


def create_heroes(number_of_heroes, heroes_dict):
    for _ in range(number_of_heroes):
        data = input().split(' ')
        hero_name = data[0]
        health = int(data[1])
        mana = int(data[2])

        heroes_dict[hero_name] = [health, mana]

    return heroes_dict

def heroes_of_code_and_logic():
    heroes_dict = {}

    number_of_heroes = int(input())
    heroes_dict = create_heroes(number_of_heroes, heroes_dict)
    heroes_dict = playing_game(heroes_dict)

    for element in heroes_dict:
        print(element)
        print(f'  HP: {heroes_dict[element][0]}')
        print(f'  MP: {heroes_dict[element][1]}')

heroes_of_code_and_logic()

