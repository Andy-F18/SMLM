import os
import github as gh
import requests as rqst
import tkinter as tk


def smlmInstallerCheck():
    dirList = ["config",
               "data"]

    ok = True
    for d in dirList:
        if not os.path.exists(d):
            ok = False

    return ok


def smlmInstaller(instWin: tk.Tk):
    dirList = ["config",
               "data"]
    lFiles = tk.StringVar()
    tk.Label(instWin, textvariable=lFiles).pack(padx=5, pady=5)

    g = gh.Github()
    repo = g.get_repo("Andy-F18/SMLM")
    content = []
    for d in dirList:
        os.mkdir(d)
        lFiles.set(d)
        content.extend(repo.get_contents(d))
        instWin.update()

    while content:
        file = content.pop(0)
        lFiles.set(file.path)
        instWin.update()
        print(file.path)
        if file.type == "dir":
            content.extend(repo.get_contents(file.path))
            os.mkdir(file.path)
        else:
            rep = rqst.get('https://raw.github.com/Andy-F18/SMLM/main/'+file.path)
            print("bruh")
            with open(file.path, 'wb') as hdl:
                for data in rep.iter_content():
                    hdl.write(data)

    instWin.destroy()