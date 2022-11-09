shoot_target = [int(num) for num in input().split(' ')]
counter = 0
while True:
    index = input()
    if index == "End":
        break
    index = int(index)

    if 0 <= index < len(shoot_target) and shoot_target[index] != -1:
        current_target = shoot_target[index]
        shoot_target[index] = -1
        counter += 1
        for i in range(len(shoot_target)):
            if shoot_target[i] == -1:
                continue
            if shoot_target[i] > current_target:
                shoot_target[i] -= current_target
            elif shoot_target[i] <= current_target:
                shoot_target[i] += current_target
shoot_target_to_rsting = [str(num) for num in shoot_target]
print(f"Shot targets: {counter} -> {' '.join(shoot_target_to_rsting)}")







