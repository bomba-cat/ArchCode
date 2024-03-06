import tkinter as tk
import os as linux

bg = None

installer = tk.Tk()

linux.system("echo 'Welcome to the CLD installer'")

def GetUserPass():
    linux.system("echo Getting user and password")

def Welcome():
    global bg
    bg = tk.PhotoImage(file="welcome.png")
    installer.wm_title("Welcome")
    tk.Label(installer, image=bg).place(relx=0.5, rely=0.5, anchor="center")
    tk.Label(installer, text="Welcome to the CLD installer", font=("Helvetica", 20)).place(relx=0.5, rely=0.5, anchor="center")
    tk.Button(installer, text="Next", command=GetUserPass).place(relx=0.5, rely=0.6, anchor="center")

# Execute all functions
Welcome()

installer.resizable(width=False, height=False)
installer.title("Installer")
installer.geometry("1100x650")
installer.mainloop()
