integers = input().split()
list = []
for integer in integers:
    list.append(int(integer))

result = sorted(list)
print(result)