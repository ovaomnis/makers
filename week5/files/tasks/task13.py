def reverse_file_print(filename: str) -> None:
    with open(filename) as file:
        for i in file:
            print(i[::-1])
