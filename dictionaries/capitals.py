countries = input().split(', ')
capitals = input().split(', ')
final_print = dict(zip(countries, capitals))
for country, capital in final_print.items():
    print(f"{country} -> {capital}")