from abc import ABC, abstractmethod
from typing import Sized
from exeptions import BadDataException


class Validator(ABC):
    __msg: str

    @abstractmethod
    def validate(self, obj: any):
        ...


class ValidatorBase:
    def __init__(self, msg: str = None):
        self.msg = msg

    @property
    def msg(self) -> str:
        return self.__msg

    @msg.setter
    def msg(self, value) -> None:
        if not isinstance(value, str):
            raise Exception("Massage for validator have to be string")
        self.__msg = value

    def raise_exception(self):
        raise BadDataException(self.msg)



class LengthValidator(ValidatorBase, Validator):
    def __init__(self, max_length: int, msg: str = None,  min_length: int = 0):
        super().__init__(
            msg=msg if msg else f'Length have to be between {min_length} and {max_length}',
        )
        self.max_length = max_length
        self.min_length = min_length

    def validate(self, obj):
        if self.min_length <= len(obj) <= self.max_length:
            return obj
        self.raise_exception()


class InstanceValidator(ValidatorBase, Validator):
    def __init__(self, instance: any, msg: str = None):
        super().__init__(
            msg=msg if msg else f'Instance must to be {instance} instance'
        )
        self.instance = instance

    def validate(self, obj: any):
        if isinstance(obj, self.instance):
            return obj
        self.raise_exception()


class IntegerValidator(ValidatorBase, Validator):
    def __init__(self):
        super().__init__(
            msg='Integer validation failed'
        )

    def validate(self, obj: any):
        if isinstance(obj, int) or obj.isdigit():
            return int(obj)
        self.raise_exception()


if __name__ == '__main__':
    name = LengthValidator(max_length=4)
    name.validate('Adil')
