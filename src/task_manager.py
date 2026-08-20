from task import Task


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title):
        task = Task(self.next_id, title)
        self.tasks.append(task)
        self.next_id += 1

        print(f"Task added successfully: {title}")

    def list_tasks(self):
        if not self.tasks:
            print("\nNo tasks available.")
            return

        print("\n----- Task List -----")

        for task in self.tasks:
            print(task)

    def complete_task(self, task_id):
        task = self.find_task(task_id)

        if task is None:
            print("Task not found.")
            return

        if task.completed:
            print("Task is already completed.")
            return

        task.mark_completed()
        print("Task marked as completed.")

    def delete_task(self, task_id):
        task = self.find_task(task_id)

        if task is None:
            print("Task not found.")
            return

        self.tasks.remove(task)
        print("Task deleted successfully.")

    def find_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                return task

        return None