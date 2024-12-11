budget = float(input())
price_for_kg_of_flour = float(input())
price_for_pack_of_eggs = price_for_kg_of_flour * 0.75
price_for_litre_of_milk = price_for_kg_of_flour * 1.25
bread_counter = 0
coloured_egg_counter = 0
bread_left = 0
ingredients_for_one_bread = price_for_pack_of_eggs + price_for_kg_of_flour + (price_for_litre_of_milk / 4)
while True:
    if ingredients_for_one_bread > budget:
        break
    bread_counter += 1
    coloured_egg_counter += 3
    if bread_counter % 3 == 0:
        coloured_egg_counter -= bread_counter - 2
    budget -= ingredients_for_one_bread

print(f'You made {bread_counter} loaves of Easter bread! Now you have {coloured_egg_counter} eggs and {budget:.2f}BGN left.')
