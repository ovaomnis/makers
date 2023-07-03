with open('task5.txt', 'r') as file:
    nums = file.readlines()
    with open('task6.txt', 'w+') as file2:
        file2.write(f'{int(min(nums))}-{int(max(nums))}')