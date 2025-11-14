# To-Do List Application
# Uses list, add/remove/view, and stores tasks in a text file using open()

TASK_FILE = "tasks.txt"

# ---------------------------------------------------
# Load tasks from file into a list
# ---------------------------------------------------
def load_tasks():
    tasks = []
    try:
        f = open(TASK_FILE, "r")
        for line in f:
            tasks.append(line.strip())
        f.close()
    except FileNotFoundError:
        pass
    return tasks

# ---------------------------------------------------
# Save list of tasks into the file
# ---------------------------------------------------
def save_tasks(tasks):
    f = open(TASK_FILE, "w")
    for task in tasks:
        f.write(task + "\n")
    f.close()

# ---------------------------------------------------
# View tasks
# ---------------------------------------------------
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.\n")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print()

# ---------------------------------------------------
# Add task
# ---------------------------------------------------
def add_task(tasks):
    task = input("Enter new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added.")
    else:
        print("Cannot add empty task.")

# ---------------------------------------------------
# Remove task
# ---------------------------------------------------
def remove_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a number.")

# ---------------------------------------------------
# Main Menu
# ---------------------------------------------------
def main():
    tasks = load_tasks()

    while True:
        print("""
=== To-Do List Menu ===
1. View tasks
2. Add task
3. Remove task
4. Quit
""")

        choice = input("Choose an option: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Exiting... Tasks saved.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
