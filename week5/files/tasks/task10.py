from typing import List, Dict

def read_csv(filename: str) -> Dict[str, List[str]]:
    data = {}
    with open(filename) as file:
        for line in file.readlines():
            el = line.replace('\n', '').split(',')
            data.update({
                el[0]: el[1:]
            })
    return data
