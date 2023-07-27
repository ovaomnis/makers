from validators import LengthValidator, InstanceValidator, IntegerValidator
from typing import Dict
from exeptions import BadDataException


class BaseModel:
    fields = []
    _raw_data = {}
    _valid_data = {}

    def __init__(self, fields: Dict = None):
        """
        :param fields: {'field_name': (validators)}
        """
        if fields:
            for name, validators in fields.items():
                self.fields.append(name)
                self.__setattr__(name, validators)

    def is_valid(self):
        for field in self.fields:
            validating_data = self._raw_data.get(field)

            if not validating_data:
                raise BadDataException(f'There no data {field} in class {self.__class__.__name__}')

            try:
                self._valid_data.update({
                    field: self.__dict__.get(field).validate(validating_data)
                })
            except BadDataException as err:
                raise err

    @property
    def data(self):
        if self._valid_data:
            return self._valid_data
        return self._raw_data

    @data.setter
    def data(self, data):
        self._raw_data = data


class ProductModel(BaseModel):
    def __init__(self):
        super().__init__(fields={
            'title': LengthValidator(max_length=50),
            'body': InstanceValidator(str),
            'price': IntegerValidator(),
            'amount': IntegerValidator(),
        })


if __name__ == '__main__':
    product = ProductModel()
    product.data = {'title': 'Hello World', 'body': 'somebody', 'price': 123, 'amount': 93}
    product.is_valid()
    print(product.data)
