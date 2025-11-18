import json

tasks = []  

def add_task():
    
    description = input("Enter task description: ")
    due_date = input("Enter due date (optional): ")
    
    if due_date == "":
        due_date = "No date"

    while True:
        priority = input("Enter priority (High, Medium, Low): ").title()

        if priority in ["High", "Medium", "Low"]:
            break
        else:
            print("Invalid priority. Please enter High, Medium, or Low.")
    
    task = {
        "description": description,
        "due_date": due_date,
        "priority": priority
    }

    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    if not tasks:  # Check if task list is empty
        print("No tasks available.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['description']} - Due: {task['due_date']} - Priority: {task['priority']}")

def delete_task():
    view_tasks()  
    task_num = input("Enter task number to delete: ") 

    try:
        task_num = int(task_num) - 1
    except ValueError:
        print("Please enter a valid number.")
        return
 
    if 0 <= task_num < len(tasks):
        confirm = input(f"Are you sure you want to delete task {task_num + 1}? (y/n): ").lower()
        if confirm == 'y': 
            tasks.pop(task_num)   
            print("Task deleted successfully.")
    else:
        print("Invalid task number.")

def edit_task():
    view_tasks()  

    
    try:
        task_num = int(input("Enter the task number you want to edit: ")) - 1
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    
    if 0 <= task_num < len(tasks):
        print("What would you like to edit?")
        print("1. Description")
        print("2. Due Date")
        print("3. Priority")

        choice = input("Enter choice (1-3): ")

        if choice == "1":
            tasks[task_num]["description"] = input("Enter new description: ")

        elif choice == "2":
            tasks[task_num]["due_date"] = input("Enter new due date (YYYY-MM-DD): ")

        elif choice == "3":
            new_priority = input("Enter new priority (High/Medium/Low): ").title()
            if new_priority not in ["High", "Medium", "Low"]:
                print("Invalid priority.")
                return
            tasks[task_num]["priority"] = new_priority

        else:
            print("Invalid choice.")
            return

        print("Task updated successfully.")
    else:
        print("Invalid task number.")

def save_tasks():
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file) 
    print("Tasks saved to file.")

def load_tasks():
    global tasks
    try:
        with open('tasks.txt', 'r') as file:
            tasks = json.load(file)  
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []  

def menu():
    load_tasks()  # Load tasks at the beginning
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Save and Exit")
 
        choice = input("Choose an option: ")
 
        if choice == '1':
            add_task()  
        elif choice == '2':
            view_tasks()  
        elif choice == '3':
            edit_task()  
        elif choice == '4':
            delete_task()  
        elif choice == '5':
            save_tasks()  
            print("Tasks saved successfully. Goodbye!")
            break  
        else:
            print("Invalid option. Please try again.")


menu()