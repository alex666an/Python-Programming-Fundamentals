numbers = input().split()
opposite_string_list = []

for number in numbers:
    current_number = -int(number)
    opposite_string_list.append(current_number)

print(opposite_string_list)
