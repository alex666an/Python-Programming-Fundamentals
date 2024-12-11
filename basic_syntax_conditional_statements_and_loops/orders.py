number_of_orders = int(input())
coffe_price = 0
total_price = 0
for current_order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())

    if price_per_capsule > 100.00 or price_per_capsule < 0.01:
        continue
    elif days > 31 or days < 1:
        continue
    elif capsules_needed_per_day > 2000 or capsules_needed_per_day < 1:
        continue
    coffe_price = price_per_capsule * days * capsules_needed_per_day
    print(f"The price for the coffee is: ${coffe_price:.2f}")
    total_price += coffe_price
print(f"Total: ${total_price:.2f}")
