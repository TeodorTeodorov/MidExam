energy = int(input())
win = 0
have_energy = True
while True:
    distance = input()
    if distance == "End of battle":
        break
    distance = int(distance)
    if energy > 0:
        energy -= distance
        win += 1
        if win % 3 == 0:
            energy += win
    else:
        have_energy = False
        print(f"Not enough energy! Game ends with {win} won battles and {energy} energy")

        break


if have_energy:

    print(f"Won battles: {win}. Energy left: {energy}")
