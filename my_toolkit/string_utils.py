def count_words(word):
    new = word.strip()
    return len(new)

def is_palindrom(word):
    if word == word[::-1]:
        return f"YES the word is palindrome"
    else:
        return f"NOT a palindrome"
    