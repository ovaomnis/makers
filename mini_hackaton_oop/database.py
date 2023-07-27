import json
import time
from typing import TextIO, Dict
from models import ProductModel, BaseModel


class DbFile:
    file_name = ''
    file: TextIO

    def init_file(self):
        self.file = open(self.file_name, 'a+')
        self.file.seek(0)
        if not self.file.read():
            print('wroked')
            self.write_file({
                'serial_id': 0,
                'data': []
            })
        print(self.file.read())

    def write_file(self, data):
        self.file.seek(0)
        self.file.truncate()
        self.file.write(json.dumps(data, indent=2))


class DbBase(DbFile):
    _data = {}
    model = BaseModel()

    @property
    def data(self) -> Dict:
        self.file.seek(0)
        self._data = json.load(self.file)
        return self._data

    @staticmethod
    def get_item(data, id_):
        for i in data:
            if i['id'] == id_:
                return i
        return None


class CreateMixin(DbBase):
    def create(self, **kwargs) -> Dict:
        self.model.data = kwargs
        self.model.is_valid()
        data = self.data
        data['serial_id'] += 1
        self.model.data.update({'id': data['serial_id']})
        data['data'].append(self.model.data)
        self.write_file(data)
        print('created', self.model.data)
        return self.model.data


class DeleteMixin(DbBase):
    def delete(self, id_: int):
        data = self.data
        item = self.get_item(data['data'], id_)
        if item:
            data['data'].remove(item)
            self.write_file(data)
            return item
        return None


class UpdateMixin(DbBase):
    def update(self, id_: int, new_data):
        data = self.data
        item = self.get_item(data['data'], id_)

        if not item:
            return None

        data['data'].remove(item)

        for field in self.model.fields:
            item[field] = new_data.get(field, item[field])

        self.model.data = item
        self.model.is_valid()

        data['data'].append(item)
        self.write_file(data)

        return item


class ReadMixin(DbBase):
    def read_one(self, id_):
        return self.get_item(self.read_all(), id_)

    def read_all(self, sort_by: str = 'id', reverse: bool = False):
        if sort_by not in ['id', *self.model.fields]:
            raise Exception(f'There is no field {sort_by} in {self.model.fields}')
        return sorted(self.data['data'], key=lambda x: x[sort_by], reverse=reverse)


class ProductDatabase(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin, DbBase):
    file_name = 'products.json'
    model = ProductModel()

    def __init__(self):
        self.init_file()

    def close(self):
        self.file.close()


if __name__ == '__main__':
    db = ProductDatabase()
    db.create(
        title="Xioami Mi 8",
        body='Some body',
        price='800',
        amount='999'
    )
    db.close()
    # print(db.read_all())
