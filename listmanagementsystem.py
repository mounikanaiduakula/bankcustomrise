tasks = []  

while True:
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Mark Task as Done")
    print("5. Delete Task")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    # Add Task
    if choice == "1":
        if len(tasks) >= 8:
            print("Task limit reached (8 tasks maximum).")
        else:
            description = input("Enter task description: ").strip()
            if description == "":
                print("Task description cannot be empty.")
            else:
                task = {
                    "ID": len(tasks) + 1,
                    "Task": description,
                    "Status": "Pending"
                }
                tasks.append(task)
                print("Task added successfully.")

    #  View Tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\n--- Task List ---")
            for t in tasks:
                print(f"ID: {t['ID']} | Task: {t['Task']} | Status: {t['Status']}")
            print("-----------------")

            pending = 0
            done = 0
            for t in tasks:
                if t["Status"] == "Pending":
                    pending += 1
                if t["Status"] == "Done":
                    done += 1
            print(f"Pending: {pending} | Done: {done}")

    # Update Task
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to update.")
        else:
            task_id = input("Enter Task ID to update: ")
            if task_id.isdigit():
                task_id = int(task_id)
                index = -1
                for i in range(len(tasks)):
                    if tasks[i]["ID"] == task_id:
                        index = i
                        break
                if index != -1:
                    new_desc = input("Enter new task description: ").strip()
                    if new_desc == "":
                        print("Description cannot be empty.")
                    else:
                        tasks[index]["Task"] = new_desc
                        print("Task updated successfully.")
                else:
                    print("Task not found.")
            else:
                print("Invalid Task ID.")

    #  Mark Task as Done
    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks to mark as done.")
        else:
            task_id = input("Enter Task ID to mark as done: ")
            if task_id.isdigit():
                task_id = int(task_id)
                index = -1
                for i in range(len(tasks)):
                    if tasks[i]["ID"] == task_id:
                        index = i
                        break
                if index != -1:
                    tasks[index]["Status"] = "Done"
                    print("Task marked as done.")
                else:
                    print("Task not found.")
            else:
                print("Invalid Task ID.")

    # Delete Task
    elif choice == "5":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            task_id = input("Enter Task ID to delete: ")
            if task_id.isdigit():
                task_id = int(task_id)
                index = -1
                for i in range(len(tasks)):
                    if tasks[i]["ID"] == task_id:
                        index = i
                        break
                if index != -1:
                    del tasks[index]
                    print("Task deleted successfully.")

                    new_id = 1
                    for t in tasks:
                        t["ID"] = new_id
                        new_id += 1
                else:
                    print("Task not found.")
            else:
                print("Invalid Task ID.")

    # Exit
    elif choice == "6":
        print("Exiting To-Do List. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
