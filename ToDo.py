
tasks = []

def show_menu():
    print("\nSimple To-Do List")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"'{task}' has been added to the list.")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks in the list.")
    else:
        print("\nTasks:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")

def remove_task():
    view_tasks()
    if len(tasks) > 0:
        task_num = int(input("\nEnter the task number to remove: "))
        if 0 < task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"'{removed_task}' has been removed from the list.")
        else:
            print("Invalid task number.")

while True:
    show_menu()
    choice = input("Choose an option: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Exiting the To-Do List application.")
        break
    else:
        print("Invalid choice. Please try again.")
