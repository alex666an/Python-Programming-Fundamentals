number_of_wagons = [0] * int(input())

while True:
    command = input().split()
    if command[0] == 'End':
        print(number_of_wagons)
        break
    elif command[0] == 'add':
        number_of_people = int(command[1])
        number_of_wagons[-1] += number_of_people
    elif command[0] == 'insert':
        index = int(command[1])
        people = int(command[2])
        number_of_wagons[index] += people
    elif command[0] == 'leave':
        index = int(command[1])
        people = int(command[2])
        number_of_wagons[index] -= people

