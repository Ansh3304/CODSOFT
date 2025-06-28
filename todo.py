
import json
import os

TASK_FILE = "tasks.json"

# Initialize tasks storage
def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Display all tasks
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks found!\n")
        return
    print("\n--- Your To-Do List ---")
    for idx, task in enumerate(tasks, start=1):
        status = "✔️ Done" if task["completed"] else "⏳ Pending"
        print(f"{idx}. {task['title']} - {status}")

# Add new task
def add_task(tasks):
    title = input("Enter task title: ")
    tasks.append({"title": title, "completed": False})
    save_tasks(tasks)
    print("Task added successfully!")

# Mark task as completed
def complete_task(tasks):
    view_tasks(tasks)
    try:
        idx = int(input("Enter task number to mark as completed: "))
        if 1 <= idx <= len(tasks):
            tasks[idx - 1]["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        idx = int(input("Enter task number to delete: "))
        if 1 <= idx <= len(tasks):
            removed = tasks.pop(idx - 1)
            save_tasks(tasks)
            print(f"Task '{removed['title']}' deleted!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main menu
def main():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
    