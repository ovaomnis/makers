from typing import List, Callable


def get_full_number(func: Callable[[List[str]], List[str]]):
    def wrapper(*args, **kwargs):
        nums = func(*args, **kwargs)
        print('#'.join([f'+996 {num[1:4]} {num[4:]}' for num in nums]))
    return wrapper


@get_full_number
def sort_phone_nums(nums: List[str]) -> List[str]:
    return sorted(nums)


sort_phone_nums(['0777987456', '0555123456', '0770369852'])
