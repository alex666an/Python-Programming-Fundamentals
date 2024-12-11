decoration_quantity = int(input())
shopping_days = int(input())
ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15
total_price = 0
total_christmas_spirit = 0
for current_day in range(1, shopping_days + 1):
    if current_day % 11 == 0:
        decoration_quantity += 2
    if current_day % 2 == 0:
        total_price += decoration_quantity * ornament_set_price
        total_christmas_spirit += 5
    if current_day % 3 == 0:
        total_price += decoration_quantity * (tree_skirt_price + tree_garland_price)
        total_christmas_spirit += 10 + 3
    if current_day % 5 == 0:
        total_price += decoration_quantity * tree_lights_price
        total_christmas_spirit += 17
        if current_day % 3 == 0:
            total_christmas_spirit += 30
    if current_day % 10 == 0:
        total_christmas_spirit -= 20
        total_price += tree_skirt_price + tree_garland_price + tree_lights_price
if shopping_days % 10 == 0:
    total_christmas_spirit -= 30
print(f"Total cost: {total_price}")
print(f"Total spirit: {total_christmas_spirit}")


