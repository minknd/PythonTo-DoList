#Import fastapi, sqlite, Task class
from fastapi import FastAPI
import sqlite3
from Task import Task


#Maps 0,1,2 from db to To-Do, In Progress, Done
progressMap = {
    0 : "To-Do",
    1 : "In Progress",
    2 : "Done"
}

#function to query database and map progress
def readAll():
    #connect to db through filepath 
    connection = sqlite3.connect("PythonTo-DoList\Data\Task.db")

    #cursor that executes db commands
    cursor = connection.cursor()

    #Read all query
    sql = "SELECT * FROM Task"
    row = cursor.execute(sql)
    #temp placeholder, will need to set all tasks found from db to task objects in python (This is just fetching all items and printing to test)
    print(cursor.fetchall())

    #Close cursor and connection
    cursor.close()
    connection.close()

readAll()

#set up endpoint for getting all tasks