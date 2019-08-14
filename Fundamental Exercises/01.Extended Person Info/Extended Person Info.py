name = input()
age = int(input())
town = input()
salary = float(input())
ageRange = ''
salaryRange = ''

if age < 18:
    ageRange = 'teen'
elif age < 70:
    ageRange = 'adult'
else:
    ageRange = 'elder'
if salary < 500:
    salaryRange = 'low'
elif salary < 2000:
    salaryRange = 'medium'
else:
    salaryRange = 'high'
print('Name: %s \nAge: %d \nTown: %s \nSalary: $%0.2f \nAge range: %s \nSalary range: %s' % (name, age, town, salary, ageRange, salaryRange))