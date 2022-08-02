import json
from getpass import getpass
from tokenize import Ignore
import bcrypt
import os
from rich.markdown import Markdown
from rich.console import Console
from rich.table import Table
from rich.theme import Theme
import pandas as pd
import time 
import warnings
warnings.filterwarnings('ignore')

myTheme = Theme({
    "good":"green",
    "bad":"red",
    "warning":"yellow"
})

console = Console(theme=myTheme)

def login():
    d = json.load(open('./data/login/account.json'))
    username = input("Username :")
    password = getpass("Password :").encode("utf-8")
    while not (username==d["username"] and bcrypt.checkpw(password,d["password"].encode("utf-8"))):
        print("Wrong Credentials")
        username = input("Username :")
        # password = input("Password :")
        password = getpass("Password :").encode("utf-8")
    console.print(":white_check_mark:  You are logged in !!")

def clear():
    os.system('clear')

def get_selection():
    print()
    a = int(input("Select Your Option : "))
    print()
    return a

def main_menu():
    MARKDOWN = """
                    :arrow_forward:   Welcome Work Manager admin panel :
                    
                        :one:        To-Do List
                        :two:        Appointments
                        :three:        Notes
                        :four:        Projects 
                        :zero:        Exit
                """
    console.print(MARKDOWN)

def initiate():
    try:
        df = pd.read_parquet("data/projects/table.parquet")
    except:
        d = {
            "id" : [0],
            "Title" : ["Others"],
            "Description" : ["0.txt"],
            "Status" : ["Ongoing"],
            "Departement" : ["DS & BI"],
        }
        df = pd.DataFrame(d)
        df.to_parquet("data/projects/table.parquet")


def get_confirmation(action):
    MARKDOWN = """
                    To confirm """+action+""" choose Yes, else choose No
                        :one:        Yes
                        :two:        No
                """
    print(MARKDOWN)
    a = int(input("Enter you choice :"))
    if a == 1:
        return True
    else:
        return False