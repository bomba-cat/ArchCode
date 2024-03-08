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

#Get user and password
def GetUserPass():
    global user, passw
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
    for widget in installer.winfo_children():               #Clear all widgets
        widget.destroy()
    tk.Label(installer, text="Select kernel", font=("Helvetica", 40)).place(relx=0.5, rely=0.1, anchor="center")
    tk.Button(installer, text="Linux (Recommended)", command=GetDrives).place(relx=0.5, rely=0.2, anchor="center")
    tk.Button(installer, text="Linux-LTS", command=GetDrives).place(relx=0.5, rely=0.3, anchor="center")
    tk.Button(installer, text="Linux-Zen", command=GetDrives).place(relx=0.5, rely=0.4, anchor="center")
    tk.Label(installer, text="Not sure what to pick?", font=("Helvetica", 20)).place(relx=0.5, rely=0.5, anchor="center")
    tk.Label(installer, text="Linux - Latest linux kernel", font=("Helvetica", 10)).place(relx=0.5, rely=0.6, anchor="center")
    tk.Label(installer, text="Linux LTS - Long Term Support kernel", font=("Helvetica", 10)).place(relx=0.5, rely=0.7, anchor="center")
    tk.Label(installer, text="Linux Zen - Hacker tested kernel", font=("Helvetica", 10)).place(relx=0.5, rely=0.8, anchor="center")

def GetDrives():
    drives = linux.popen("lsblk --nodeps --output NAME | grep -v 'NAME'").read()
    for widget in installer.winfo_children():               #Clear all widgets
        widget.destroy()
    drives = drives.split("\n")

    tk.Label(installer, text="Select drive, WARNING: ALL DATA ON DRIVE WILL BE LOST", font=("Helvetica", 20)).place(relx=0.5, rely=0.1, anchor="center")
    tk.Label(installer, text="Drives:", font=("Helvetica", 20)).place(relx=0.5, rely=0.2, anchor="center")

    for drive in drives:
        if drive != "":
            tk.Radiobutton(installer, text=drive, value=drive).place(relx=0.5, rely=0.3+(drives.index(drive)*0.1), anchor="center")

#Welcome
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
