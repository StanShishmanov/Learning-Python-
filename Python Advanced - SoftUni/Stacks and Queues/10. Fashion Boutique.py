def solve():
    clothes = [int(num) for num in input().split()]
    rack_capacity = int(input())

    sum_clothes = 0
    total_racks_used = 1

    while clothes:
        
        sum_clothes += clothes[0]

        if sum_clothes <= rack_capacity:
            clothes.pop(0)
        else:
                total_racks_used += 1
                sum_clothes = 0

    print(total_racks_used)
solve()