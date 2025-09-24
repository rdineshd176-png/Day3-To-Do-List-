tasks =[]

while True:
    print("\n Welcome to To Do List")
    print("1.Add New Task")
    print("2.View Task")
    print("3.Delete Task")
    print("4.Exit")

    inp = input("Enter your choice (1-4): ")

    if inp == "1":
        task = input("Enter Your Task: ")
        tasks.append(task)
        print(task, "Added to your list")
    
    elif inp == "2":
        if len(tasks) == "0":
            print("No Task yet")
        else:
            i = 1 
            print("Your To Do List")
            for i , task in enumerate(tasks ,start=1):
                print(i, task)
                

    elif inp == "3":
        if len(tasks) == "0":
            print("No Task yet")
        else:
            for i, task in enumerate(tasks,start=1):
                print(i, task)
                

            try: 
                task_num = int(input("Which task You want to delete: "))
                if 1<= task_num <= len(tasks):
                    remove = tasks.pop(task_num -1)
                    print(remove,"is deleted is deleted from the list ")
                else:
                    print("❌ Invalid task number.")

            except ValueError:
                print("Please enter a valid Number ")

    elif inp == "4":
        print("Exiting Bye Bye")
        break
                    
                
            

