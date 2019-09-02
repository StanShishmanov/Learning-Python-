data = input()
exercises = []
class Exercise:
    def __init__(self, topic, course_name, judge_contest_link, prob_list):
        self.topic = topic
        self.course_name = course_name
        self.judge_contest_link = judge_contest_link
        self.prob_list = prob_list
while not data == "go go go":
    prob_list = []
    topic = data.split(' -> ')[0]
    course_name = data.split(' -> ')[1]
    judge_contest_link = data.split(' -> ')[2]
    problems = data.split(' -> ')[3]
    for i in problems.split(', '):
        prob_list.append(i)
    exercise = Exercise(topic, course_name, judge_contest_link, prob_list)
    exercises.append(exercise)

    data = input()
for ex in exercises:
    topic = ex.topic
    course_name = ex.course_name
    judge_contest_link = ex.judge_contest_link
    problems = ex.prob_list

    print(f'Exercises: {topic}')
    print(f'Problems for exercises and homework for the "{course_name}" course @ SoftUni.')
    print(f'Check your solutions here: {judge_contest_link}')
    counter = 1
    for i in problems:
        print(f'{counter}. {i}')
        counter += 1
#ObjectsAndSimpleClasses -> ProgrammingFundamentalsExtended -> https://judge.softuni.bg/Contests/439 -> Exercises, OptimizedBankingSystem, Animals, Websites, Boxes, BoxIntersection, Messages
