import tkinter as tk
from PIL import Image, ImageTk


class PagePerso:
    def __init__(self, root, master):
        self.__root = root
        self.__fMain = master

        self.__confPage()

        self.__menu()
        self.__stats()
        self.__perso()
        self.__inventaire()

    def __confPage(self):
        self.__fMain.grid_rowconfigure(1, weight=1)
        self.__fMain.grid_columnconfigure(0, weight=1)

        self.__fContent = tk.Frame(self.__fMain, background=self.__root.color('bg1'))
        self.__fContent.grid_columnconfigure(0, weight=1)
        self.__fContent.grid_columnconfigure(1, weight=2)
        self.__fContent.grid_columnconfigure(2, weight=7)
        self.__fContent.grid_columnconfigure(3, weight=2)
        self.__fContent.grid_columnconfigure(4, weight=1)
        self.__fContent.grid_rowconfigure(0, weight=1)
        self.__fContent.grid(column=0, row=1, sticky=tk.NSEW)

    def __menu(self):

        self.__fMenuP = tk.Frame(self.__fMain, background=self.__root.color('bg2'))
        self.__fMenuP.grid_columnconfigure(0, weight=1)
        self.__fMenuP.grid_columnconfigure(1, weight=1)
        self.__fMenuP.grid_columnconfigure(2, weight=1)

        o = tk.LabelFrame(self.__fMenuP, background=self.__root.color('bg2'))
        tk.Label(o, text="A", background=self.__root.color('bg2'), font=self.__root.font(16)).grid(column=0, row=0)
        o.grid(column=0, row=0, sticky=tk.NSEW)

        o = tk.LabelFrame(self.__fMenuP, background=self.__root.color('bg2'))
        tk.Label(o, text="B", background=self.__root.color('bg2'), font=self.__root.font(16)).grid(column=0, row=0)
        o.grid(column=1, row=0, sticky=tk.NSEW)

        o = tk.LabelFrame(self.__fMenuP, background=self.__root.color('bg2'))
        tk.Label(o, text="C", background=self.__root.color('bg2'), font=self.__root.font(16)).grid(column=0, row=0)
        o.grid(column=2, row=0, sticky=tk.NSEW)

        self.__fMenuP.grid(column=0, row=0, sticky=tk.EW)

    def __stats(self):
        fStats = tk.Frame(self.__fContent, background=self.__root.color('bg1'))
        fStats.grid_rowconfigure(0, weight=1)
        fStats.grid_rowconfigure(1, weight=5)
        fStats.grid_rowconfigure(2, weight=1)
        fStats.grid_rowconfigure(3, weight=3)
        fStats.grid_rowconfigure(4, weight=1)
        fStats.grid_columnconfigure(0, weight=1)

        tk.Label(fStats, text="Stats", background=self.__root.color('bg1'), font=self.__root.font(24))\
            .grid(column=0, row=0)
        fStatsA = tk.LabelFrame(fStats, background=self.__root.color('bg2'))
        fStatsA.grid(column=0, row=1, sticky=tk.NSEW)

        tk.Label(fStats, text='(dé)Buff', background=self.__root.color('bg1'), font=self.__root.font(24))\
            .grid(column=0, row=2)
        fStatsB = tk.LabelFrame(fStats, background=self.__root.color('bg2'))
        fStatsB.grid(column=0, row=3, sticky=tk.NSEW)

        fStats.grid(column=1, row=0, sticky=tk.NSEW)

    def __perso(self):
        fPerso = tk.Frame(self.__fContent, background=self.__root.color('bg1'))
        fPerso.grid_rowconfigure(0, weight=1)
        fPerso.grid_rowconfigure(1, weight=10)
        fPerso.grid_rowconfigure(2, weight=1)
        fPerso.grid_columnconfigure(0, weight=1)

        tk.Label(fPerso, text='Nom du perso', background=self.__root.color('bg1'), font=self.__root.font(20))\
            .grid(column=0, row=0)

        can = tk.Canvas(fPerso, background=self.__root.color('bg1'), highlightthickness=0, width=500, height=700)

        img = Image.open("data/Personnages/djovn.png")
        img = img.resize(size=(500, int(500/img.width*img.height)))
        can.img = ImageTk.PhotoImage(img)

        can.create_image(250, 0, anchor=tk.N, image=can.img)
        can.grid(column=0, row=1)

        fPerso.grid(column=2, row=0, sticky=tk.NSEW)

    def __inventaire(self):
        fInv = tk.Frame(self.__fContent, background=self.__root.color('bg1'))
        fInv.grid_rowconfigure(0, weight=1)
        fInv.grid_rowconfigure(1, weight=4)
        fInv.grid_rowconfigure(4, weight=5)
        fInv.grid_columnconfigure(0, weight=1)

        tk.Label(fInv, text="Inventaire", background=self.__root.color('bg1'), font=self.__root.font(24))\
            .grid(column=0, row=0)
        fInvA = tk.LabelFrame(fInv, background=self.__root.color('bg2'))
        for x in range(0, 3):
            fInvA.grid_columnconfigure(x, weight=1)
        for y in range(0, 3):
            fInvA.grid_rowconfigure(y, weight=1)
        fInvA.grid(column=0, row=1, sticky=tk.NSEW)

        for y in range(0, 3):
            for x in range(0, 3):
                tk.LabelFrame(fInvA, background=self.__root.color('bg2')).grid(column=x, row=y, sticky=tk.NSEW)

        fInv.grid(column=3, row=0, sticky=tk.NSEW)