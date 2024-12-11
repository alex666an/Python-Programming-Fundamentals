parking_lot = {}
number_of_commands = int(input())

for parking_spaces in range(number_of_commands):
    command = input().split()
    if command[0] == 'register':
        username, license_plate = command[1], command[2]
        if username not in parking_lot:
            parking_lot[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate}")
            continue
    elif command[0] == 'unregister':
        username = command[1]
        if username not in parking_lot:
            print(f"ERROR: user {username} not found")
        else:
            del parking_lot[username]
            print(f"{username} unregistered successfully")

for username, license_plate in parking_lot.items():
    print(f"{username} => {license_plate}")