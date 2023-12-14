import tkinter as tk
import csv
import os
from tkinter import *
from tkinter import Tk, ttk, Canvas, Entry, Button, PhotoImage, messagebox
from datetime import datetime
from config import relative_to_assets
from kasirMakan import menu_makan

class menu_home:

    def setup(self):
        self.jenisMotor = []
        self.homepage = Tk()
        self.homepage.title("PROGRAM KASIR")
        self.homepage.geometry("720x600")
        self.homepage.configure(bg="#FFFFFF")
        self.cekDatabase()
        canvasH = Canvas(self.homepage, bg="#FFFFFF", height=480, width=720, bd=0, highlightthickness=0, relief="ridge")
        canvasH.place(x=0, y=0)
        # entry1
        inputP_image = PhotoImage(file=relative_to_assets("home_entry1.png"))
        inputP_BG = canvasH.create_image(206.5, 169.0, image=inputP_image)
        self.inputP = Entry(bd=0, bg="#BEDCE1", fg="#000716", highlightthickness=0, font=("Arial 12"))
        self.inputP.place(x=114.0, y=150.0, width=185.0, height=38.0)
        # entry2
        inputP_image2 = PhotoImage(file=relative_to_assets("home_entry1.png"))
        inputP_BG2 = canvasH.create_image(208.5, 241.0, image=inputP_image2)
        self.inputP2 = Entry(bd=0, bg="#BEDCE1", fg="#000716", highlightthickness=0, font=("Arial 12"))
        self.inputP2.place(x=116.0, y=222.0, width=185.0, height=38.0)
        # combobox
        self.framecombo = Frame(self.homepage, width=209.0, height=40, bg="white")
        self.framecombo.place(x=104.0, y=301.0)
        self.combo_image = PhotoImage(file=relative_to_assets("combobox.png"))
        self.combo1 = Button(self.framecombo, image=self.combo_image, borderwidth=0, highlightthickness=0, command=self.comboboxD,relief="flat")
        self.combo1.place(x=0.0, y=0.0, width=209.0, height=40.0)
        # button input data
        dataimage = PhotoImage(file=relative_to_assets("input_data.png"))
        dataButton = Button(image=dataimage, borderwidth=0, highlightthickness=0, command=self.inputdata, relief="flat")
        dataButton.place(x=449.0, y=218.0, width=186.0, height=45.0)
        # Text di home
        canvasH.create_text(109.0, 124.0, anchor="nw", text="Plat Motor", fill="#000000",font=("OpenSansRoman Bold", 14 * -1))
        canvasH.create_text(109.0, 198.0, anchor="nw", text="Nama Motor", fill="#000000",font=("OpenSansRoman Bold", 14 * -1))
        canvasH.create_text(109.0, 274.0, anchor="nw", text="Jenis Motor", fill="#000000",font=("OpenSansRoman Bold", 14 * -1))
        # tempat menu
        self.frameM = Frame(self.homepage, width=720, height=70, bg="#6E8C91")
        self.frameM.place(x=0,y=0)

        self.textTM = Label(self.frameM, text="MENU UTAMA")
        self.textTM.config(font=("Open Sans", 24,'bold'), fg="white", bg="#6E8C91")
        self.textTM.place(x=410.0, y=14.0)
        garisIM = PhotoImage(file=relative_to_assets("garis.png"))
        garis = Label(self.frameM, image=garisIM, bg="#6E8C91")
        garis.place(x=315.0, y=6.0)
        # tombol exit
        exitBut = PhotoImage(file=relative_to_assets("exit.png"))
        exitB = Button(image=exitBut, borderwidth=0, highlightthickness=0, command=self.exitMenu,relief="flat")
        exitB.place(x=22.0, y=8.0, width=55.0, height=55.0)
        # tombol home
        homeBut = PhotoImage(file=relative_to_assets("home.png"))
        homeB = Button(image=homeBut, borderwidth=0, highlightthickness=0, command=self.homeMenu, relief="flat")
        homeB.place(x=90.0, y=8.0, width=55.0, height=55.0)
        # tombol bayar
        bayarBut = PhotoImage(file=relative_to_assets("bayar.png"))
        bayarB = Button(image=bayarBut, borderwidth=0, highlightthickness=0, command=self.bayarMenu, relief="flat")
        bayarB.place(x=158.0, y=8.0, width=55.0, height=55.0)
        #tombol makan
        makanBut = PhotoImage(file=relative_to_assets("makan.png"))
        makanB = Button(image=makanBut, borderwidth=0, highlightthickness=0, command=self.gotoMenuMakan, relief="flat")
        makanB.place(x=226.0, y=8.0, width=55.0, height=55.0)

        #setting page home
        self.homepage.resizable(False, False)
        self.homepage.mainloop()

    def inputdata(self):
        platM = self.inputP.get()
        namaM = self.inputP2.get()
        if len(self.jenisMotor) != 0:
            for i in range(len(self.jenisMotor) - 1, len(self.jenisMotor)):
                jenisM = self.jenisMotor[i]
            if platM == "" or namaM == "" or jenisM == "":
                messagebox.showerror("WARNING", "Ada data yang belum diinput!")
            else:
                if jenisM == 'Motor Kecil':
                    log_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                    with open('Logging.csv', 'a', newline='') as log_file:
                        fieldnames = ['Waktu', 'PlatM', 'NamaM', 'JenisM', 'Harga']
                        writer = csv.DictWriter(log_file, fieldnames=fieldnames)
                        writer.writerow({'Waktu': log_time, 'PlatM': platM, 'NamaM': namaM, 'JenisM': jenisM, 'Harga': 15000})
                    with open('databaseM.csv', 'a', newline='') as file:
                        fieldnames = ['PlatM', 'NamaM', 'jenisM', 'Harga']
                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        writer.writerow({'PlatM': platM, 'NamaM': namaM, 'jenisM': jenisM, 'Harga': 15000})

                elif jenisM == 'Motor Besar':
                    log_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    with open('Logging.csv', 'a', newline='') as log_file:
                        fieldnames = ['Waktu', 'PlatM', 'NamaM', 'JenisM', 'Harga']
                        writer = csv.DictWriter(log_file, fieldnames=fieldnames)
                        writer.writerow({'Waktu': log_time, 'PlatM': platM, 'NamaM': namaM, 'JenisM': jenisM, 'Harga': 18000})
                    with open('databaseM.csv', 'a', newline='') as file:
                        fieldnames = ['PlatM', 'NamaM', 'jenisM', 'Harga']
                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        writer.writerow({'PlatM': platM, 'NamaM': namaM, 'jenisM': jenisM, 'Harga': 18000})

                elif jenisM == 'Motor Trail':
                    log_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    with open('Logging.csv', 'a', newline='') as log_file:
                        fieldnames = ['Waktu', 'PlatM', 'NamaM', 'JenisM', 'Harga']
                        writer = csv.DictWriter(log_file, fieldnames=fieldnames)
                        writer.writerow({'Waktu': log_time, 'PlatM': platM, 'NamaM': namaM, 'JenisM': jenisM, 'Harga': 22000})
                    with open('databaseM.csv', 'a', newline='') as file:
                        fieldnames = ['PlatM', 'NamaM', 'jenisM', 'Harga']
                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        writer.writerow({'PlatM': platM, 'NamaM': namaM, 'jenisM': jenisM, 'Harga': 22000})

                self.jenisMotor.pop(0)
                self.combo1.destroy()
                self.combo_image = PhotoImage(file=relative_to_assets("combobox.png"))
                self.combo1 = Button(self.framecombo, image=self.combo_image, borderwidth=0, highlightthickness=0, command=self.comboboxD,relief="flat")
                self.combo1.place(x=0.0, y=0.0, width=209.0, height=40.0)
                self.inputP.delete(0, END)
                self.inputP2.delete(0, END)
                messagebox.showinfo("Information", "Data berhasil diinput!")
        else:
            messagebox.showerror("WARNING", "Ada data yang belum diinput!")

    def comboboxD(self):
        self.frameisiC = Frame(self.homepage, width=143, height=111, bg="white", highlightthickness=1,highlightbackground="black")
        self.frameisiC.place(x=318.0, y=302.0)
        self.comboTimage = PhotoImage(file=relative_to_assets("combotrail.png"))
        self.comboT = Button(self.frameisiC, image=self.comboTimage, borderwidth=0, highlightthickness=0, command=self.opsicombo3,relief="flat")
        self.comboT.place(x=0.0, y=72.0, width=140.0, height=37.0)
        self.comboGimage = PhotoImage(file=relative_to_assets("combogede.png"))
        self.comboG = Button(self.frameisiC, image=self.comboGimage, borderwidth=0, highlightthickness=0, command=self.opsicombo2,relief="flat")
        self.comboG.place(x=0.0, y=40.0, width=140.0, height=31.0)
        self.comboKimage = PhotoImage(file=relative_to_assets("combokecil.png"))
        self.comboK = Button(self.frameisiC, image=self.comboKimage, borderwidth=0, highlightthickness=0, command=self.opsicombo1,relief="flat")
        self.comboK.place(x=0.0, y=0.0, width=140.0, height=39.0)

    def opsicombo1(self):
        self.frameisiC.destroy()
        self.combo1.destroy()
        self.combo_image = PhotoImage(file=relative_to_assets("Motor_Kecil.png"))
        self.combo1 = Button(self.framecombo, image=self.combo_image, borderwidth=0, highlightthickness=0, command=self.comboboxD,relief="flat")
        self.combo1.place(x=0.0, y=0.0, width=209.0, height=40.0)
        self.jenisMotor.append("Motor Kecil")

    def opsicombo2(self):
        self.frameisiC.destroy()
        self.combo1.destroy()
        self.combo_image = PhotoImage(file=relative_to_assets("Motor_Besar.png"))
        self.combo1 = Button(self.framecombo, image=self.combo_image, borderwidth=0, highlightthickness=0, command=self.comboboxD,relief="flat")
        self.combo1.place(x=0.0, y=0.0, width=209.0, height=40.0)
        self.jenisMotor.append("Motor Besar")

    def opsicombo3(self):
        self.frameisiC.destroy()
        self.combo1.destroy()
        self.combo_image = PhotoImage(file=relative_to_assets("Motor_Trail.png"))
        self.combo1 = Button(self.framecombo, image=self.combo_image, borderwidth=0, highlightthickness=0, command=self.comboboxD,relief="flat")
        self.combo1.place(x=0.0, y=0.0, width=209.0, height=40.0)
        self.jenisMotor.append("Motor Trail")

    def exitMenu(self):
        msg_box = tk.messagebox.askquestion('Keluar Aplikasi', 'Apakah ingin keluar dari aplikasi?',icon='warning')
        if msg_box == 'yes':
            self.homepage.destroy()
        else:
            pass
    
    def gotoMenuMakan(self):
        self.homepage.destroy()
        makanGUI = menu_makan()
        makanGUI.setup()

    def cekDatabase(self):
        if not os.path.isfile('databaseM.csv'):
            with open('databaseM.csv', 'w', newline='') as temp2:
                    kolom = ['plat', 'nama', 'jenis', 'harga']
                    databaru = csv.DictWriter(temp2, kolom)
                    databaru.writeheader()
                            
    def homeMenu(self):
        try:
            self.textTM2.destroy()
            frameB.destroy()
            frameBD.destroy()
            textTM = Label(self.frameM, text="MENU UTAMA")
            textTM.config(font=("Open Sans", 24, 'bold'), fg="white", bg="#6E8C91")
            textTM.place(x=410.0, y=14.0)
        except:
            pass

    def bayarMenu(self):
        data = []
        try:
            self.textTM.destroy()
            self.textTM2 = Label(self.frameM, text="MENU BAYAR")
            self.textTM2.config(font=("Open Sans", 24, 'bold'), fg="white", bg="#6E8C91")
            self.textTM2.place(x=413.0, y=14.0)
        except:
            pass

        def bayar():
            total_tmp = []
            total = 0
            temp1 = open('databaseM.csv', 'r')
            harga = self.treeview.selection()

            for item in harga:
                index = self.treeview.index(item)  # Use treeview.index to get the index
                total_tmp = data[index]
                total += int(total_tmp["harga"])

            msg_box = tk.messagebox.askquestion('PEMBAYARAN', f"Total pembayaran adalah {total}. Apakah Anda yakin ingin membayar?")
            temp1.close()

            if msg_box == 'yes':
                for item in harga:
                    index = self.treeview.index(item)
                    data.pop(index)

                with open('databaseM.csv', 'w', newline='') as temp2:
                    kolom = ['plat', 'nama', 'jenis', 'harga']
                    databaru = csv.DictWriter(temp2, kolom)
                    databaru.writeheader()
                    for jumlah in data:
                        databaru.writerow(jumlah)
                temp2.close()

                for item in harga[::-1]:
                    self.treeview.delete(item)
            else:
                pass

        def hapusdata():
            msg_box = tk.messagebox.askquestion('HAPUS DATA', 'Apakah ingin menghapus data?', icon='warning')
            if msg_box == 'yes':
                temp1 = open('databaseM.csv', 'r')
                items_to_delete = self.treeview.selection()

                indexes_to_delete = [self.treeview.index(item) for item in items_to_delete]
                for index in sorted(indexes_to_delete, reverse=True):
                    data.pop(index)

                temp1.close()
                with open('databaseM.csv', 'w', newline='') as temp2:
                    kolom = ['plat', 'nama', 'jenis', 'harga']
                    databaru = csv.DictWriter(temp2, kolom)
                    databaru.writeheader()

                    for jumlah in data:
                        databaru.writerow(jumlah)
                temp2.close()

                for item in items_to_delete:
                    self.treeview.delete(item)
            else:
                pass

        def isitabel():
            global frameB, frameBD, butbayarIM, buthapusIM

            frameB = tk.Frame(self.homepage, width=720, height=600, bg="white")
            frameB.place(x=0, y=70)
            frameBD = tk.Frame(frameB, width=430, height=348, bg="white", highlightthickness=1, highlightbackground="black")
            frameBD.place(x=40.0, y=30)

            # scrollbar
            scrolly = tk.Scrollbar(frameBD, orient=tk.VERTICAL)
            scrolly.pack(side=tk.RIGHT, fill=tk.Y)

            # horizontal scrollbar
            scrollx = tk.Scrollbar(frameBD, orient=tk.HORIZONTAL)
            scrollx.pack(side=tk.BOTTOM, fill=tk.X)

            # treeview with checkboxes
            self.treeview = ttk.Treeview(frameBD, columns=("PlatM", "NamaM", "jenisM", "Harga"), selectmode='extended', yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
            self.treeview.heading("#0", text="Index")
            self.treeview.heading("PlatM", text="Plat Motor")
            self.treeview.heading("NamaM", text="Nama Motor")
            self.treeview.heading("jenisM", text="Jenis Motor")
            self.treeview.heading("Harga", text="Harga")
            self.treeview.column("#0", width=0, stretch=tk.NO)
            self.treeview.column("PlatM", anchor=tk.W, width=150)
            self.treeview.column("NamaM", anchor=tk.W, width=150)
            self.treeview.column("jenisM", anchor=tk.W, width=150)
            self.treeview.column("Harga", anchor=tk.W, width=150)

            self.treeview.pack(expand=tk.YES, fill=tk.BOTH, side=tk.LEFT)

            # scrollbar config
            scrolly.config(command=self.treeview.yview)
            scrollx.config(command=self.treeview.xview)

            try:
                self.cekDatabase()  
                pass
            except:
                raise ("File already exists")

            with open('databaseM.csv') as f:
                reader = csv.DictReader(f, delimiter=',')
                for idx, row in enumerate(reader):
                    data.append(row)
                    self.treeview.insert("", "end", values=(row["plat"], row["nama"], row["jenis"], row["harga"]))
                    data[-1]["index"] = idx

            # tombol
            butbayarIM = tk.PhotoImage(file=relative_to_assets("tombolbayar.png"))
            butbayar = tk.Button(frameB, image=butbayarIM, borderwidth=0, highlightthickness=0, command=bayar, relief="flat")
            butbayar.place(x=170.0, y=400.0, width=130.0, height=39.0)

            buthapusIM = tk.PhotoImage(file=relative_to_assets("hapus.png"))
            button_2 = tk.Button(frameB, image=buthapusIM, borderwidth=0, highlightthickness=0, command=hapusdata, relief="flat")
            button_2.place(x=400.0, y=400.0, width=130.0, height=39.0)

        try:
            frameB.destroy()
            isitabel()
        except:
            isitabel()

