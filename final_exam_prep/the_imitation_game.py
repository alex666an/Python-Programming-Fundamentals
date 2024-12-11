encrypted_message = input()

while True:
    command = input()
    if command == 'Decode':
        break
    codes = command.split('|')
    command = codes[0]
    if command == 'Move':
        index = int(codes[1])
        encrypted_message = encrypted_message[index:] + encrypted_message[: index]
    elif command == 'Insert':
        index = int(codes[1])
        value = codes[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]
    elif command == 'ChangeAll':
        substring = codes[1]
        replacement = codes[2]
        encrypted_message = encrypted_message.replace(substring, replacement)

print(f"The decrypted message is: {encrypted_message}")

