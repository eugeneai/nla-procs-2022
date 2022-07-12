import glob

lf = glob.glob("*.tex")

BET = r"\begin{englishtitle}"
EET = r"\end{englishtitle}"


def proc(name, c):
    # c = c.replace("/r/n", "/n")
    #c = c.replace("/n/r", "/n")
    #ls = c.split("/n")

    #re = []

    betidx = c.find(BET)
    eetidx = c.find(EET)+len(EET)

    et = c[betidx:eetidx]

    cc = c[:betidx]+c[eetidx:]

    assert len(cc) > 0

    o = open(name, "w")
    o.write(et)
    o.write(cc)
    o.close()


for f in lf:
    c = open(f).read()
    if c.find(BET) >= 0:
        print(f)
        proc(f, c)
