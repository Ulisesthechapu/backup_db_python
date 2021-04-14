import patoolib
import os
import glob
import os.path
from os import path

basepath = "C:\Respaldo\Mar21/"
myfiles = [f for f in glob.glob(basepath + "*.bak")]
listfinal = []

for f in myfiles:
    x = f.find("Mar_")
    if x > 0 :
        f = f.upper()
        fx = f.replace(".BAK",".RAR")
        if path.exists(fx) == False :
            listfinal.append(f)

for t in listfinal:
    t = t.upper()
    fx = t.replace(".BAK",".RAR")
    print(t)
    patoolib.create_archive(fx,(t,))
    patoolib.test_archive(fx, verbosity=1)