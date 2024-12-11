def is_palindrome(random_number_as_string: str) -> bool:
    return random_number_as_string == random_number_as_string[::-1]


numbers_as_string = input().split(', ')
for number_as_string in numbers_as_string:
    print(is_palindrome(number_as_string))