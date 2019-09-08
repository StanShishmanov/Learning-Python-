players = []

class Player:
    def __init__(self, name, count_of_games, score=[]):
        self.name = name
        self.score = score
        self.count_of_games = count_of_games

data = input()
while not data == "report":
    name = data.split(' -> ')[0]
    score = data.split(' -> ')[1:]
    digits = [i.split(', ') for i in score]
    flattened = [int(val) for sublist in digits for val in sublist]

    count_of_games = 0
    for i in flattened:
        count_of_games += 1
    score = sum(i for i in flattened)
    new_player = Player(name, count_of_games, score)
    players.append(new_player)

    data = input()

new_data = input()

while not new_data == "end":
    input_one = new_data.split()[0]
    input_two = new_data.split()[1]
    if input_one == "score" and input_two == "ascending":
        for i in sorted(players, key=lambda x: (x.score, x.name)):
            print(f'{i.name}: {i.score}')
    elif input_one == "score" and input_two == "descending":
        for i in sorted(players, key=lambda x: (-x.score, x.name)):
            print(f'{i.name}: {i.score}')


    elif input_one == "numberOfGames" and input_two == "descending":
        for i in sorted(players, key=lambda x: (-x.count_of_games, x.name)):
            print(f'{i.name}: {i.count_of_games}')

    else: # input_one == "numberOfGames" and input_two == "ascending":
        for i in sorted(players, key=lambda x: (x.count_of_games, x.name)):
            print(f'{i.name}: {i.count_of_games}')
    new_data = input()