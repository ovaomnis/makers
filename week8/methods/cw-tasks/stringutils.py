class StringUtils:
    @staticmethod
    def is_palindrome(word: str):
        return word.lower() == word.lower()[::-1]


print(StringUtils.is_palindrome('Mom'))
