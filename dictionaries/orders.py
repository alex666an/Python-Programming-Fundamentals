orders = {}

while True:
    current_order = input()
    if current_order == 'buy':
        break
    product_info = current_order.split()
    product_name, product_price, product_quantity = product_info[0], float(product_info[1]), int(product_info[2])

    if product_name not in orders.keys():
        orders[product_name] = {'price': product_price, 'quantity': product_quantity}
    else:
        orders[product_name]['quantity'] += product_quantity
        if product_price != orders[product_name]['price']:
            orders[product_name]['price'] = product_price

for product_name, product_info in orders.items():
    total_price = product_info['price'] * product_info['quantity']
    print(f"{product_name} -> {total_price:.2f}")




