def password_validator(some_password: str) -> list:
    invalid_passwords = []
    if len(some_password) < 6 or len(some_password) > 10:
        invalid_passwords.append('Password must be between 6 and 10 characters')
    if not some_password.isalnum():
        invalid_passwords.append('Password must consist only of letters and digits')
    digits_counter = 0
    for character in some_password:
        if character.isdigit():
            digits_counter += 1
    if digits_counter < 2:
        invalid_passwords.append('Password must have at least 2 digits')
    return invalid_passwords


password = input()
password_errors = password_validator(password)
if not password_errors:
    print('Password is valid')
else:
    print('\n'.join(password_errors))