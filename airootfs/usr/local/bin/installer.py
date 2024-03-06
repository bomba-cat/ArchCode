#Imports
import tkinter as ntk
from tkinter import ttk as tk
from ttkthemes import ThemedTk
import os as linux

#Variables
user = ""
passw = ""

#Create window class
installer = ThemedTk(theme="breeze")

#Print to terminal
linux.system("echo 'Starting the CLD installer'")

#Get user and password
def GetUserPass():
    global user, passw
    linux.system("echo Getting user and password")
    for widget in installer.winfo_children():               #Clear all widgets
        widget.destroy()
    user = ntk.StringVar()
    passw = ntk.StringVar()
    tk.Label(installer, text="Create user", font=("Helvetica", 40)).place(relx=0.5, rely=0.1, anchor="center")
    tk.Label(installer, text="Enter username:", font=("Helvetica", 20)).place(relx=0.5, rely=0.2, anchor="center")
    tk.Entry(installer, textvariable=user, font=("Helvetica", 20)).place(relx=0.5, rely=0.3, anchor="center")
    tk.Label(installer, text="Enter password:", font=("Helvetica", 20)).place(relx=0.5, rely=0.4, anchor="center")
    tk.Entry(installer, textvariable=passw, show="*", font=("Helvetica", 20)).place(relx=0.5, rely=0.5, anchor="center")
    tk.Button(installer, text="Next", command=GetKernel).place(relx=0.5, rely=0.6, anchor="center")

def GetKernel():
    global user, passw
    print("echo Received user and password as " + user.get() + " and " + passw.get())
    for widget in installer.winfo_children():               #Clear all widgets
        widget.destroy()
    tk.Label(installer, text="Select kernel", font=("Helvetica", 40)).place(relx=0.5, rely=0.1, anchor="center")
    tk.Button(installer, text="Linux", command=GetKernel).place(relx=0.5, rely=0.2, anchor="center")
    tk.Button(installer, text="Linux-LTS", command=GetKernel).place(relx=0.5, rely=0.3, anchor="center")
    tk.Button(installer, text="Linux-Zen", command=GetKernel).place(relx=0.5, rely=0.4, anchor="center")

#Welcome screen
def Welcome():
                                                            #Create a Welcome frame
    installer.wm_title("Welcome")
    tk.Label(installer, text="Welcome to the CLD installer", font=("Helvetica", 20)).place(relx=0.5, rely=0.5, anchor="center")
    tk.Button(installer, text="Next", command=GetUserPass).place(relx=0.5, rely=0.6, anchor="center")

#Execute all functions
Welcome()

#Window settings
installer.resizable(width=False, height=False)
installer.title("Installer")
installer.geometry("1100x650")
installer.mainloop()
