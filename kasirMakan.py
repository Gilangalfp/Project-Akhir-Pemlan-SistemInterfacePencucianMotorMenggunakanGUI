import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from config import relative_to_assets
from datetime import datetime
import csv

class Menu:
    def __init__(self, window, frame, label_text, images, spinbox_from, spinbox_to, item_type, prices):
        self.window = window
        self.frame = frame
        self.label = Label(self.frame, text=label_text, font=("Times New Roman", 20, "bold"))
        self.label.grid(column=0, row=0, columnspan=3)

        self.canvas = [Canvas(self.frame, width=200, height=200, highlightthickness=0) for _ in range(len(images))]
        self.images = [PhotoImage(file=relative_to_assets(img)) for img in images]

        self.spinbox_list = []
        for i, img in enumerate(self.images):
            self.canvas[i].create_image(100, 100, image=img, anchor='center')
            self.canvas[i].image = img
            self.canvas[i].grid(column=i, row=1, pady=10)

            spinbox = Spinbox(self.frame, from_=spinbox_from, to=spinbox_to, width=5)
            spinbox.grid(column=i, row=2)
            self.spinbox_list.append(spinbox)

        self.item_type = item_type
        self.prices = prices

class FoodMenu(Menu):
    def __init__(self, window, frame, label_text, images, spinbox_from, spinbox_to):
        prices = [15, 20, 25]  # Adjust the prices for each food item
        super().__init__(window, frame, label_text, images, spinbox_from, spinbox_to, "food", prices)

class DrinkMenu(Menu):
    def __init__(self, window, frame, label_text, images, spinbox_from, spinbox_to):
        prices = [10, 12, 15]  # Adjust the prices for each drink item
        super().__init__(window, frame, label_text, images, spinbox_from, spinbox_to, "drink", prices)

class menu_makan:
    def setup(self):
        self.window = Tk()
        self.window.title("Warmindo Restaurant") 
        self.window.geometry("680x700")

        bg_image = Image.open(relative_to_assets("indomiebg.png"))
        resized_bg_image = bg_image.resize((680, 700))
        tk_bg_image = ImageTk.PhotoImage(resized_bg_image)

        background_label = Label(self.window, image=tk_bg_image)
        background_label.image = tk_bg_image
        background_label.place(relwidth=1, relheight=1)

        self.food_frame = Frame(self.window, padx=10, pady=10)
        self.food_frame.grid(column=0, row=3, padx=20)

        self.food_menu = FoodMenu(self.window, self.food_frame, "Pilih Makanan",
                                  ["indomie.png", "indomiejumbo.png", "indomiekuah.png"], 0, 10)

        self.drink_frame = Frame(self.window, padx=10, pady=10)
        self.drink_frame.grid(column=0, row=4, padx=20)

        self.drink_menu = DrinkMenu(self.window, self.drink_frame, "Pilih Minuman",
                                    ["esteh.png", "kopi.png", "esjeruk.png"], 0, 10)

        self.finish = Button(text="Order", command=self.button_clicked)
        self.finish.place(relx=0.2, rely=0.95, anchor="center")

        self.reset_button = Button(text="Reset", command=self.reset_value)
        self.reset_button.place(relx=0.5, rely=0.95, anchor="center")

        self.reset_button = Button(text="Menu Motor", command=self.gotoJunction)
        self.reset_button.place(relx=0.8, rely=0.95, anchor="center")

        self.window.resizable(False, False)
        self.window.mainloop()

    def gotoJunction(self):
        from kasir import menu_home
        self.window.destroy()
        backGUI = menu_home()
        backGUI.setup()

    def reset_value(self):
        for spinbox in self.food_menu.spinbox_list + self.drink_menu.spinbox_list:
            spinbox.delete(0, tk.END)
            spinbox.insert(0, 0)

    def button_clicked(self):
        food_quantities = [int(spinbox.get()) for spinbox in self.food_menu.spinbox_list]
        drink_quantities = [int(spinbox.get()) for spinbox in self.drink_menu.spinbox_list]
        
        food_total = sum(quantity * price for quantity, price in zip(food_quantities, self.food_menu.prices))
        drink_total = sum(quantity * price for quantity, price in zip(drink_quantities, self.drink_menu.prices))
        total_bills = food_total + drink_total
        self.rupiah = f"{total_bills}.000"
        self.saveToCsv(food_quantities, drink_quantities)

        messagebox.showinfo("Rincian pesanan", f"Total harga pesanan anda adalah: Rp. {self.rupiah}")

    def saveToCsv(self, food_quantities, drink_quantities):
        log_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        makan = ', '.join([f"{quantity} {food}" for quantity, food in zip(food_quantities, ["Indomie", "Indomie Jumbo", "Indomie Kuah"])])
        minum = ', '.join([f"{quantity} {drink}" for quantity, drink in zip(drink_quantities, ["Es Teh", "Kopi", "Es Jeruk"])])
        
        with open('Logging.csv', 'a', newline='') as log_file:
            fieldnames = ['Waktu', 'Makan', 'Minum', 'Harga']
            writer = csv.DictWriter(log_file, fieldnames=fieldnames)
            writer.writerow({'Waktu': log_time, 'Makan': makan, 'Minum': minum, 'Harga': self.rupiah})
