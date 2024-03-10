#Imports
import tkinter as ntk
from tkinter import ttk as tk
from ttkthemes import ThemedTk
import os as linux

#Variables
user = ""
passw = ""
kernel = ""
drive = ""

#Create window class
installer = ThemedTk(theme="breeze")

#Get user and password
def GetUserPass():
    global user, passw
    for widget in installer.winfo_children():               #Clear all widgets
        widget.destroy()
    user = ntk.StringVar()
    passw = ntk.StringVar()
    tk.Label(installer, text="Create user", font=("Courier New", 40)).place(relx=0.5, rely=0.1, anchor="center")
    tk.Label(installer, text="Enter username:", font=("Courier New", 20)).place(relx=0.5, rely=0.2, anchor="center")
    tk.Entry(installer, textvariable=user, font=("Courier New", 20)).place(relx=0.5, rely=0.3, anchor="center")
    tk.Label(installer, text="Enter password:", font=("Courier New", 20)).place(relx=0.5, rely=0.4, anchor="center")
    tk.Entry(installer, textvariable=passw, show="*", font=("Courier New", 20)).place(relx=0.5, rely=0.5, anchor="center")
    tk.Button(installer, text="Next", command=GetKernel).place(relx=0.5, rely=0.6, anchor="center")

def GetKernel():
    global kernel
    for widget in installer.winfo_children():               #Clear all widgets
        widget.destroy()
    tk.Label(installer, text="Select kernel", font=("Courier New", 40)).place(relx=0.5, rely=0.1, anchor="center")
    tk.Button(installer, text="Linux (Recommended)", command=lambda: GetDrives("linux")).place(relx=0.5, rely=0.2, anchor="center")
    tk.Button(installer, text="Linux-LTS", command=lambda: GetDrives("linux-lts")).place(relx=0.5, rely=0.3, anchor="center")
    tk.Button(installer, text="Linux-Zen", command=lambda: GetDrives("linux-zen")).place(relx=0.5, rely=0.4, anchor="center")
    tk.Label(installer, text="Not sure what to pick?", font=("Courier New", 20)).place(relx=0.5, rely=0.5, anchor="center")
    tk.Label(installer, text="Linux - Latest linux kernel", font=("Courier New", 10)).place(relx=0.5, rely=0.6, anchor="center")
    tk.Label(installer, text="Linux LTS - Long Term Support kernel", font=("Courier New", 10)).place(relx=0.5, rely=0.7, anchor="center")
    tk.Label(installer, text="Linux Zen - Hacker tested kernel", font=("Courier New", 10)).place(relx=0.5, rely=0.8, anchor="center")

def GetDrives(chosenKernel):
    global kernel, drive
    kernel = chosenKernel
    drives = linux.popen("lsblk --nodeps --output NAME | grep -v 'NAME'").read()
    for widget in installer.winfo_children():               #Clear all widgets
        widget.destroy()
    drives = drives.split("\n")

    tk.Label(installer, text="Select drive, WARNING: ALL DATA ON DRIVE WILL BE LOST", font=("Courier New", 20)).place(relx=0.5, rely=0.1, anchor="center")
    tk.Label(installer, text="Drives:", font=("Courier New", 20)).place(relx=0.5, rely=0.2, anchor="center")

    for d in drives:
        if d != "":
            tk.Radiobutton(installer, text=d, value=d, variable=drive).place(relx=0.5, rely=0.3+(drives.index(d)*0.1), anchor="center")

#Welcome
def Welcome():
                                                            #Create a Welcome frame
    installer.wm_title("Welcome")
    tk.Label(installer, text="Welcome to the ArchCode installer", font=("Courier New", 20)).place(relx=0.5, rely=0.5, anchor="center")
    tk.Button(installer, text="Next", command=GetUserPass).place(relx=0.5, rely=0.6, anchor="center")

#Execute all functions
Welcome()

#Window settings
installer.resizable(width=False, height=False)
installer.title("Installer")
installer.geometry("1100x650")
installer.mainloop()
