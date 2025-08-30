# To-Do List
tasks = []

while True:
    print('''    1. Add Tasks
    2. View Tasks
    3. Delete Tasks
    4. Exit ''')
    choice = input("Choose an option: ")

    if choice == '1':
       task = input("Enter Task: ")
       tasks.append(task)
       print("Task added")
    elif choice == '2':
       print("Your tasks: ")
       for i,t in enumerate(tasks, start=1):
          print(f"{i}. {t}")
    elif choice == '3':
       num = int(input("Enter task number to delet: "))
       if 0<num<=len(tasks):
          tasks.pop(num-1)
          print("Task deleted")
       else:
          print("Invalid Number")
    elif choice == '4':
       print("Goodbye")
       break
    else:
       print("Invalid choice, try again")