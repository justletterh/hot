def read(fp):
    f=open(fp,"r")
    res=f.read()
    f.close()
    return res.strip()
