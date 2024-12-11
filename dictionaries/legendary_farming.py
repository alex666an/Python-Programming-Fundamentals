items = {'shards': 0, 'fragments': 0, 'motes': 0}
obtained_item = False

while not obtained_item:
    current_items = input().split()
    for index in range(0, len(current_items), 2):
        value = int(current_items[index])
        key = current_items[index + 1].lower()
        if key not in items.keys():
            items[key] = 0
        items[key] += value
        if items['shards'] >= 250:
            print("Shadowmourne obtained!")
            items['shards'] -= 250
            obtained_item = True
        elif items['fragments'] >= 250:
            print("Valanyr obtained!")
            items['fragments'] -= 250
            obtained_item = True
        elif items['motes'] >= 250:
            print("Dragonwrath obtained!")
            items['motes'] -= 250
            obtained_item = True
        if obtained_item:
            break

for material, quantity in items.items():
    print(f"{material}: {quantity}")

