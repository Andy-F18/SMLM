import tkinter as tk
# from tkinter import font
import numpy as np
from PIL import Image, ImageTk
import yaml


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

        self.__size = {'h': self.__root.winfo_screenheight(), 'w': self.__root.winfo_screenwidth()}
        # self.__root.state('zoomed')
        self.__root.attributes("-fullscreen", True)
        self.__root.geometry(f"{self.__size['w']}x{self.__size['h']}")
        self.__root.config(background=self.__color['bg1'])

        self.__root.grid_columnconfigure(0, weight=1)
        self.__root.grid_rowconfigure(0, weight=1)

        self.__hide = False
        self.__menu()
        self.__v = 0.15
        self.__x = 0
        self.__posMenu = 0
        self.__lShow = tk.Label(self.__root, text=">>", background=self.__color['bg1'], font=self.__fonts['cal16'])
        self.__lShow.bind('<Button-1>', lambda event: self.__showMenu())
        self.__lShow.bind('<Enter>', lambda event, lab=self.__lShow: self.__hoverMenuE(lab))
        self.__lShow.bind('<Leave>', lambda event, lab=self.__lShow: self.__hoverMenuL(lab))

        self.__fMain = tk.Frame(self.__root, background=self.__color['bg1'])
        self.__fMain.grid(column=0, row=0)
        self.__acceuil()

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

        l = tk.Label(self.__fMenu, text="Acceuil", background=self.__color['them2'], font=self.__fonts['cal16'])
        l.bind("<Button-1>", lambda event: self.__acceuil())
        l.bind('<Enter>', lambda event, lab=l: self.__hoverMenuE(lab))
        l.bind('<Leave>', lambda event, lab=l: self.__hoverMenuL(lab))
        l.grid(column=0, row=1, sticky=tk.NSEW, padx=10)

        l = tk.Label(self.__fMenu, text="Personnages", background=self.__color['them2'], font=self.__fonts['cal16'])
        l.bind("<Button-1>", lambda event: self.__personnages())
        l.bind('<Enter>', lambda event, lab=l: self.__hoverMenuE(lab))
        l.bind('<Leave>', lambda event, lab=l: self.__hoverMenuL(lab))
        l.grid(column=0, row=2, sticky=tk.NSEW, padx=10)

        l = tk.Label(self.__fMenu, text="L'ile?", background=self.__color['them2'], font=self.__fonts['cal16'])
        l.bind("<Button-1>", lambda event: self.__lIle())
        l.bind('<Enter>', lambda event, lab=l: self.__hoverMenuE(lab))
        l.bind('<Leave>', lambda event, lab=l: self.__hoverMenuL(lab))
        l.grid(column=0, row=3, sticky=tk.NSEW, padx=10)

        l = tk.Label(self.__fMenu, text="Galerie", background=self.__color['them2'], font=self.__fonts['cal16'])
        l.bind("<Button-1>", lambda event: self.__galerie())
        l.bind('<Enter>', lambda event, lab=l: self.__hoverMenuE(lab))
        l.bind('<Leave>', lambda event, lab=l: self.__hoverMenuL(lab))
        l.grid(column=0, row=4, sticky=tk.NSEW, padx=10)

        l = tk.Label(self.__fMenu, text="Aide", background=self.__color['them2'], font=self.__fonts['cal16'])
        l.bind("<Button-1>", lambda event: self.__aide())
        l.bind('<Enter>', lambda event, lab=l: self.__hoverMenuE(lab))
        l.bind('<Leave>', lambda event, lab=l: self.__hoverMenuL(lab))
        l.grid(column=0, row=5, sticky=tk.NSEW, padx=10)

        l = tk.Label(self.__fMenu, text="Favoris", background=self.__color['them2'], font=self.__fonts['cal16'])
        l.bind("<Button-1>", lambda event: self.__favoris())
        l.bind('<Enter>', lambda event, lab=l: self.__hoverMenuE(lab))
        l.bind('<Leave>', lambda event, lab=l: self.__hoverMenuL(lab))
        l.grid(column=0, row=6, sticky=tk.NSEW, padx=10)

        l = tk.Label(self.__fMenu, text="Options", background=self.__color['them2'], font=self.__fonts['cal16'])
        l.bind("<Button-1>", lambda event: self.__options())
        l.bind('<Enter>', lambda event, lab=l: self.__hoverMenuE(lab))
        l.bind('<Leave>', lambda event, lab=l: self.__hoverMenuL(lab))
        l.grid(column=0, row=7, sticky=tk.NSEW, padx=10)

        l = tk.Label(self.__fMenu, text="Quitter", background=self.__color['them2'], font=self.__fonts['cal16'])
        l.bind("<Button-1>", lambda event: self.__root.quit())
        l.bind('<Enter>', lambda event, lab=l: self.__hoverMenuE(lab))
        l.bind('<Leave>', lambda event, lab=l: self.__hoverMenuL(lab))
        l.grid(column=0, row=8, sticky=tk.NSEW, padx=10)

        self.__lHideShowMenu = tk.Label(self.__fMenu, text="<<", background=self.__color['them2'],
                                        font=self.__fonts['cal16'])
        self.__lHideShowMenu.bind("<Button-1>", lambda event: self.__hideMenu())
        self.__lHideShowMenu.bind('<Enter>', lambda event, lab=self.__lHideShowMenu: self.__hoverMenuE(lab))
        self.__lHideShowMenu.bind('<Leave>', lambda event, lab=self.__lHideShowMenu: self.__hoverMenuL(lab))
        self.__lHideShowMenu.grid(column=0, row=9, sticky=tk.E, padx=10)

        self.__fMenu.place(width=250, height=self.__size['h'])

    def __showMenu(self):
        # self.__hide = False
        if self.__posMenu == -250:
            self.__lShow.place_forget()
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
            self.__lShow.place_forget()
        if self.__posMenu > -250:
            self.__posMenu = int(250 * np.exp(-self.__x))-250
            self.__x += self.__v
            # print(self.__posMenu)
            self.__fMenu.place(anchor=tk.NW, width=250, height=self.__size['h'], x=self.__posMenu)
            self.__root.after(10, self.__hideMenu)
        else:
            self.__x = 0
            self.__lShow.place(anchor=tk.SW, x=10, y=self.__size['h']-20)

    def __hoverMenuE(self, widget):
        widget.config(font=self.__fonts['cal20'])

    def __hoverMenuL(self, widget):
        widget.config(font=self.__fonts['cal16'])

    def __acceuil(self):
        for widget in self.__fMain.winfo_children():
            widget.destroy()

        tk.Label(self.__fMain, text="Acceuil", background=self.__color['bg1']).grid(column=0, row=0)

    def __personnages(self):
        for widget in self.__fMain.winfo_children():
            widget.destroy()

        tk.Label(self.__fMain, text="Personnages", background=self.__color['bg1']).grid(column=0, row=0)

    def __lIle(self):
        for widget in self.__fMain.winfo_children():
            widget.destroy()

        tk.Label(self.__fMain, text="L'ile", background=self.__color['bg1']).grid(column=0, row=0)

    def __galerie(self):
        for widget in self.__fMain.winfo_children():
            widget.destroy()

        tk.Label(self.__fMain, text="Galerie", background=self.__color['bg1']).grid(column=0, row=0)

    def __aide(self):
        for widget in self.__fMain.winfo_children():
            widget.destroy()

        tk.Label(self.__fMain, text="Aide", background=self.__color['bg1']).grid(column=0, row=0)

    def __favoris(self):
        for widget in self.__fMain.winfo_children():
            widget.destroy()

        tk.Label(self.__fMain, text="Favoris", background=self.__color['bg1']).grid(column=0, row=0)

    def __options(self):
        for widget in self.__fMain.winfo_children():
            widget.destroy()

        tk.Label(self.__fMain, text="Options", background=self.__color['bg1']).grid(column=0, row=0)

    def __test(self, txt):
        for widget in self.__fMain.winfo_children():
            widget.destroy()

        tk.Label(self.__fMain, text=txt, background=self.__color['bg1']).grid(column=0, row=0)


if __name__ == '__main__':
    SMLM()