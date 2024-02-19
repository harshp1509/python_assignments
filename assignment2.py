def display():
    print("Enter the number accoding to your task")
    print("1:- Add Task")
    print("2:- View Tasks")
    print("3:- Mark As Done")
    print("4:- Remove the task")
    print("5:- Exit")

def add_task(tasks):
    task_name=input("Enter task name:--")
    priority=input("enter priority (High/Medium/Low): ").capitalize()
    task={'task_name':task_name,"priority":priority,'completed':False}
    tasks.append(task)
    print("Task added successfully!")

def view_task(tasks):
    print("\n To do List:  \n")
    for i,task in enumerate(tasks):
        status="completed" if task['completed'] else "Not Completed"
        print(f" {i}.  {task['task_name']} --priority: {task['priority']},Status:{status} ")

def remove_task(tasks):
    view_task(tasks)
    index=int(input("enter task index which you want to remove:---"))

    if(0<=index<len(tasks)):
        r_task=tasks.pop(index)
        print(f"Task '{r_task['task_name']}'  is removed.")
    else:
        print("Invalid task index.")

def mark_task_done(tasks):
    view_task(tasks)
    t_index=int(input("enter the index of the task to mark as completed:--"))

    if(0<=t_index<len(tasks)):
        tasks[t_index]['completed']=True
        print("Task marked as completed!")
    else:
        print("Invalid index")





tasks=[]

while True:
    display()

    choice=input("enter your choice:--")

    if choice=='1':
        add_task(tasks)
    elif(choice=='2'):
        view_task(tasks)
    elif(choice=='3'):
        mark_task_done(tasks)
    elif(choice=='4'):
        remove_task(tasks)
    elif(choice=='5'):
        print("exiting.")
        break
    else:
        print("Invalid choice. Please select a valid option")





