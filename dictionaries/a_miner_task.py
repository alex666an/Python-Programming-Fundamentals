recourses = {}

while True:
    current_recourses = input()
    if current_recourses == 'stop':
        break
    current_quantity = int(input())
    if current_recourses not in recourses.keys():
        recourses[current_recourses] = 0
    recourses[current_recourses] += current_quantity

for resource, quantity in recourses.items():
    print(f"{resource} -> {quantity}")