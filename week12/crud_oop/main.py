from typing import List

from task import Task
from decorators import log_activity


class TaskList:
    _tasks = []

    @log_activity
    def create_task(self, title: str, description: str, status: bool = False) -> Task:
        task = Task(title, description, status)
        self._tasks.append(task)
        return task

    @log_activity
    def get_task(self, index: int) -> Task:
        return self._tasks[index]

    @log_activity
    def remove_task(self, index) -> Task:
        return self._tasks.pop(index)

    @log_activity
    def get_all_tasks(self) -> List[Task]:
        return self._tasks

    @log_activity
    def __len__(self) -> int:
        return len(self._tasks)


if __name__ == '__main__':
    tl = TaskList()
    tl.create_task(title='do home work 1', description='Do you home work you stupid guy')
    tl.create_task(title='do home work 2', description='Do you home work you stupid guy')
    tl.create_task(title='do home work 3', description='Do you home work you stupid guy')
    tl.create_task(title='do home work 4', description='Do you home work you stupid guy')
    print(tl.get_all_tasks())
    tl.remove_task(1)
    print(tl.get_all_tasks())

