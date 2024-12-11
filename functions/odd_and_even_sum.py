def odd_even_sums(some_number: str):
    even_counter = 0
    odd_counter = 0
    for digit in some_number:
        if int(digit) % 2 == 0:
            even_counter += int(digit)
        else:
            odd_counter += int(digit)
    return odd_counter, even_counter


number = input()
odd_counter, even_counter = odd_even_sums(number)
print(f"Odd sum = {odd_counter}, Even sum = {even_counter}")