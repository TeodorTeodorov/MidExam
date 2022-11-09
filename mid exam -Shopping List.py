initial_list = input().split('!')
while True:
    commands = input()
    if commands == "Go Shopping!":
        break
    commands_split = commands.split(' ')
    command = commands_split[0]
    item = commands_split[1]

    # command, item = commands.split(' ')

    if command == 'Urgent':
        if item not in initial_list:
            initial_list.insert(0, item)

    if command == "Unnecessary":
        if item in initial_list:
            initial_list.remove(item)

    if command == 'Correct':
        old_item = item
        new_item = commands_split[2]

        # old_item, new_item = item.split(' ')
        if old_item in initial_list:
            old_item_index = initial_list.index(old_item)
            initial_list.insert(old_item_index, new_item)
            initial_list.remove(old_item)
    if command == 'Rearrange':
        if item in initial_list:
            initial_list.remove(item)
            initial_list.append(item)

print(', '.join(initial_list))