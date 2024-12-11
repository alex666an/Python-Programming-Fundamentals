def all_characters(char_one:str, char_two:str) -> list:
    characters = []
    for current_character_as_digit in range(ord(character_one) + 1, ord(character_two)):
        characters.append(chr(current_character_as_digit))
    return characters


character_one = input()
character_two = input()
final_print = all_characters(character_one, character_two)
print(" ".join(final_print))