from ClassesAndObjectsExercise.project1.task import Task

class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if not new_task in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"
            #return f"Task"
        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return f"Completed task {task.name}"
        return f"Could not find task with the name {task_name}"

        # if task_name in self.tasks:
        #     task_name.completed = True
        #     return f"Completed task {task_name.name}"
        # return f"Could not find task with the name {task_name}"

    def clean_section(self):
        amount_of_tasks = 0
        for task in self.tasks:
            if task.completed:
                self.tasks.remove(task)
                amount_of_tasks += 1

        return f"Cleared {amount_of_tasks} tasks."

    def view_section(self):
        message = f"Section {self.name}:\n"
        for task in self.tasks:
            message += f"{task.details()}\n"

        return message



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
section1 = Section("New section")
task1 = Task("Tst", "27.04.2020")
print(section1.add_task(task1))
print(section1.complete_task("Tst"))