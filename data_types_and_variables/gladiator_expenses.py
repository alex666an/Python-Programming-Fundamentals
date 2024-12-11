lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
broken_helmets = lost_fights // 2
broken_swords = lost_fights // 3
broken_shields = lost_fights // (2 * 3)
broken_armor = broken_shields // 2
helmet_expenses = broken_helmets * helmet_price
sword_expenses = broken_swords * sword_price
shield_expenses = broken_shields * shield_price
armor_expenses = broken_armor * armor_price
total_expenses = helmet_expenses + shield_expenses + sword_expenses + armor_expenses
print(f"Gladiator expenses: {total_expenses:.2f} aureus")
