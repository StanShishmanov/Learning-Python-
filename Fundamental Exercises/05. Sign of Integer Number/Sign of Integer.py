num = int(input())
def sign_printer():
    word = ''
    if num > 0:
        word = 'positive'
    elif num < 0:
        word = 'negative'
    else:
        word = 'zero'
    print(f'The number {num} is {word}.')


sign_printer()