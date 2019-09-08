import datetime

today = datetime.date(2018, 8, 26)
date = input().split('-')
year = int(date[0])
month = int(date[1])
day = int(date[2])
question_date = datetime.date(year, month, day)
if question_date < today:
    print('Passed')
elif question_date == today:
    print('Today date')
else:
    print(f'{(question_date - today).days + 1} days left')