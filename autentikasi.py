import tkinter as tk
import customtkinter
import csv
import os
from tkinter import PhotoImage, messagebox
from config import relative_to_assets
from kasir import menu_home

class LoginGUI:

    def setup(self):
        if 'self.window' in globals():
            self.window.destroy()

        customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

        self.logintk = customtkinter.CTk()
        self.logintk.geometry("600x440")
        self.logintk.title('Login')    
        
        img1 = PhotoImage(file=relative_to_assets("pattern.png"))
        l1=customtkinter.CTkLabel(master=self.logintk,image=img1)
        l1.pack()

        frame=customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=15)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        l2=customtkinter.CTkLabel(master=frame, text="Admin Login",font=('Century Gothic',20))
        l2.place(x=50, y=45)

        self.nameI=customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Username')
        self.nameI.place(x=50, y=110)

        self.passI=customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Password', show="*")
        self.passI.place(x=50, y=165)

        button1 = customtkinter.CTkButton(master=frame, width=220, text="Login", command=self.login, corner_radius=6)
        button1.place(x=50, y=240)

        button2 = customtkinter.CTkButton(master=frame, width=220, text="Register", command=self.register, corner_radius=6)
        button2.place(x=50, y=280)
        self.logintk.mainloop()

    def register(self):
        self.cekfile()
        self.logintk.destroy()
    
        customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

        self.window = customtkinter.CTk()
        self.window.geometry("600x440")
        self.window.title('Login')    
        
        img1 = PhotoImage(file=relative_to_assets("pattern.png"))
        l1=customtkinter.CTkLabel(master=self.window,image=img1)
        l1.pack()

        frame=customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=15)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        l2=customtkinter.CTkLabel(master=frame, text="Admin Register",font=('Century Gothic',20))
        l2.place(x=50, y=45)

        self.nameI=customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Username')
        self.nameI.place(x=50, y=110)

        self.passI=customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Password', show="*")
        self.passI.place(x=50, y=165)
        
        button1 = customtkinter.CTkButton(master=frame, width=220, text="Register", command=self.save_to_csv, corner_radius=6)
        button1.place(x=50, y=220)
        
        button2 = customtkinter.CTkButton(master=frame, width=50, text="Back", command=self.goToBack, corner_radius=6)
        button2.place(x=220, y=260)

        self.window.mainloop()

    def goToBack(self):
        self.window.destroy()
        self.setup()

    def save_to_csv(self):
        self.cekfile()
        with open('register.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.nameI.get(), self.passI.get()])
        messagebox = tk.messagebox.askquestion("Success", "Register successful, please go back to login menu")
        if messagebox == 'yes':
            self.goToBack()

    def login(self):
        self.cekfile()
        with open('register.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if [self.nameI.get(), self.passI.get()] == row:
                    messagebox.showinfo("Success", "Login successful")
                    self.logintk.destroy()
                    menu_GUI = menu_home()
                    menu_GUI.setup()
                    return
            messagebox.showerror("Error", "Login failed")


    def cekfile(self):
       if not os.path.isfile('register.csv'):
        with open('register.csv', 'w') as file:
            writer = csv.writer(file)