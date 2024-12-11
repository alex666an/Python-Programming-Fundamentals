def all_characters(first_char, second_char):
    characters = []
    for current_character_as_digit in range(ord(first_character) + 1, ord(second_character)):
        characters.append(chr(current_character_as_digit))
    return characters


first_character = input()
second_character = input()

final_print = all_characters(first_character, second_character)
print(" ".join(final_print))
