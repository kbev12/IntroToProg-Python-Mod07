# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Working with pickling data and utilizing try/except
# ChangeLog (Who,When,What):
# KBeverly,8.23.2022,Created script
# KBeverly,8.24.2022,Added try/except functionality
# ---------------------------------------------------------------------------- #


import pickle

# Declare variables and constants
task = str(input("Enter a task: "))
priority = int(input("Enter a priority: "))
to_do = [task, priority]


def storeData():
    # Use binary mode
    obj_file = open('todo.txt', 'ab')
    # source, destination
    pickle.dump(to_do, obj_file)
    obj_file.close()


def printData():
    # read the data back with the pickle.load method
    obj_file = open('todo.txt', 'rb')
    try:
        while True:
            obj_file_data = pickle.load(obj_file)
            print(obj_file_data)
    except EOFError:
        print('End of File')
    obj_file.close()


def endProgram():
    #End program
    input('(Press Enter to End Program)')


storeData()
printData()
endProgram()
