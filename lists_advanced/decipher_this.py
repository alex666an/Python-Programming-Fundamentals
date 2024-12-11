message = input().split()
deciphered_message = ""
for word in message:
    word_list = list(word)
    digits = []
    for character in word_list:
        if character.isdigit():
            digits += character
    word_list = [word for word in word_list if word not in digits]
    number = int("".join(digits))
    word_list.insert(0, chr(number))
    word_list[1], word_list[-1] = word_list[-1], word_list[1]
    deciphered_message += f"{''.join(word_list)}"
print(deciphered_message)


