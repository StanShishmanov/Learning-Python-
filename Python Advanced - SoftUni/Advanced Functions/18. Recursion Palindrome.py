def palindrome(text, index):
    index_end = len(text) - 1 - index
    if index == len(text) // 2:
        return f'{text} is a palindrome'
    if text[index] == text[index_end]:
        return palindrome(text, index + 1)
    else:
        return f'{text} is not a palindrome'