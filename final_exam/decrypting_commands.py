text = input()
command = input().split()

while command[0] != 'Finish':
    if command[0] == 'Replace':
        current_char, new_char = command[1], command[2]
        if current_char in text:
            text = text.replace(current_char, new_char)
            print(text)
    elif command[0] == 'Cut':
        start_index, end_index = int(command[1]), int(command[2])
        if start_index in range(len(text)) and end_index in range(len(text)):
            text = text[:start_index] + text[end_index + 1:]
            print(text)
        else:
            print("Invalid indices!")
    elif command[0] == 'Make':
        if command[1] == 'Upper':
            text = text.upper()
            print(text)
        elif command[1] == 'Lower':
            text = text.lower()
            print(text)
    elif command[0] == 'Check':
        string_to_check = command[1]
        if string_to_check in text:
            print(f"Message contains {string_to_check}")
        else:
            print(f"Message doesn't contain {string_to_check}")
    elif command[0] == 'Sum':
        start_index, end_index = int(command[1]), int(command[2])
        if start_index >= 0 and start_index <= len(text) and end_index >= 0 and end_index <= len(text):
            substring = text[start_index:end_index + 1]
            ascii_sum = sum(ord(character) for character in substring)
            print(ascii_sum)
        else:
            print("Invalid indices!")






    command = input().split()