from tasker import Tasker 

def print_commands():
    print(
        '''
        WELCOME TO THE TASKER APP
        -------
        COMMANDS:
        -------
        add [DESCRIPTION]
        update [TASK_ID] [NEW_DESCRIPTION]
        delete [TASK_ID]
        mark-in-progress [TASK_ID]
        mark-done [TASK_ID]
        list
        list done
        list in-progress
        list todo
        exit'''
    )
print_commands()

def tryint(num):
    try:
        return int(num)
    except ValueError:
        return None

def sanitize_command(command):
    command = command.strip().split(' ')
    command = [x.strip() for x in command]

    if len(command) == 0:
        return None

    if command[0] == "add":
        if len(command) > 1:
            command = [command[0], ' '.join(command[1:])]
            return command
        
    elif command[0] == "update":
        if len(command) > 2:
            command[1] = tryint(command[1])
            if command[1] != None:
                command = [command[0], command[1], ' '.join(command[2:])]
                return command
        
    elif command[0] == "delete":
        if len(command) == 2:
            command[1] = tryint(command[1])
            if command[1] != None:
                return command
        
    elif command[0] == "mark-in-progress":
        if len(command) == 2:
            command[1] = tryint(command[1])
            if command[1] != None:
                return command
        
    elif command[0] == "mark-done":
        if len(command) == 2:
            command[1] = tryint(command[1])
            if command[1] != None:
                return command
    
    elif command[0] == "list":
        if len(command) == 1:
            return command 
        elif len(command) == 2:
            if command[1] in ["done", "todo", "in-progress"]:
                return command

    return None 

command = ""
tasker = Tasker()
tasker.load_tasks()

while command != "exit":
    command = input("> ")

    if command.strip() == 'exit':
        tasker.save_tasks()
        print('bye')
        exit()

    command = sanitize_command(command)
    if command == None:
        print_commands()
        continue
    
    if command[0] == "add":
        task = tasker.add_task(command[1])
        if task != None:
            print(f"Task added successfully (ID: {tasker.db['last_id']})")
        else:
            print("Error adding task")

    elif command[0] == "update":
        if tasker.update_task(command[1], command[2]):
            print("Task updated successfully")
        else:
            print("Error updating task")

    elif command[0] == "delete":
        if tasker.delete_task(command[1]):
            print("Task deleted successfully")
        else:
            print("Error deleting task")

    elif command[0] == "mark-in-progress":
        if tasker.mark_in_progress(command[1]):
            print("Task marked as in progress")
        else:
            print("Error marking task as in progress")

    elif command[0] == "mark-done":
        if tasker.mark_done(command[1]):
            print("Task marked as done")
        else:
            print("Error marking task as done")

    elif command[0] == "list":
        if len(command) == 1:
            tasker.list()
        elif len(command) == 2:
            tasker.list_by_status(command[1])
