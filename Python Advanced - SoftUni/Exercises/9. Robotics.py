import datetime
from collections import deque

active_robots = deque(input().split(';'))
busy_robots = {}
start_time = input()
hours = int(start_time.split(":")[0])
minutes = int(start_time.split(":")[1])
seconds = int(start_time.split(":")[2])
start_time = datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds)
products = deque()

product = input()

while product != 'End':
    products.append(product)
    product = input()

while products:
    start_time = start_time + datetime.timedelta(seconds=1)
    product = products.popleft()

    if busy_robots:
        for bot in busy_robots:
            busy_robots[bot] -= 1
            if busy_robots[bot] == 0:
                active_robots.append(bot)
    busy_robots = {key: value for key, value in busy_robots.items() if value != 0}

    if active_robots:
        robot = active_robots.popleft()
        robot_name = robot.split('-')[0]
        robot_process = int(robot.split('-')[1])
        print(f"{robot_name} - {product} - [{start_time}]")
        busy_robots[robot] = robot_process
    else:
        products.append(product)