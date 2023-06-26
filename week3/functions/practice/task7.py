def is_palindrome(string: str):
    for i in range(len(string) // 2):
        if string[i].lower() != string[len(string) - i - 1].lower():
            return False
    return True

print(is_palindrome('Mom'))