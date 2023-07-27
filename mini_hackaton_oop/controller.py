from typing import Callable

from database import ProductDatabase
from view import View


class Controller:
    def __init__(self):
        self.actions = {
            'read one': self.read_one,
            'read all': self.read_all,
            'create': self.create,
            'update': self.update,
            'delete': self.delete,
            'quit': self.quit
        }
        self.db = ProductDatabase()
        self.db.create(
            title="Xioami Mi 8",
            body='Some body',
            price='800',
            amount='999'
        )

    def start(self):
        print('')
        print(f'Please select action: ')
        for a in self.actions:
            print(a)

        action = input('Your choice: ').strip().lower()
        if action in self.actions.keys():
            self.actions[action]()
        else:
            self.start()

    def read_one(self):
        item = self.get_record_by_id()
        View(item).list()
        self.start()

    def read_all(self):
        View(self.db.read_all()).list()
        self.start()

    def create(self):
        print('')
        data = {}
        for field in self.db.model.fields:
            data.update({
                field: input(f'{field}: ').strip()
            })
        self.db.create(**data)
        self.start()

    def update(self):
        item = self.get_record_by_id()
        updated_data = {}
        for k, v in item.items():
            if k != 'id':
                field = input(f'{k} [{v}]: ')
                if field:
                    updated_data.update({k: field})
        res = self.db.update(item['id'], updated_data)
        if res:
            print('Successfully updated')
        else:
            print('Update took no effect')
        self.start()

    def delete(self):
        item = self.get_record_by_id()
        res = self.db.delete(item['id'])
        if res:
            print('Successfully deleted')
        else:
            print('Delete took no effect')
        self.start()

    def quit(self):
        self.db.close()
        quit()

    def get_record_by_id(self):
        print('')
        id_ = int(input('Please enter id of product: '))
        print()
        item = self.db.read_one(id_)
        if not item:
            print('There is not item such id')
            what_next = input('Do you want not continue reading one (yes/no): ').lower()
            if what_next in ['yes', 'no'] and what_next == 'yes':
                self.read_one()
            else:
                self.start()
        return item


if __name__ == '__main__':
    Controller().start()
