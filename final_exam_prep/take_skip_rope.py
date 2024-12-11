text = input()
numbers_list = []
non_numbers_list = ""
take_list = []
skip_list = []
output = ""


for character in text:
    if character.isdigit():
        numbers_list.append(int(character))
    else:
        non_numbers_list += character

for index, number in enumerate(numbers_list):
    if index % 2 == 0:
        take_list.append(number)
    else:
        skip_list.append(number)

for take, skip in zip(take_list, skip_list):
    if take == 0:
        non_numbers_list = non_numbers_list[skip:]
    elif take != 0:
        output = output + non_numbers_list[:take]
        non_numbers_list = non_numbers_list[skip + take:]

print(output)
