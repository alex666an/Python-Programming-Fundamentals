number_of_strings = int(input())
for current_string in range(number_of_strings):
    string_type = input()
    if ',' in string_type or '.' in string_type or '_' in string_type:
        print(f"{string_type} is not pure!")
    else:
        print(f"{string_type} is pure.")