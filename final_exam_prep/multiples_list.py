factor = int(input())
count = int(input())
list = []

for multiplier in range(1, count + 1):
    list.append(multiplier * factor)

print(list)