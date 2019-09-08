gladiators = []
class Gladiator:
    def __init__(self, name, total_skill, technique, skill, skill_set={}):
        self.name = str(name)
        self.total_skill = int(total_skill)
        self.technique = str(technique)
        self.skill = int(skill)

        self.skill_set = skill_set

    def __str__(self):
        return f'{self.name}: {self.total_skill} skill'


def duel(glad_1, glad_2):
    gladiator_1_name = glad_1
    gladiator_2_name = glad_2
    for i in gladiators:
        if gladiator_1_name == i.name:
            gladiator_1_total = i.total_skill
        elif gladiator_2_name == i.name:
            gladiator_2_total = i.total_skill

    if gladiator_1_total > gladiator_2_total:
        loser = gladiator_2_name
    else:
        loser = gladiator_1_name
    for i in gladiators:
        if i.name == loser:
            gladiators.remove(i)


data = input()
while not data == "Ave Cesar":
    if " -> " in data:
        gladiator_name = data.split(" -> ")[0]
        gladiator_technique = data.split(" -> ")[1]
        gladiator_skill = int(data.split(" -> ")[2])
        gladiator_exists = False

        for i in gladiators:
            if gladiator_name == i.name:
                gladiator_exists = True
                if gladiator_technique in i.skill_set.keys():
                    if i.skill_set[gladiator_technique] < gladiator_skill:
                        previous_skill = i.skill_set[gladiator_technique]
                        result = abs(previous_skill - gladiator_skill)
                        i.total_skill += result
                        i.skill_set[gladiator_technique] = gladiator_skill
                else:
                    new_skill = {}
                    new_skill[gladiator_technique] = gladiator_skill
                    i.skill_set.update(new_skill)
                value_total_skill = 0
                for k, v in i.skill_set.items():
                    value_total_skill += v
                i.total_skill = value_total_skill
        if not gladiator_exists:
            new_gladiator = Gladiator(gladiator_name, gladiator_skill, gladiator_technique, gladiator_skill, {gladiator_technique: gladiator_skill})
            gladiators.append(new_gladiator)
    else:
        gladiator_1 = data.split(" vs ")[0]
        gladiator_2 = data.split(" vs ")[1]
        glad_1_exists = False
        glad_2_exists = False

        glad_1_skills = []
        glad_2_skills = []

        for i in gladiators:
            if i.name == gladiator_1:
                glad_1_exists = True
                for k, v in i.skill_set.items():
                    glad_1_skills.append(k)
            elif i.name == gladiator_2:
                glad_2_exists = True
                for k, v in i.skill_set.items():
                    glad_2_skills.append(k)

        if glad_1_exists and glad_2_exists:
            skill_result = any(elem in glad_1_skills for elem in glad_2_skills)
            if skill_result:
                duel(gladiator_1, gladiator_2)
    data = input()
for i in sorted(gladiators, key=lambda x: (-x.total_skill, x.name)):
    print(i)
    for k, v in sorted(i.skill_set.items(), key=lambda x: (-x[1], x[0])):
        print(f'- {k} <!> {v}')