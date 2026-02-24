task = []

while True:
    commands = input("Enter a command (add, delete, list, quit): ").strip().lower()

    if commands == "add":
        add = input("Type something to add: ")
        task.append(add)
        print(f"'{add}' added.")
    elif commands == "delete":
        if not task:
            print("Task empty.")
        else:
            for i, val in enumerate(task):
                print(f"{i}: {val}")
            try:
                index = int(input("Enter the number of the task to delete: "))
                removed = task.pop(index)
                print(f"Removed: {removed}")
            except (ValueError, IndexError):
                print("Invalid numbers. Please try again.")
        task.pop()
    elif commands == "list":
        if not task:
            print("Task empty")
        else:
            for i, val in enumerate(task):
                print(f"{i + 1}. {val}")
    elif commands == "quit":
        break
    else:
        print(f"Invalid commands: {commands}")