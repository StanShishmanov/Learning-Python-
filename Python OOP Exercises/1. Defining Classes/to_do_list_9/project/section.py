# from to_do_list_9.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = list()

    def add_task(self, new_task):
        for t in self.tasks:
            if t.name == new_task:
                return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        for t in self.tasks:
            if t.name == task_name:
                t.completed = True
                return f"Completed task {task_name}"
        return "Could not find task with the name {task_name}"

    def clean_section(self):
        removed_tasks = 0
        for t in self.tasks:
            if t.completed:
                removed_tasks += 1
                self.tasks.remove(t)
        return f"Cleared {removed_tasks} tasks."

    def view_section(self):
        line_one = f"Section {self.name}:\n"
        text = ""
        for t in self.tasks:
            text += t.details() + '\n'
        return line_one + text


# task = Task("Make bed", "27/05/2020")
# print(task.change_name("Go to University"))
# print(task.change_due_date("28.05.2020"))
# task.add_comment("Don't forget laptop")
# print(task.edit_comment(0, "Don't forget laptop and notebook"))
# print(task.details())
# section = Section("Daily tasks")
# print(section.add_task(task))
# second_task = Task("Make bed", "27/05/2020")
# section.add_task(second_task)
# print(section.clean_section())
# print(section.view_section())
