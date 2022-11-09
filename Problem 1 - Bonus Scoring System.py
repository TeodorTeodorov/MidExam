number_students = int(input())
total_number_of_lectures = int(input())
additional_bonus = int(input())
total_bonus = 0
max_bonus = 0
max_atented = 0
for student in range(number_students):
    count_of_attendances = int(input())
    total_bonus = count_of_attendances / total_number_of_lectures * (5 + additional_bonus)
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        max_atented = count_of_attendances
print(f'Max Bonus: {round(max_bonus)}.')
print(f'The student has attended {max_atented} lectures.')