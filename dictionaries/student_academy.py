grades = {}
number_of_grades = int(input())

for _ in range(number_of_grades):
    name = input()
    current_grade = float(input())
    if name not in grades:
        grades[name] = []
        grades[name].append(current_grade)
    else:
        grades[name].append(current_grade)

for student, student_grades in grades.items():
    average_grade = sum(student_grades) / len(student_grades)
    if average_grade >= 4.5:
        print(f"{student} -> {average_grade:.2f}")




