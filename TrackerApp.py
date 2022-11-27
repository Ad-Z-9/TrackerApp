# from tkinter import *
# from tkinter import ttk
# root = Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

# Future additions - button to reset a task and show how many times it was done
from pymongo import MongoClient
import datetime

client = MongoClient('localhost', 27017)
db = client.taskDatabase

posts = db.posts

class dataManagement:
    def addData(taskTitle, taskDescription):
        print("Adding Data to DB")
        post = {
            "Task Title": taskTitle,
            "Task Discription" : taskDescription
        }
        post_id = posts.insert_one(post).inserted_id
        post_id
    def getData():
        print("Getting Data from DB")
    def deleteData():
        print("Deleting Data from DB")
    def refreshData(): 
        print("Refressing Data from DB")


tasks = dataManagement 
tasks.addData("Test title1","test discription1")