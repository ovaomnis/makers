import datetime


class Smartphone:
    def call(self, number: str):
        return f'Calling {number}'

    def where_to_wear(self):
        return '“You can keep me anywhere'


class Watch:
    def see_time(self):
        return datetime.datetime.now().time()

    def where_to_wear(self):
        return "You should wear me on your hand"


class SmartWatch(Watch, Smartphone):
    pass


sw = SmartWatch()
print(sw.where_to_wear())
