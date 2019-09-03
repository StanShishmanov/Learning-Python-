class Human:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        if not first_name[0].isupper():
            raise Exception("Expected upper case letter! Argument: firstName")
        elif len(first_name) <= 3:
            raise Exception('Expected length at least 4 symbols! Argument: firstName')
        self.__first_name = first_name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        if not last_name[0].isupper():
            raise Exception("Expected upper case letter! Argument: lastName")
        elif len(last_name) <= 2:
            raise Exception('Expected length at least 3 symbols! Argument: lastName')
        self.__last_name = last_name

    def __str__(self):
        return f"First Name: {self.first_name}\nLast Name: {self.last_name}"


class Worker(Human):
    def __init__(self, first_name, last_name, week_salary, work_hours_per_day):
        Human.__init__(self, first_name, last_name)
        self.week_salary = float(week_salary)
        self.work_hours_per_day = float(work_hours_per_day)

    @property
    def week_salary(self):
        return self.__week_salary

    @week_salary.setter
    def week_salary(self, week_salary):
        if int(week_salary) < 10:
            raise Exception('Expected value mismatch! Argument: weekSalary')
        self.__week_salary = week_salary

    @property
    def work_hours_per_day(self):
        return self.__work_hours_per_day

    @work_hours_per_day.setter
    def work_hours_per_day(self, work_hours_per_day):
        if 1 <= work_hours_per_day <= 12:
            self.__work_hours_per_day = work_hours_per_day
        else:
            raise Exception('Expected value mismatch! Argument: workHoursPerDay')
        
    def __str__(self):
        return f"First Name: {self.first_name}\nLast Name: {self.last_name}\nWeek Salary: {self.week_salary:.2f}\nHours per day: {self.work_hours_per_day:.2f}\nSalary per hour: {(self.week_salary / (5* self.work_hours_per_day)):.2f}"

class Student(Human):
    def __init__(self, first_name, last_name, faculty_number):
        Human.__init__(self, first_name, last_name)
        self.faculty_number = faculty_number

    @property
    def faculty_number(self):
        return self.__faculty_number

    @faculty_number.setter
    def faculty_number(self, faculty_number):
            if not all( i.isdigit() or i.isalpha() for i in faculty_number):
                raise Exception("Invalid faculty number!")
            elif not len(faculty_number) in range(5, 10):
                raise Exception("Invalid faculty number!")
            self.__faculty_number = faculty_number

    def __str__(self):
        return f"First Name: {self.first_name}\nLast Name: {self.last_name}\nFaculty number: {self.faculty_number}"

try:
    student_data = input().split()
    worker_data = input().split()

    student_f_name = student_data[0]
    student_l_name = student_data[1]
    f_number = student_data[2]

    worker_f_name = worker_data[0]
    worker_l_name = worker_data[1]
    worker_salary = worker_data[2]
    worker_hours = worker_data[3]

    student = Student(student_f_name, student_l_name, f_number)
    worker = Worker(worker_f_name, worker_l_name, worker_salary, worker_hours)
    print(student)
    print()
    print(worker)
except Exception as exe:
    print(exe)

""""
Ivan Ivanov 9234DDd1
Ivan Petrov 129.99 8.5

"""