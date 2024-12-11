def order(drink, quantity):
    if drink == 'coffee':
        return quantity * 1.50
    elif drink == 'coke':
        return quantity * 1.40
    elif drink == 'water':
        return quantity * 1.00
    elif drink == 'snacks':
        return quantity * 2.00


drink = input()
quantity = int(input())
result = order(drink, quantity)
print(f'{result:.2f}')
