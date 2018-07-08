# Program for Todo App
import sqlite3
import sys

# Program for connection of database
connection = sqlite3.connect('sqlite3_todo.db')
cursor = connection.cursor()

# Creating a table for tasks
# cursor.execute('CREATE TABLE tasks ( id INTEGER PRIMARY KEY, task TEXT)')

class Todo():
    def start(self):
        print('Welcome To ToDo App')
    def choice(self):
        press = 0
        while(press !=5):
            press=input('\n 1. To add Task\n 2. To view Tasks\n 3. To edit Tasks\n 4. To delete Tasks\n 5. To exit\n')
            if press == 1:
                task = raw_input('Enter Task\n')
                cursor.execute('INSERT INTO tasks(task) VALUES(?)', (task, ))
                connection.commit()
                raw_input("Press Enter to continue...")
            elif press == 2:
                print('List of Task To Do are:')
                cursor.execute('SELECT * FROM tasks')
                row = cursor.fetchone()
                while row is not None:
                    id = row[0]
                    task = row[1]
                    print(str(id)+'. ' + str(task))
                    row = cursor.fetchone()
                raw_input("Press Enter to continue...")
            elif press == 3:
                print('Enter id to edit Task')
                cursor.execute('SELECT * FROM tasks')
                row = cursor.fetchone()
                while row is not None:
                    id = row[0]
                    task = row[1]
                    print(str(id)+'. ' + str(task))
                    row = cursor.fetchone()
                number = raw_input('\n')
                data = raw_input('\n Edit Task\n')
                query = "UPDATE tasks SET task ="+"'"+data+"'"+" WHERE id = "+number
                cursor.execute(query)
                raw_input("Press Enter to continue...")
            elif press == 4:
                print('Enter id to delete Task')
                cursor.execute('SELECT * FROM tasks')
                row = cursor.fetchone()
                while row is not None:
                    id = row[0]
                    task = row[1]
                    print(str(id)+'. '+ str(task))
                    row = cursor.fetchone()
                number = raw_input('\n')
                query = "DELETE FROM tasks WHERE id = "+number
                cursor.execute(query)
                raw_input("Press Enter to continue...")
            elif press == 5:
                print('Thanks :)')
                sys.exit()
            else:
                return
    
        
        

t = Todo()
t.start()
t.choice()

