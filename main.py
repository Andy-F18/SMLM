import tkinter as tk
# from tkinter import ttk
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
        self.__root.resizable(False, False)

        self.__size = {'h': int(self.__root.winfo_screenheight()/2-50), 'w': int(self.__root.winfo_screenwidth()/2)}
        self.__root.state('zoomed')
        self.__root.geometry(f"{self.__size['w']}x{self.__size['h']}")
        self.__root.config(background=self.__color['bg1'])

        self.__root.grid_columnconfigure(0, weight=1)
        self.__root.grid_columnconfigure(1, weight=20)
        self.__root.grid_rowconfigure(0, weight=1)

        self.__hide = False
        self.__menu()
        self.__lShow = tk.Label(self.__root, text=">>", background=self.__color['bg1'], font=self.__fonts['cal16'])
        self.__lShow.bind('<Button-1>', lambda event: self.__hideShowMenu())
        self.__lShow.bind('<Enter>', lambda event, lab=self.__lShow: self.__hoverMenuE(lab))
        self.__lShow.bind('<Leave>', lambda event, lab=self.__lShow: self.__hoverMenuL(lab))

        self.__root.mainloop()

    def __menu(self):
        self.__fMenu = tk.LabelFrame(self.__root, background=self.__color['them2'])
        self.__fMenu.grid_rowconfigure(0, weight=1)
        self.__fMenu.grid_rowconfigure(1, weight=1)
        self.__fMenu.grid_rowconfigure(2, weight=1)
        self.__fMenu.grid_rowconfigure(3, weight=1)
        self.__fMenu.grid_rowconfigure(4, weight=1)
        self.__fMenu.grid_rowconfigure(5, weight=1)
        self.__fMenu.grid_rowconfigure(6, weight=1)
        self.__fMenu.grid_rowconfigure(7, weight=1)
        self.__fMenu.grid_columnconfigure(0, weight=1)

        img = Image.open("config/gia3.png")
        img2 = Image.open("config/fanion.png")
        img = img.resize(size=(179, 179))
        img2 = img2.resize(size=(int(200/img2.height*img2.width), 200))
        img = ImageTk.PhotoImage(img)
        img2 = ImageTk.PhotoImage(img2)
        can = tk.Canvas(self.__fMenu, background=self.__color['them2'], height=300, width=200, highlightthickness=0)

        can.picture1 = img
        can.picture2 = img2
        can.create_image(100, 100, anchor=tk.N, image=can.picture2)
        can.create_image(100, 0, anchor=tk.N, image=can.picture1)
        can.grid(column=0, row=0)

        l = tk.Label(self.__fMenu, text="Acceuil", background=self.__color['them2'], font=self.__fonts['cal16'])
        l.bind("<Button-1>", lambda event: self.__test("Acceuil"))
        l.bind('<Enter>', lambda event, lab=l: self.__hoverMenuE(lab))
        l.bind('<Leave>', lambda event, lab=l: self.__hoverMenuL(lab))
        l.grid(column=0, row=1, sticky=tk.NSEW, padx=10)

        l = tk.Label(self.__fMenu, text="Personnages", background=self.__color['them2'], font=self.__fonts['cal16'])
        l.bind("<Button-1>", lambda event: self.__test("Personnages"))
        l.bind('<Enter>', lambda event, lab=l: self.__hoverMenuE(lab))
        l.bind('<Leave>', lambda event, lab=l: self.__hoverMenuL(lab))
        l.grid(column=0, row=2, sticky=tk.NSEW, padx=10)

        l = tk.Label(self.__fMenu, text="L'ile?", background=self.__color['them2'], font=self.__fonts['cal16'])
        l.bind("<Button-1>", lambda event: self.__test("L'ile?"))
        l.bind('<Enter>', lambda event, lab=l: self.__hoverMenuE(lab))
        l.bind('<Leave>', lambda event, lab=l: self.__hoverMenuL(lab))
        l.grid(column=0, row=3, sticky=tk.NSEW, padx=10)

        l = tk.Label(self.__fMenu, text="Galerie", background=self.__color['them2'], font=self.__fonts['cal16'])
        l.bind("<Button-1>", lambda event: self.__test("Galerie"))
        l.bind('<Enter>', lambda event, lab=l: self.__hoverMenuE(lab))
        l.bind('<Leave>', lambda event, lab=l: self.__hoverMenuL(lab))
        l.grid(column=0, row=4, sticky=tk.NSEW, padx=10)

        l = tk.Label(self.__fMenu, text="Aide", background=self.__color['them2'], font=self.__fonts['cal16'])
        l.bind("<Button-1>", lambda event: self.__test("Aide"))
        l.bind('<Enter>', lambda event, lab=l: self.__hoverMenuE(lab))
        l.bind('<Leave>', lambda event, lab=l: self.__hoverMenuL(lab))
        l.grid(column=0, row=5, sticky=tk.NSEW, padx=10)

        l = tk.Label(self.__fMenu, text="Favoris", background=self.__color['them2'], font=self.__fonts['cal16'])
        l.bind("<Button-1>", lambda event: self.__test("Favoris"))
        l.bind('<Enter>', lambda event, lab=l: self.__hoverMenuE(lab))
        l.bind('<Leave>', lambda event, lab=l: self.__hoverMenuL(lab))
        l.grid(column=0, row=6, sticky=tk.NSEW, padx=10)

        self.__lHideShowMenu = tk.Label(self.__fMenu, text="<<", background=self.__color['them2'],
                                        font=self.__fonts['cal16'])
        self.__lHideShowMenu.bind("<Button-1>", lambda event: self.__hideShowMenu())
        self.__lHideShowMenu.bind('<Enter>', lambda event, lab=self.__lHideShowMenu: self.__hoverMenuE(lab))
        self.__lHideShowMenu.bind('<Leave>', lambda event, lab=self.__lHideShowMenu: self.__hoverMenuL(lab))
        self.__lHideShowMenu.grid(column=0, row=7, sticky=tk.E, padx=10)

        self.__fMenu.place(width=250, height=self.__root.winfo_screenheight() - 50)

    def __hideShowMenu(self):
        v = 0.15
        if self.__hide:
            self.__hide = False
            self.__lShow.place_forget()
            x = 0
            n = -250
            while n < 0:
                n = -int(250 * np.exp(-x))
                x += v
                # print(n)
                time.sleep(0.01)
                self.__fMenu.place(anchor=tk.NW, width=250, height=self.__root.winfo_screenheight() - 50, x=n)
                self.__fMenu.update()

        else:
            self.__hide = True
            x = 0
            n = 0
            while n > -250:
                n = int(250 * np.exp(-x))-250
                x += v
                # print(n)
                time.sleep(0.01)
                self.__fMenu.place(anchor=tk.NW, width=250, height=self.__root.winfo_screenheight() - 50, x=n)
                self.__fMenu.update()
            # self.fMenu.grid_forget()
            self.__lShow.place(anchor=tk.SW, x=0, y=self.__size['h'] * 2)

    def __hoverMenuE(self, widget):
        widget.config(font=self.__fonts['cal20'])

    def __hoverMenuL(self, widget):
        widget.config(font=self.__fonts['cal16'])

    @staticmethod
    def __test(txt):
        print(txt)


if __name__ == '__main__':
    SMLM()