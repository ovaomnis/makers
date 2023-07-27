class CustomError(Exception):
    pass


capitals_error = CustomError('ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ')


def check_letters(word: str):
    if word.upper() == word:
        return f'ВСЕ ОТЛИЧНО! {word}'
    else:
        raise capitals_error


print(check_letters("HELLO"))
