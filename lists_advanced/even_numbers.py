number_list = list(map(int, input().split(', ')))
is_even_number = map(lambda x: x if number_list[x] % 2 == 0 else 'no', range(len(number_list)))

even_numbers = list(filter(lambda a: a != 'no', is_even_number))
print(even_numbers)