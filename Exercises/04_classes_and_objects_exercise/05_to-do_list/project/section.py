from task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: str):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"
        else:
            return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str):
        for name in self.tasks:
            if name.name == task_name:
                name.completed = True
                return f"Completed task {name.name}"
        else:
            return f"Could not find task with the name {task_name}"

    def clean_section(self):
        removed = [self.tasks.remove(task) for task in self.tasks if task.completed is True]
        return f"Cleared {len(removed)} tasks."

    def view_section(self):
        return f"Section {self.name}:\n" + '\n'.join([t.details() for t in self.tasks])


