import json
from datetime import datetime, timedelta

TASKS_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    description = input("Enter the task description: ")
    due_date = input("Enter the due date (YYYY-MM-DD) or leave empty: ")
    
    if not due_date:
        due_date = None
    else:
        try:
            due_date = datetime.strptime(due_date, '%Y-%m-%d').date()
        except ValueError:
            print("Invalid date format. Task not added.")
            return

    task = {
        "description": description,
        "due_date": str(due_date) if due_date else None,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{description}' added.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    print("\n--- Task List ---")
    for index, task in enumerate(tasks):
        status = "✔️ Completed" if task["completed"] else "❌ Pending"
        due_date = task["due_date"] if task["due_date"] else "No due date"
        print(f"{index + 1}. {task['description']} | Due: {due_date} | Status: {status}")

def filter_tasks(tasks, filter_type):
    if filter_type == "completed":
        return [task for task in tasks if task["completed"]]
    elif filter_type == "pending":
        return [task for task in tasks if not task["completed"]]
    elif filter_type == "due_soon":
        soon_tasks = []
        for task in tasks:
            if task["due_date"]:
                due_date = datetime.strptime(task["due_date"], '%Y-%m-%d').date()
                if 0 <= (due_date - datetime.today().date()).days <= 3:
                    soon_tasks.append(task)
        return soon_tasks
    else:
        return tasks

def mark_completed(tasks):
    view_tasks(tasks)
    task_number = int(input("Enter the task number to mark as completed: ")) - 1
    if 0 <= task_number < len(tasks):
        tasks[task_number]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

def edit_task(tasks):
    view_tasks(tasks)
    task_number = int(input("Enter the task number to edit: ")) - 1
    if 0 <= task_number < len(tasks):
        new_description = input("Enter new task description (leave empty to keep current): ")
        new_due_date = input("Enter new due date (YYYY-MM-DD) or leave empty to keep current: ")
        
        if new_description:
            tasks[task_number]["description"] = new_description
        if new_due_date:
            try:
                tasks[task_number]["due_date"] = str(datetime.strptime(new_due_date, '%Y-%m-%d').date())
            except ValueError:
                print("Invalid date format. Due date not updated.")

        save_tasks(tasks)
        print("Task updated.")
    else:
        print("Invalid task number.")

def delete_task(tasks):
    view_tasks(tasks)
    task_number = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_number < len(tasks):
        tasks.pop(task_number)
        save_tasks(tasks)
        print("Task deleted.")
    else:
        print("Invalid task number.")

def todo_list_manager():
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List Manager ---")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. View completed tasks")
        print("4. View pending tasks")
        print("5. View tasks due soon")
        print("6. Mark a task as completed")
        print("7. Edit a task")
        print("8. Delete a task")
        print("9. Exit")

        choice = input("Choose an option (1-9): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            view_tasks(filter_tasks(tasks, "completed"))
        elif choice == "4":
            view_tasks(filter_tasks(tasks, "pending"))
        elif choice == "5":
            view_tasks(filter_tasks(tasks, "due_soon"))
        elif choice == "6":
            mark_completed(tasks)
        elif choice == "7":
            edit_task(tasks)
        elif choice == "8":
            delete_task(tasks)
        elif choice == "9":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    todo_list_manager()
