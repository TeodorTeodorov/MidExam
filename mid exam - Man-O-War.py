def fire_func(index, damage, status):
    statuss = True
    if 0 <= index < len(status):
        status[index] -= damage
        if index <= 0:
            statuss = False
            return print("You won! The enemy ship has sunken.")
    return statuss


def defend_func(first_index, second_index, damages, ship_statuss):
    status_lost = False
    if 0 <= first_index <= len(ship_statuss) and 0 <= second_index <= len(ship_statuss):
        ship_statuss[first_index] -= damages
        ship_statuss[second_index] -= damages
        if ship_statuss[first_index] <= 0 or ship_statuss[second_index] <= 0:
            status_lost = True
            print("You lost! The pirate ship has sunken.")
    return status_lost


def repair_func(index, health, pirats_ship_status, vitality):
    if 0 <= index <= len(pirats_ship_status):
        pirats_ship_status[index] += health
        if pirats_ship_status[index] > vitality:
            pirats_ship_status[index] = vitality


def ship_status_func(status):
    index_count = 0
    while True:
        commands = input()
        if commands == "Retire":
            break
        if commands[0] == 'Defend':
            defend, start_index, end_index, damage = commands.split(' ')
            result = defend_func(int(start_index), int(end_index), int(damage), military_ship)
        else:
            current_command, first_element, second_element = commands.split(' ')
        if commands[0] == "Status":
            for index in range(len(pirates_shup_status)):
                if vitality_chip * 0.2 < pirates_shup_status[index]:
                    index_count += 1
            if index_count > 0:
                continue

            if current_command == "Fire":
                result = fire_func(int(first_element), int(second_element), status)

            if current_command == "Repair":
                result = repair_func(int(first_element), int(second_element), pirates_shup_status, vitality_chip)




    return result
pirates_shup_status = [int(num) for num in input().split('>')]
military_ship = [int(num) for num in input().split('>')]
vitality_chip = int(input())


