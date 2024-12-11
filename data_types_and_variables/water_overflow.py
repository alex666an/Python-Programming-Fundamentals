water_tank_capacity = 255
total_litres = 0
number_of_lines = int(input())
for current_line in range(number_of_lines):
    current_litres = int(input())
    if water_tank_capacity - current_litres < 0:
        print('Insufficient capacity!')
        continue
    water_tank_capacity -= current_litres
    total_litres += current_litres
print(total_litres)