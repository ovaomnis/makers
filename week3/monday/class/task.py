employees = {
    'id1': {
        'first name': 'Александр',
        'last name' : 'Иванов',
        'age': 30,
        'job':'программист'
            },
    'id2': {
        'first name': 'Ольга',
        'last name' : 'Петрова',
        'age': 35,
        'job':'ML-engineer'
            }
}

dct = {key: {k: float(v) 
             if type(v) == int 
             else v 
             for k, v in value.items()} 
       for key, value in employees.items()}
print(dct)``