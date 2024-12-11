def sum_numbers(one, two):
    return one + two

def subtract(result, three):
    return result - three

def  add_and_subtract(one, two, three):
    sum = sum_numbers(one, two)
    subtraction = subtract(sum, three)
    return subtraction


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(add_and_subtract(first_number, second_number, third_number))