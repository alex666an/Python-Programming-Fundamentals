start_index = int(input())
end_index = int(input())
for current_character in range(start_index, end_index + 1):
    current_character_as_string = chr(current_character)
    print(current_character_as_string, end= ' ')