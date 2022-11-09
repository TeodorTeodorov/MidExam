numbers = [int(num) for num in input().split("@")]
jump_bul = False
house_count = 0
jump_count = 0
failed = 0
position = 0
jump_move = 0
while True:
    jump_number = input()
    if jump_number == "Love!":
        break
    else:
        jump_bul = True
        jump, number = jump_number.split(' ')
        number = int(number)
        jump_move += number
        if jump_move not in range(len(numbers) + 1):
            jump_move = 0

        if number == jump_move:
            place = number
            if numbers[number] == 0:
                print(f"Place {place} already had Valentine's day.")

            else:
                numbers[number] -= 2

                if numbers[number] == 0:
                    house_count += 1
                    print(f"Place {place} has Valentine's day.")


        if sum(numbers) == 0:
            print("Mission was successful.")
house_without = len(numbers) - house_count
print(f"Cupid's last position was {place}.")
print(f"Cupid has failed {house_without} places.")

#         if jump_count:
#             if number - 1 not in range(len(numbers)):
#                 continue
#
#             for index in range(len(numbers)):
#                 if numbers[index] == 0:
#                     print(f"Place {jump_count} already had Valentine's day.")
#                 if index == number:
#                     numbers[index+1] -= 2
# print(numbers)
