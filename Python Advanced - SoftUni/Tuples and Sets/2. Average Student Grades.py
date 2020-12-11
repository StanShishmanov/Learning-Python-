def avg_num(numbers):
    return sum(numbers) / len(numbers)

def solve(student_grades_string):
    student_grades = {}

    for s_grades in student_grades_string:
        (name, grade_str) = s_grades.split(' ')
        grade = float(grade_str)

        if name not in student_grades:
            student_grades[name] = []
        student_grades[name].append(grade)

    for (name, grades) in student_grades.items():
        grades_str = ' '.join(f'{x:.2f}' for x in grades)
        avg_grade = avg_num(grades)
        print(f'{name} -> {grades_str} (avg: {round(avg_grade, 2):.2f})')

n = int(input())
student_grades = [input() for _ in range(n)]

solve(student_grades)