numbers_as_string = input().split()
numbers_as_digits = []
for number in numbers_as_string:
    numbers_as_digits.append(int(number))

smallest = min(numbers_as_digits)
biggest = max(numbers_as_digits)
sum_of_all = sum(numbers_as_digits)

print(f"The minimum number is {smallest}")
print(f"The maximum number is {biggest}")
print(f"The sum number is: {sum_of_all}")