class Task:
    def __init__(self, title, status="ToDo"):
        self.title = title
        self.status = status

    def mark_completed(self):
        self.status = "Done"


class TaskPool:
    def __init__(self):
        self.tasks = []

    def populate(self):
        self.tasks = [
            Task("Add Login UI", "Done"),
            Task("Fix UI Bug", "Done"),
            Task("Write Tests", "Done"),
            Task("Update Login UI"),
            Task("Update Documentation"),
            Task("Deploy to Production"),
        ]

    def add_task(self, task):
        self.tasks.append(task)

    def get_open_tasks(self):
        return [task for task in self.tasks if task.status == "ToDo"]

    def get_done_tasks(self):
        return [task for task in self.tasks if task.status == "Done"]


if __name__ == "__main__":
    pool = TaskPool()
    pool.populate()

    print("ToDo Tasks:")
    for task in pool.get_open_tasks():
        print(task.title)

    print("")
    print("Done Tasks:")
    for task in pool.get_done_tasks():
        print(task.title)
