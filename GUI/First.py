# Python gui

# import
from tkinter import *


def validatae_login(uname="", pwd=""):
    if not uname or len(uname) < 5:
        return False
    if not pwd or len(pwd) < 5:
        return False

    if uname == "nehal" and pwd == "nehal":
        return True

    return False


def login(event):
    uname = username.get()
    paswd = password.get()
    print("User login attempt")
    print("username : %s " % uname)
    print("Password : %s " % paswd)

    if uname or len(uname) < 5:
        username.config(bg="red")
    if(paswd or len(paswd) < 5):
        password.config(bg="red")
    if validatae_login(uname, paswd):
        print("Welcome Valid User")
    else:
        username.config(bg="red")
        password.config(bg="red")
        print("User name or password don't meet the requirement")
        reset(event)



def reset(event):
    print("Reset the controller")
    username.delete(0, E)
    username.config(bg="white")
    password.delete(0, E)
    password.config(bg="white")
    username.insert(0, "USERNAME")
    password.insert(0, "PASSWORD")

def enter_uname(event):
    uname = username.get()
    if uname == "USERNAME":
        username.delete(0, E)

def leave_uname(event):
    uname = username.get()
    if uname == "":
        username.insert(0, "USERNAME")

def enter_password(event):
    paswd = password.get()
    if paswd == "PASSWORD":
        password.delete(0, E)

def leave_password(event):
    paswd = password.get()
    if paswd == "":
        password.insert(0, "PASSWORD")

# create root
root = Tk()
root.title("Employee Database System")
root.geometry('350x250')

fram = Frame(root, width=200, height=200)
fram.pack()

lable1 = Label(fram, text="User Name", font=("calibri", 14))
lable1.grid(row=0, column=0)

lable2 = Label(fram, text="Password", font=("calibri", 14))
lable2.grid(row=1, column=0)

username = Entry(fram )
username.focus()
username.insert(0, "USERNAME")
username.grid(row=0, column=1)
username.bind('<Enter>', enter_uname)
username.bind('<Leave>', leave_uname)

password = Entry(fram,)
password.insert(0, "PASSWORD")
password.grid(row=1, column=1,)
password.bind('<Enter>', enter_password)
password.bind('<Leave>', leave_password)


submitButton = Button(fram, text="Login", bg="green", fg="black")
submitButton.grid(row=2, column=0)
submitButton.bind('<Button-1>', login)


resetButton = Button(fram, text="Reset", bg="red", fg="black")
resetButton.grid(row=2, column=1)
resetButton.bind('<Button-1>', reset)

root.mainloop()