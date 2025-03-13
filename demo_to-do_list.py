import time # Slow down terminal
import os # Need to clear screen

list = [] # For holding to-dos'
# Save for Users
def save_task():
    with open("task.txt", 'w') as file:
        for lists in list:
            file.write(lists + '\n')
            
def load_task():
    global list  # Use the same tasks list
    try:
        with open("tasks.txt", "r") as file:  # Open file in read mode
            list = [line.strip() for line in file.readlines()]  # Read and clean lines
    except FileNotFoundError:
        list = []  # If the file doesn't exist, start with an empty list

def add_task():
    x = input("Add New Task: ")
    list.append(x)
    save_task()
    
def remove_task():
    for lists in list:
        print(lists)
    x = input("Which Task to Remove: ")
    if x in list:
        list.remove(x)
        save_task()

def edit_task():
    for lists in list:
        print(lists)
    x = str(input("Which Task to Edit: "))
    if x in list:
        list.remove(x)
        y = input("New Task: ")
        list.append(y)
        save_task()

# Main app
load_task()
while True:
    os.system('cls')
    print("--Welcome to The List!--")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Edit Tasks")
    print("4. Remove Tasks")
    print("5. Exit")

    choices = int(input("Choice: "))
    if choices == str:
        print("Invalid Entry")
    else:
        while choices != 6:
            if choices == 1:
                os.system('cls')
                add_task()
                time.sleep(2)
                break
            elif choices == 2:
                os.system('cls')
                for lists in list:
                    print(lists)
                time.sleep(4)
                break
            elif choices == 3:
                os.system('cls')
                edit_task()
                time.sleep(2)
                break
            elif choices == 4:
                os.system('cls')
                remove_task()
                time.sleep(2)
                break
            elif choices == 5:
                print("Goodbye")
                time.sleep(2)
                quit()