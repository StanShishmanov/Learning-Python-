import os
search_extension = input()
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith(search_extension):
            print(file)
