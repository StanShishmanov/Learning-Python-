base1 = input()
height = input()

def triangle_area(base1, height):
    area = (float(base1) * float(height)) / 2
    print(f'{area:.12g}')

triangle_area(base1, height)