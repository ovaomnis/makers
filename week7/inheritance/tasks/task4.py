class MyDict(dict):
    def get(self, key):
        if not super().get(key):
            return 'Are you kidding?'
        else:
            return super().get(key)


obj_dict = MyDict({'some_title': 2})
print(obj_dict.get('some'))
