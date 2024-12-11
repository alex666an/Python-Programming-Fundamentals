population = [int(person) for person in input().split(", ")]
min_wealth = int(input())

for current_person in range(len(population)):
    if population[current_person] < min_wealth:
        difference = min_wealth - population[current_person]
        if max(population) - difference >= min_wealth:
            current_index = population.index((max(population)))
            population[current_index] -= difference
            population[current_person] += difference
        else:
            print("No equal distribution possible")
            exit()

print(population)

