number_of_people = int(input())
elevator_capacity = int(input())
courses = 0
while number_of_people > 0:
    number_of_people -= elevator_capacity
    courses += 1
print(courses)