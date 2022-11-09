first_number_of_students_per_hour = int(input())
second_number_of_students_per_hour = int(input())
third_number_of_students_per_hour = int(input())
number_of_students = int(input())
student_per_hour = first_number_of_students_per_hour + second_number_of_students_per_hour + third_number_of_students_per_hour
hour_count = 0
while number_of_students > 0:

    number_of_students -= student_per_hour
    hour_count += 1
    if hour_count % 4 == 0:
        hour_count += 1
    if number_of_students <= 0:
        break

print(f"Time needed: {hour_count}h.")
