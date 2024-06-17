# todo.py

class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        self.tasks[len(self.tasks) + 1] = {'task': task, 'completed': False}

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("To-Do List:")
            for task_id, task_info in self.tasks.items():
                print(f"{task_id}: [{'' if task_info['completed'] else ' '}] {task_info['task']}")

    def mark_completed(self, task_id):
        if task_id in self.tasks:
            self.tasks[task_id]['completed'] = True
        else:
            print("Task ID not found.")

    def delete_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
            print(f"Task {task_id} deleted.")
        else:
            print("Task ID not found.")


def main():
    todo_list = ToDoList()
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task = input("Enter task to add: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task_id = int(input("Enter task ID to mark as completed: "))
            todo_list.mark_completed(task_id)
        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            todo_list.delete_task(task_id)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
