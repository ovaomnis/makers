def sort_names(func):
    def wrapper(*args, **kwargs):
        return [i[0] for i in sorted(func(*args, **kwargs), key=lambda x: x[1])]
    return wrapper


@sort_names
def prefix_name(persons: [()]):
    return [[f'{"Ms" if person[3] == "F" else "Mr"}. {person[0]} {person[1]}', person[2]]for person in persons]


print(prefix_name([('Leo', 'Nimoy', 40, 'M'),
      ('Carrie', 'Fisher', 35, 'F'),
      ('Harrison', 'Ford', 38, 'M')]))
