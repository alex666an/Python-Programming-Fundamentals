def smallest(numbers_list:list):
    return min(numbers_list)


first_number = int(input())
second_number = int(input())
third_number = int(input())
smallest_number = smallest([first_number, second_number, third_number])
print(smallest_number)