number_of_messages = int(input())
for current_message in range(number_of_messages):
    current_number = int(input())
    if current_number == 88:
        print('Hello')
    elif current_number == 86:
        print('How are you?')
    elif current_number < 88:
        print('GREAT!')
    else:
        print('Bye.')
