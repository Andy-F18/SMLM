import os
import tkinter as tk
from tkinter import font, ttk
import numpy as np
from PIL import Image, ImageTk
import yaml
import requests as rqst

from pages.PagePerso import PagePerso
import smlmInstaller as smlmI


class SMLM:
    def __init__(self):
        self.__version = "2022.09.17"
        if not smlmI.smlmInstallerCheck():
            instWin = tk.Tk()
            tk.Label(instWin, text="Install SMLM?").pack(pady="10")
            tk.Button(instWin, text="Install", command=lambda win=instWin: smlmI.smlmInstaller(win)).pack(pady=10)
            instWin.mainloop()

        self.__updateCheck()

        config = yaml.safe_load(open("config/config.yml"))
        self.__color = config["colors"]

        self.__root = tk.Tk()
        self.__root.title("SMLM")
        self.__root.iconbitmap(r"config/gia.ico")
        self.__root.resizable(False, False)

        self.__fonts = list(font.families())
        self.__fonts.sort()
        self.__font = config['font']

        self.__size = {'h': self.__root.winfo_screenheight(), 'w': self.__root.winfo_screenwidth()}
        self.__root.attributes("-fullscreen", True)
        self.__root.geometry(f"{self.__size['w']}x{self.__size['h']}")
        self.__root.config(background=self.__color['bg1'])

        self.__root.grid_columnconfigure(0, weight=1)
        self.__root.grid_rowconfigure(0, weight=1)

        self.__fMain = tk.Frame(self.__root, background=self.__color['bg1'])
        self.__fMain.grid(column=0, row=0, sticky=tk.NSEW)
        self.__fMain.grid_rowconfigure(1, weight=1)
        self.__fMain.grid_columnconfigure(0, weight=1)

        self.__menu()
        self.__v = 0.1
        self.__x = 0
        self.__posMenu = 0
        self.__acceuil()

        self.__root.mainloop()

    def font(self, size):
        return self.__font, size

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
        self.__fMenu.grid_rowconfigure(8, weight=1)
        self.__fMenu.grid_rowconfigure(9, weight=1)
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

        l = tk.Label(self.__fMenu, text="Acceuil", background=self.__color['them2'], font=self.font(16))
        l.bind("<Button-1>", lambda event: self.__acceuil())
        l.bind('<Enter>', lambda event, lab=l: self.__hoverMenuE(lab))
        l.bind('<Leave>', lambda event, lab=l: self.__hoverMenuL(lab))
        l.grid(column=0, row=1, sticky=tk.NSEW, padx=10)

        l = tk.Label(self.__fMenu, text="Personnages", background=self.__color['them2'], font=self.font(16))
        l.bind("<Button-1>", lambda event: self.__personnages())
        l.bind('<Enter>', lambda event, lab=l: self.__hoverMenuE(lab))
        l.bind('<Leave>', lambda event, lab=l: self.__hoverMenuL(lab))
        l.grid(column=0, row=2, sticky=tk.NSEW, padx=10)

        l = tk.Label(self.__fMenu, text="L'ile?", background=self.__color['them2'], font=self.font(16))
        l.bind("<Button-1>", lambda event: self.__lIle())
        l.bind('<Enter>', lambda event, lab=l: self.__hoverMenuE(lab))
        l.bind('<Leave>', lambda event, lab=l: self.__hoverMenuL(lab))
        l.grid(column=0, row=3, sticky=tk.NSEW, padx=10)

        l = tk.Label(self.__fMenu, text="Galerie", background=self.__color['them2'], font=self.font(16))
        l.bind("<Button-1>", lambda event: self.__galerie())
        l.bind('<Enter>', lambda event, lab=l: self.__hoverMenuE(lab))
        l.bind('<Leave>', lambda event, lab=l: self.__hoverMenuL(lab))
        l.grid(column=0, row=4, sticky=tk.NSEW, padx=10)

        l = tk.Label(self.__fMenu, text="Aide", background=self.__color['them2'], font=self.font(16))
        l.bind("<Button-1>", lambda event: self.__aide())
        l.bind('<Enter>', lambda event, lab=l: self.__hoverMenuE(lab))
        l.bind('<Leave>', lambda event, lab=l: self.__hoverMenuL(lab))
        l.grid(column=0, row=5, sticky=tk.NSEW, padx=10)

        l = tk.Label(self.__fMenu, text="Favoris", background=self.__color['them2'], font=self.font(16))
        l.bind("<Button-1>", lambda event: self.__favoris())
        l.bind('<Enter>', lambda event, lab=l: self.__hoverMenuE(lab))
        l.bind('<Leave>', lambda event, lab=l: self.__hoverMenuL(lab))
        l.grid(column=0, row=6, sticky=tk.NSEW, padx=10)

        l = tk.Label(self.__fMenu, text="Options", background=self.__color['them2'], font=self.font(16))
        l.bind("<Button-1>", lambda event: self.__options())
        l.bind('<Enter>', lambda event, lab=l: self.__hoverMenuE(lab))
        l.bind('<Leave>', lambda event, lab=l: self.__hoverMenuL(lab))
        l.grid(column=0, row=7, sticky=tk.NSEW, padx=10)

        l = tk.Label(self.__fMenu, text="Quitter", background=self.__color['them2'], font=self.font(16))
        l.bind("<Button-1>", lambda event: self.__root.quit())
        l.bind('<Enter>', lambda event, lab=l: self.__hoverMenuE(lab))
        l.bind('<Leave>', lambda event, lab=l: self.__hoverMenuL(lab))
        l.grid(column=0, row=8, sticky=tk.NSEW, padx=10)

        self.__lHideMenu = tk.Label(self.__fMenu, text="<<", background=self.__color['them2'], font=self.font(16))
        self.__lHideMenu.bind("<Button-1>", lambda event: self.__hideMenu())
        self.__lHideMenu.bind('<Enter>', lambda event, lab=self.__lHideMenu: self.__hoverMenuE(lab))
        self.__lHideMenu.bind('<Leave>', lambda event, lab=self.__lHideMenu: self.__hoverMenuL(lab))
        self.__lHideMenu.grid(column=0, row=9, sticky=tk.E, padx=10)

        self.__lShowMenu = tk.Label(self.__root, text=">>", background=self.__color['bg1'], font=self.font(16))
        self.__lShowMenu.bind('<Button-1>', lambda event: self.__showMenu())
        self.__lShowMenu.bind('<Enter>', lambda event, lab=self.__lShowMenu: self.__hoverMenuE(lab))
        self.__lShowMenu.bind('<Leave>', lambda event, lab=self.__lShowMenu: self.__hoverMenuL(lab))

        self.__fMenu.place(width=250, height=self.__size['h'])

    def __showMenu(self):
        # self.__hide = False
        if self.__posMenu == -250:
            self.__lShowMenu.place_forget()
        if self.__posMenu < 0:
            self.__posMenu = -int(250 * np.exp(-self.__x))
            self.__x += self.__v
            # print(n)
            self.__fMenu.place(anchor=tk.NW, width=250, height=self.__size['h'], x=self.__posMenu)
            self.__root.after(10, self.__showMenu)
        else:
            self.__x = 0

    def __hideMenu(self):
        # self.__hide = False
        if self.__posMenu == -250:
            self.__lShowMenu.place_forget()
        if self.__posMenu > -250:
            self.__posMenu = int(250 * np.exp(-self.__x))-250
            self.__x += self.__v
            # print(self.__posMenu)
            self.__fMenu.place(anchor=tk.NW, width=250, height=self.__size['h'], x=self.__posMenu)
            self.__root.after(10, self.__hideMenu)
        else:
            self.__x = 0
            self.__lShowMenu.place(anchor=tk.SW, x=10, y=self.__size['h'] - 20)

    def __hoverMenuE(self, widget):
        widget.config(font=self.font(20))

    def __hoverMenuL(self, widget):
        widget.config(font=self.font(16))

    def __acceuil(self):
        self.__hideMenu()
        for widget in self.__fMain.winfo_children():
            widget.destroy()

        tk.Label(self.__fMain, text="Acceuil", background=self.__color['bg1'], font=self.font(16)).grid(column=0, row=0)

    def __personnages(self):
        self.__hideMenu()
        for widget in self.__fMain.winfo_children():
            widget.destroy()

        PagePerso(self, self.__fMain)

    def __lIle(self):
        self.__hideMenu()
        for widget in self.__fMain.winfo_children():
            widget.destroy()

        tk.Label(self.__fMain, text="L'ile", background=self.__color['bg1'], font=self.font(16)).grid(column=0, row=0)

    def __galerie(self):
        self.__hideMenu()
        for widget in self.__fMain.winfo_children():
            widget.destroy()

        tk.Label(self.__fMain, text="Galerie", background=self.__color['bg1'], font=self.font(16)).grid(column=0, row=0)

    def __aide(self):
        self.__hideMenu()
        for widget in self.__fMain.winfo_children():
            widget.destroy()

        tk.Label(self.__fMain, text="Aide", background=self.__color['bg1'], font=self.font(16)).grid(column=0, row=0)

    def __favoris(self):
        self.__hideMenu()
        for widget in self.__fMain.winfo_children():
            widget.destroy()

        tk.Label(self.__fMain, text="Favoris", background=self.__color['bg1'], font=self.font(16)).grid(column=0, row=0)

    def __options(self):
        self.__hideMenu()
        for widget in self.__fMain.winfo_children():
            widget.destroy()

        tk.Label(self.__fMain, text="Options", background=self.__color['bg1'], font=self.font(16)).grid(column=0, row=0)
        self.__cFont = ttk.Combobox(self.__fMain, values=self.__fonts)
        self.__cFont.current(self.__fonts.index(self.__font))
        self.__cFont.grid(column=0, row=1)

        tk.Button(self.__fMain, text="Save", command=self.__reload).grid(column=0, row=2)
        # tk.Button(self.__fMain, text="update", command=self.__updateCheck).grid(column=0, row=3)

    def __reload(self):
        for widget in self.__fMenu.winfo_children():
            widget.destroy()
        self.__fMenu.destroy()
        self.__lShowMenu.destroy()

        self.__font = self.__cFont.get()
        self.__menu()

    def __test(self, txt):
        for widget in self.__fMain.winfo_children():
            widget.destroy()

        tk.Label(self.__fMain, text=txt, background=self.__color['bg1']).grid(column=0, row=0)

    def __updateCheck(self):
        newestVersion = rqst.get('https://raw.github.com/Andy-F18/SMLM/main/release/version.txt').text
        if newestVersion > self.__version:
            rep = rqst.get('https://raw.github.com/Andy-F18/SMLM/main/release/smlm.exe')
            with open('smlm.exe', 'wb') as hdl:
                for data in rep.iter_content():
                    hdl.write(data)

            os.startfile(os.path.abspath(".")+'/smlm.exe')
            self.__root.quit()

    def color(self, color):
        return self.__color[color]


if __name__ == '__main__':
    SMLM()