
pirates_shup_status = [int(num) for num in input().split('>')]
military_ship = [int(num) for num in input().split('>')]
vitality_chip = int(input())

index_count = 0
while True:
    commands = input()
    if commands == "Retire":
        break
    commands = commands.split(' ')
    print(commands)
    # if len(commands) == 3:
    #     print(commands)
    #     # commands[1] = int(commands[1])
    #     # commands[2] = int(commands[2])
    # elif len(commands) == 4:
    #     # commands[1] = int(commands[1])
    #     # commands[2] = int(commands[2])
    #     # commands[3] = int(commands[3])
    #     print(commands)
    if commands[0] == "Fire":

        if 0 <= commands[1] < len(military_ship):
            military_ship[commands[1]] -= commands[2]
            if commands[1] <= 0:
                print("You won! The enemy ship has sunken.")

        if commands[0] == 'Defend':
            if 0 <= start_index <= len(pirates_shup_status) and 0 <= end_index <= len(pirates_shup_status):
                pirates_shup_status[start_index] -= damage
                pirates_shup_status[end_index] -= damage
                if pirates_shup_status[start_index] <= 0 or pirates_shup_status[end_index] <= 0:

                    print("You lost! The pirate ship has sunken.")

    if commands[0] == "Status":
        for index in range(len(pirates_shup_status)):
            if vitality_chip * 0.2 < pirates_shup_status[index]:
                index_count += 1
            if index_count > 0:
                print(f"{index_count} sections need repair.")


    if commands[0] == "Repair":
        current_command, first_element, second_element = commands.split(' ')
        first_element = int(first_element)
        second_element = int(second_element)
        if 0 <= first_element <= len(pirates_shup_status):
            pirates_shup_status[first_element] += second_element
            if pirates_shup_status[first_element] > vitality_chip:
                pirates_shup_status[first_element] = vitality_chip

print(sum(pirates_shup_status))
print(sum(military_ship))
