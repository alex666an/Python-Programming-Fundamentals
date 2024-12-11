activation_key = input()
command = input().split('>>>')

while command[0] != 'Generate':
    if command[0] == 'Contains':
        substring = command[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif command[0] == 'Flip':
        start_index, end_index = int(command[2]), int(command[3])
        if command[1] == 'Upper':
            activation_key = activation_key[0:start_index] \
                             + activation_key[start_index:end_index].upper() \
                             + activation_key[end_index:]
        elif command[1] == 'Lower':
            activation_key = activation_key[0:start_index] \
                             + activation_key[start_index:end_index].lower() \
                             + activation_key[end_index:]

        print(activation_key)

    elif command[0] == 'Slice':
        start_index, end_index = int(command[1]), int(command[2])
        activation_key = activation_key[0:start_index] + activation_key[end_index:]

        print(activation_key)

    command = input().split('>>>')

print(f"Your activation key is: {activation_key}")

