clothes = [int(x) for x in input().split()]
rack_capacity = int(input())
total_racks = 1
current_sum = 0

while clothes:
    cloth = clothes.pop()
    if current_sum + cloth <= rack_capacity:
        current_sum += cloth
    else:
        total_racks += 1
        current_sum = cloth
print(total_racks)