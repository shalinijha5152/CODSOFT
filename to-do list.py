#To-Do List
# Create an empty list to store tasks
tasks = []

# Function to add a task
def add_task(task):
    tasks.append(task)
    print("Task added: " + task)

# Function to list all tasks
def list_tasks():
    if not tasks:
        print("No task in the To-Do List.")
    else:
        print("To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

# Function to mark a task as done
def mark_done(task_index):
    if 1 <= task_index <= len(tasks):
        print("Task marked as done: " + tasks[task_index - 1])
        del tasks[task_index - 1]
    else:
        print("Invalid task number. Please enter a valid task number.")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. List tasks")
    print("3. Mark a task as done")
    print("4. Quit")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        list_tasks()
        task_index = int(input("Enter the number of the task to mark as done: "))
        mark_done(task_index)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")