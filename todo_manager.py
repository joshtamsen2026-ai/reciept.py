#Start with a pre-populated list of 3 tasks 
starting_tasks = ["Buy groceries", "Call mom", "Finish homework"]
    
#Display the current to-do list (numbered, starting from 1)
display_tasks = starting_tasks.copy()

for i, task in enumerate(display_tasks, start=1):
    print(f"{i}. {task}")




#Let the user add a new task (append)


new_task = input("Enter a new task: ")
new_task = new_task.strip()  # Remove leading/trailing whitespace

display_tasks.append(new_task)
display_tasks.sort()  # Sort the list alphabetically

#Let the user remove a task by number (pop)
remove_index = int(input("Enter the number of the task to remove: ")) - 1
if 0 <= remove_index < len(display_tasks):
    display_tasks.pop(remove_index)
else:
    print("no task to remove.")

#Display the updated list after each operation
for i, task in enumerate(display_tasks, start=1):
    print(f"{i}. {task}")

#Show the total number of tasks remaining
print(f"Total tasks remaining: {len(display_tasks)}")

if len(display_tasks) < 0:
    print("All tasks have been completed!")
    
