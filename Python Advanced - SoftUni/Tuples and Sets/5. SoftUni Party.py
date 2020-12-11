reservations = []
attending = []

party_started = False

while True:
    command = input()
    if command == 'END':
        break
    if command == 'PARTY':
        party_started = True
        continue
    if not party_started:
        reservations.append(command)
    else:
        attending.append(command)

diff = set(reservations) ^ set(attending)
result = sorted(diff)
print(len(result))
[print(x) for x in result if x[0].isdigit()]
[print(x) for x in result if not x[0].isdigit()]