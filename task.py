tasks = []

def show_menu():
    print("\nTo-Do List Application")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Mark Task as Complete")
    print("5. Delete Task")
    print("6. Exit")

def view_tasks():
    if not tasks:
        print("\nNo tasks available.")
    else:
        for i, task in enumerate(tasks):
            status = "Complete" if task['completed'] else "Pending"
            print(f"{i + 1}. {task['title']} - {status}")

def add_task():
    title = input("Enter the task title: ")
    task = {"title": title, "completed": False}
    tasks.append(task)
    print(f"\nTask '{title}' added.")

def update_task():
    view_tasks()
    task_number = int(input("\nEnter the task number to update: ")) - 1
    if 0 <= task_number < len(tasks):
        new_title = input("Enter the new task title: ")
        tasks[task_number]['title'] = new_title
        print("\nTask updated successfully.")
    else:
        print("\nInvalid task number.")

def mark_task_complete():
    view_tasks()
    task_number = int(input("\nEnter the task number to mark as complete: ")) - 1
    if 0 <= task_number < len(tasks):
        tasks[task_number]['completed'] = True
        print("\nTask marked as complete.")
    else:
        print("\nInvalid task number.")

def delete_task():
    view_tasks()
    task_number = int(input("\nEnter the task number to delete: ")) - 1
    if 0 <= task_number < len(tasks):
        deleted_task = tasks.pop(task_number)
        print(f"\nTask '{deleted_task['title']}' deleted.")
    else:
        print("\nInvalid task number.")

def main():
    while True:
        show_menu()
        choice = input("\nEnter your choice: ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            update_task()
        elif choice == '4':
            mark_task_complete()
        elif choice == '5':
            delete_task()
        elif choice == '6':
            print("\nExiting the application.")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()