companies = {}

while True:
    data = input()
    if ' -> ' not in data:
        break
    company_name, ID = data.split(' -> ')
    if company_name not in companies:
        companies[company_name] = []
    if ID not in companies[company_name]:
        companies[company_name].append(ID)

for company, employee_ID in companies.items():
    print(f"{company}")
    for id in employee_ID:
            print(f'-- {id}')
