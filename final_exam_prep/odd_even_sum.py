def odd_and_even(some_number):
    odd = 0
    even = 0
    for digit in some_number:
        if int(digit) % 2 == 0:
            even += int(digit)
        else:
            odd += int(digit)
    return odd, even


number = input()
odd, even = odd_and_even(number)
print(f"Odd sum = {odd}, Even sum = {even}")
