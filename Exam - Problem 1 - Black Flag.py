days = int(input())
plunder_for_day = int(input())
expected_plunder = int(input())
total_plunder = 0
day_counter = 0

for day in range(days):

    day_counter += 1
    total_plunder += plunder_for_day

    if day_counter % 3 == 0:
        total_plunder += plunder_for_day / 2
    if day_counter % 5 == 0:
        total_plunder -= total_plunder * 0.3

if total_plunder >= expected_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    percentage = total_plunder / expected_plunder * 100
    print(f"Collected only {percentage:.2f}% of the plunder.")
