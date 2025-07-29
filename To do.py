def load_tasks(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.strip().split(',') for line in file]
    #Divide into lists

def save_tasks(filename, tasks):
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(','.join(task) + '\n' for task in tasks)
    #Write the tasks in the tasks list to a file and each task takes up one line in the file

def view_tasks(tasks):
    for i, task in enumerate(sorted(tasks, key=lambda x: int(x[1])), 1):
    #enumerate: Get the index and contents of the task
        status = "finish" if len(task) > 2 and task[2] == "1" else "not finish"
    # cheak the task list is longer than 2 or not，
    # task[2]==1,the thrid element in the task list is equal to 1
        print(f"{i}. [{status}] priority_level: {task[1]} task_discription: {task[0]}")

def add_task(tasks):
    description = input("Enter task description: ")
    priority = input("Enter task priority_level: ")
    tasks.append([description, priority])
    print("Task added")

def complete_task(tasks):
    view_tasks(tasks)
    idx = int(input("Enter the number of the task to mark as completed: ")) - 1
    if 0 <= idx < len(tasks):
        tasks[idx].append("1")
        print("Task marked as completed")
    else:
        print("Not available")

def delete_task(tasks):
    view_tasks(tasks)
    idx = int(input("Enter the number of the task to delete: ")) - 1
    if 0 <= idx < len(tasks):
        tasks.pop(idx)
        print("Task deleted")
    else:
        print("Not available")

def main():
    filename = "tasks.txt"
    tasks = load_tasks(filename)

    while True:
        print("\n To do List Management System")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as completed")
        print("4. Delete task")
        print("5. Save and exit")

        choice = input("Choose an option: ")
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(filename, tasks)
            print("Task saved! Exiting the program")
            break
        else:
            print("Not available,Please try again")

if __name__ == "__main__":
    main()
#Determine whether this part is the main running part