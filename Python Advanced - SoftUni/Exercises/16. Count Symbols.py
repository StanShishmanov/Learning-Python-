text = sorted([x for x in input()])

char_keeper = set()
for i in text:
    if i not in char_keeper:
        print(f"{i}: " + str(text.count(i)) + " time/s")
        char_keeper.add(i)