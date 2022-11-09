lot_of_chest = input().split('|')
item_index_count = input()
sum = 0
counter = 0
total_sum = 0
removed_list = []
while item_index_count != 'Yohoho!':
    item_index_count = item_index_count.split(' ')
    if 'Loot' in item_index_count:
        item_index_count.remove('Loot')
        for item in item_index_count:
            if item not in lot_of_chest:
                lot_of_chest.insert(0, item)

    if item_index_count[0] == 'Drop':
        item_index_count.remove('Drop')
        for item in item_index_count:
            item = int(item)
            if item < len(lot_of_chest):
                removed_item = lot_of_chest[item]
                lot_of_chest.pop(item)
                lot_of_chest.insert(-1, removed_item)
    if 'Steal' in item_index_count:
        item_index_count.remove('Steal')
        for item in item_index_count:
            item = int(item)
            for u in range(item):
                removed_list.append(lot_of_chest[-1])
                lot_of_chest.pop(-1)
    item_index_count = input()
for las_item in lot_of_chest:
    counter += 1
    sum += len(las_item)
    total_sum = sum / counter
print(*removed_list)
if len(lot_of_chest) > 0:
    print(f'Average treasure gain: {total_sum:.2f} pirate credits.')

else:
    print("Failed treasure hunt.")

