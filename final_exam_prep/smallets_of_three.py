def find_smallest(one, two, three):
    if one < two and one < three:
        return one
    elif two < one and two < three:
        return two
    elif three < one and three < two:
        return three

first_number = int(input())
second_number = int(input())
third_number = int(input())
smallest_number = find_smallest(first_number, second_number, third_number)
print(smallest_number)