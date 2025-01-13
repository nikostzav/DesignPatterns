
class Task:
    def __init__(self, name):
        self.name = name
        self.is_completed = False

    def mark_as_completed(self):
        self.is_completed = True

    def __str__(self):
        status = "Completed" if self.is_completed else "Pending"
        return f"{self.name} - {status}"



class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_name):
        self.tasks = [task for task in self.tasks if task.name != task_name]

    def list_tasks(self):
        for task in self.tasks:
            print(task)



if __name__ == "__main__":
    
    task_manager = TaskManager()

  
    task1 = Task("Go to the gym")
    task2 = Task("Read a book")
    task3 = Task("Cook meal")

    task_manager.add_task(task1)
    task_manager.add_task(task2)
    task_manager.add_task(task3)
    task_manager.remove_task(task3)


    task1.mark_as_completed()
    task2.mark_as_completed()

   
    print("Tasks:")
    task_manager.list_tasks()
