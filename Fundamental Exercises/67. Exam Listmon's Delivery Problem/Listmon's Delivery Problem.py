from math import pi
width = float(input())
depth = float(input())
height = float(input())
num_barrels = int(input())
total_truck_volume = width * depth * height
total_barrels_loaded = 0
next_barrel_vol = 0

while total_barrels_loaded <= num_barrels - 1:

    barrel_radius = float(input())
    barrel_height = float(input())
    barrel_vol = pi * barrel_radius * barrel_radius * barrel_height
    total_truck_volume -= barrel_vol
    if total_truck_volume < 0:
        print(f"Truck is full. {total_barrels_loaded} on board!")
        break
    else:
        total_barrels_loaded += 1

if total_barrels_loaded == num_barrels:
    print(f'All barrels on board. Capacity left - {total_truck_volume:.2f}.')


""""
100
100
50
2
20
40
30
60

300
150
200
6
100
100
100
100
100
100
100
100
100
100
100
100
"""

