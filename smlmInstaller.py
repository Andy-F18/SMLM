import os
import github as gh
import requests as rqst


def smlmInstaller():
    dirList = ["config",
               "data"]

    ok = True
    for d in dirList:
        if not os.path.exists(d):
            ok = False

    if not ok:
        g = gh.Github()
        repo = g.get_repo("Andy-F18/SMLM")
        content = repo.get_contents("")
        while content:
            file = content.pop(0)
            for d in dirList:
                if file.path.find(d) != -1:
                    print(file.path)
                    if file.type == "dir":
                        content.extend(repo.get_contents(file.path))
                        os.mkdir(file.path)
                    else:
                        rep = rqst.get('https://raw.github.com/Andy-F18/SMLM/'+file.path)
                        with open(file.path, 'wb') as hdl:
                            for data in rep.iter_content():
                                hdl.write(data)
