def calc_price(filename: str) -> int:
    with open(filename, 'r') as file:
        summa = 0
        for i in [i.split() for i in file.readlines()]:
            prod, count, price = i
            summa += (float(count)*float(price))
        return summa
    