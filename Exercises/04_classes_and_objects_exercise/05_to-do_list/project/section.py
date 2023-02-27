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


task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())
section.complete_task("Make bed")
print(section.clean_section())
print(section.view_section())