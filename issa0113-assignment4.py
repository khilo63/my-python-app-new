import os

tasks = []

def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def display_menu():
    print("\nTo-Do List App")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def view_tasks():
    if not tasks:
        print("\nNo tasks to display.")
    else:
        print("\nTasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added!")

def remove_task():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to remove: "))
        removed_task = tasks.pop(task_num - 1)
        print(f"Task '{removed_task}' removed!")
    except (ValueError, IndexError):
        print("Invalid task number.")

def main():
    load_tasks()
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            save_tasks()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()