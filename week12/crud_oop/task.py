from decorators import log_activity


class Task:
    _title: str
    _description: str
    _status: bool

    def __init__(self, title: str, description: str, status: bool = False):
        self._title = title
        self._description = description
        self._status = status

    @log_activity
    def mark_as_done(self):
        self._status = True

    @log_activity
    def mark_as_undone(self):
        self._status = False

    @log_activity
    def edit_description(self, description: str):
        if isinstance(description, str):
            self._description = description
        else:
            raise Exception('description must be str')

    @property
    def title(self):
        return self._title

    @property
    def description(self):
        return self._description

    @property
    def status(self):
        return self._status

    def __str__(self):
        return f'{self._title}: {self._status}'

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    t1 = Task('do homework', 'do ur hw u stupid guy')
    print(t1)
