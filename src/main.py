from task_manager import TaskManager


def display_menu():
    print("\n==========================")
    print("      TASK MANAGER")
    print("==========================")
    print("1. Add a task")
    print("2. List tasks")
    print("3. Mark a task as completed")
    print("4. Delete a task")
    print("5. Exit")
    print("==========================")


def get_task_id():
    try:
        return int(input("Enter task ID: "))
    except ValueError:
        print("Please enter a valid number.")
        return None


def main():
    manager = TaskManager()

    while True:
        display_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ").strip()

            if title:
                manager.add_task(title)
            else:
                print("Task title cannot be empty.")

        elif choice == "2":
            manager.list_tasks()

        elif choice == "3":
            task_id = get_task_id()

            if task_id is not None:
                manager.complete_task(task_id)

        elif choice == "4":
            task_id = get_task_id()

            if task_id is not None:
                manager.delete_task(task_id)

        elif choice == "5":
            print("Thank you for using Task Manager!")
            break

        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()