array_values = [int(num) for num in input().split(' ')]
while True:
    elements = input()
    if elements == "end":
        break
    if elements == "decrease":
        for num in range(len(array_values)):
            array_values[num] -= 1
    else:
        command, first_num, sec_num = elements.split(' ')
        if command == "swap":
            array_values[int(first_num)], array_values[int(sec_num)] = array_values[int(sec_num)], array_values[
                int(first_num)]
        elif command == "multiply":
            array_values[int(first_num)] *= array_values[int(sec_num)]

array_values_to_rsting = [str(num) for num in array_values]
print(', '.join(array_values_to_rsting))
