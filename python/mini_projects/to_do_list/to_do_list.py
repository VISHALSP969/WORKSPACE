def print_header():
    print("\n" + "-" * 40)
    print("       SIMPLE TODO LIST (Console)")
    print("-" * 40)

# tasks will be a list of [description, done_flag]
tasks = []

while True:
    print_header()
    print("Menu:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Edit task")
    print("4. Mark complete / incomplete")
    print("5. Delete task")
    print("6. Clear all tasks")
    print("7. Quit")

    choice = input("Enter choice (1-7): ").strip()

    # ---------- Add task ----------
    if choice == "1":
        desc = input("Enter task description: ").strip()
        if desc == "":
            print("Task description cannot be empty.")
        else:
            tasks.append([desc, False])   # False means not done
            print(f"Added: {desc}")

    # ---------- View tasks ----------
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks yet. Add one (menu option 1).")
        else:
            print("\nYour Tasks:")
            # number tasks starting from 1 for user-friendly indices
            for i in range(len(tasks)):
                desc, done = tasks[i]
                status = "[x]" if done else "[ ]"
                print(f"{i+1}. {status} {desc}")

    # ---------- Edit task ----------
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to edit.")
        else:
            print("Which task number do you want to edit?")
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i][0]}")
            idx = input("Enter task number: ").strip()
            if idx.isdigit():
                idx = int(idx)
                if 1 <= idx <= len(tasks):
                    new_desc = input("Enter new description: ").strip()
                    if new_desc == "":
                        print("Description cannot be empty. Edit cancelled.")
                    else:
                        tasks[idx-1][0] = new_desc
                        print("Task updated.")
                else:
                    print("Invalid task number.")
            else:
                print("Please enter a valid number.")

    # ---------- Mark complete / incomplete ----------
    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks to mark.")
        else:
            print("Choose task to toggle complete/incomplete:")
            for i in range(len(tasks)):
                status = "Done" if tasks[i][1] else "Not done"
                print(f"{i+1}. [{status}] {tasks[i][0]}")
            idx = input("Enter task number: ").strip()
            if idx.isdigit():
                idx = int(idx)
                if 1 <= idx <= len(tasks):
                    tasks[idx-1][1] = not tasks[idx-1][1]  # toggle boolean
                    state = "completed" if tasks[idx-1][1] else "marked as not done"
                    print(f"Task {idx} {state}.")
                else:
                    print("Invalid task number.")
            else:
                print("Please enter a valid number.")

    # ---------- Delete task ----------
    elif choice == "5":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            print("Which task number do you want to delete?")
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i][0]}")
            idx = input("Enter task number: ").strip()
            if idx.isdigit():
                idx = int(idx)
                if 1 <= idx <= len(tasks):
                    removed = tasks.pop(idx-1)   # removes and returns element
                    print(f"Deleted: {removed[0]}")
                else:
                    print("Invalid task number.")
            else:
                print("Please enter a valid number.")

    # ---------- Clear all ----------
    elif choice == "6":
        confirm = input("Are you sure you want to clear all tasks? (y/n): ").strip().lower()
        if confirm == "y":
            tasks.clear()
            print("All tasks cleared.")
        else:
            print("Clear cancelled.")

    # ---------- Quit ----------
    elif choice == "7":
        print("Goodbye! Have a productive day.")
        break

    # ---------- Invalid menu choice ----------
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")