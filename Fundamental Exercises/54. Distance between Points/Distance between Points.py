from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

first_point = list(map(float, input().split()))

first_point = Point(first_point[0], first_point[1])

second_point = list(map(float, input().split()))

second_point = Point(second_point[0], second_point[1])


def get_distance(f_point, s_point):
    side_a = s_point.x - f_point.x
    side_b = s_point.y - f_point.y
    return sqrt(side_a ** 2 + side_b ** 2)
distance = get_distance(first_point, second_point)
print(f'{distance:.3f}')