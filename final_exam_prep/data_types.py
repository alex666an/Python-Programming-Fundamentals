def integer(type, num):
    return int(num) * 2
def real(type, num):
    return int(num) * 1.5
def string(type, num):
    return "$" + num + "$"

data_type = input()
number = input()

if data_type == 'int':
    final_print = integer(data_type, number)
    print(final_print)
elif data_type == 'real':
    final_print = real(data_type, number)
    print(f'{final_print:.2f}')
elif data_type == 'string':
    final_print = string(type, number)
    print(final_print)
