import tkinter as tk
from tkinter import ttk
import numpy as np
from PIL import Image, ImageTk
import yaml
import time


class SMLM:
    def __init__(self):
        config = yaml.safe_load(open("config/config.yml"))
        self.__color = config["colors"]
        self.__fonts = {}
        for font in config['fonts']:
            self.__fonts[font] = (config['fonts'][font]['police'], config['fonts'][font]['size'])

        self.__root = tk.Tk()
        self.__root.title("SMLM")
        self.__root.iconbitmap(r"config/gia.ico")

        self.__size = {'h': int(self.__root.winfo_screenheight()/2-50), 'w': int(self.__root.winfo_screenwidth()/2)}
        self.__root.state('zoomed')
        self.__root.geometry(f"{self.__size['w']}x{self.__size['h']}")
        self.__root.config(background=self.__color['bg1'])

        self.__root.grid_columnconfigure(0, weight=1)
        self.__root.grid_columnconfigure(1, weight=20)
        self.__root.grid_rowconfigure(0, weight=1)

        self.hide = False
        self.__menu()
        self.lShow = tk.Label(self.__root, text=">>", background=self.__color['bg1'], font=self.__fonts['cal16'])
        self.lShow.bind('<Button-1>', lambda event: self.hideShowMenu())

        self.__root.mainloop()

    def __menu(self):
        self.fMenu = tk.LabelFrame(self.__root, background=self.__color['them2'])
        self.fMenu.grid_rowconfigure(0, weight=1)
        self.fMenu.grid_rowconfigure(1, weight=1)
        self.fMenu.grid_rowconfigure(2, weight=1)
        self.fMenu.grid_rowconfigure(3, weight=1)
        self.fMenu.grid_rowconfigure(4, weight=1)
        self.fMenu.grid_rowconfigure(5, weight=1)
        self.fMenu.grid_rowconfigure(6, weight=1)
        self.fMenu.grid_rowconfigure(7, weight=1)
        self.fMenu.grid_columnconfigure(0, weight=1)

        img = Image.open("config/gia.png")
        img = img.resize(size=(200, 200))
        img = ImageTk.PhotoImage(img)
        can = tk.Canvas(self.fMenu, background=self.__color['them2'], height=200, width=200, highlightthickness=0)
        can.picture = img
        can.create_image(0, 0, anchor=tk.NW, image=can.picture)
        can.grid(column=0, row=0)

        l = tk.Label(self.fMenu, text="Acceuil", background=self.__color['them2'], font=self.__fonts['cal16'])
        l.bind("<Button-1>", lambda event: self.__test("Acceuil"))
        l.grid(column=0, row=1, sticky=tk.W, padx=10)

        l = tk.Label(self.fMenu, text="pri---gne???", background=self.__color['them2'], font=self.__fonts['cal16'])
        l.bind("<Button-1>", lambda event: self.__test("pri---gne???"))
        l.grid(column=0, row=2, sticky=tk.W, padx=10)

        l = tk.Label(self.fMenu, text="L'ile?", background=self.__color['them2'], font=self.__fonts['cal16'])
        l.bind("<Button-1>", lambda event: self.__test("L'ile?"))
        l.grid(column=0, row=3, sticky=tk.W, padx=10)

        l = tk.Label(self.fMenu, text="Galerie", background=self.__color['them2'], font=self.__fonts['cal16'])
        l.bind("<Button-1>", lambda event: self.__test("Galerie"))
        l.grid(column=0, row=4, sticky=tk.W, padx=10)

        l = tk.Label(self.fMenu, text="Aide", background=self.__color['them2'], font=self.__fonts['cal16'])
        l.bind("<Button-1>", lambda event: self.__test("Aide"))
        l.grid(column=0, row=5, sticky=tk.W, padx=10)

        l = tk.Label(self.fMenu, text="Favoris", background=self.__color['them2'], font=self.__fonts['cal16'])
        l.bind("<Button-1>", lambda event: self.__test("Favoris"))
        l.grid(column=0, row=6, sticky=tk.W, padx=10)

        self.lHideShowMenu = tk.Label(self.fMenu, text="<<", background=self.__color['them2'], font=self.__fonts['cal16'])
        self.lHideShowMenu.bind("<Button-1>", lambda event: self.hideShowMenu())
        self.lHideShowMenu.grid(column=0, row=7, sticky=tk.E, padx=10)

        self.fMenu.place(width=250, height=self.__root.winfo_screenheight()-50)

    def hideShowMenu(self):
        v = 0.1
        if self.hide:
            self.hide = False
            self.lShow.place_forget()
            x = 0
            n = -250
            while n < 0:
                n = -int(250 * np.exp(-x))
                x += v
                # print(n)
                time.sleep(0.01)
                self.fMenu.place(anchor=tk.NW, width=250, height=self.__root.winfo_screenheight() - 50, x=n)
                self.__root.update()

        else:
            self.hide = True
            x = 0
            n = 0
            while n > -250:
                n = int(250 * np.exp(-x))-250
                x += v
                # print(n)
                time.sleep(0.01)
                self.fMenu.place(anchor=tk.NW, width=250, height=self.__root.winfo_screenheight()-50, x=n)
                self.__root.update()
            # self.fMenu.grid_forget()
            self.lShow.place(anchor=tk.SW, x=0, y=self.__size['h']*2)

    @staticmethod
    def __test(txt):
        print(txt)


if __name__ == '__main__':
    SMLM()