from typing import Dict, List, Union


class View:
    def __init__(self, data: Union[List[dict], dict]):
        if isinstance(data, dict):
            self.all_data = [data]
        else:
            self.all_data = data

    def list(self):
        for item in self.all_data:
            for k, v in item.items():
                print(k + ':', v)
            print()


if __name__ == '__main__':
    from database import ProductDatabase
    db = ProductDatabase()
    View(db.read_one(5)).list()
