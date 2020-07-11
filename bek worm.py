
print('welcome to the beklemishev worm game')
cl = [int(input('pick size of worm'))]
def clprinter(x):
    r1 = ''
    r2 = ''
    r3 = ''
    r4 = ''
    r5 = ''
    for i in x:
        r1 += "              _,.--.  "
        r2 += "      " + str(i) + "     .'`      -"
        r3 += ".'.       .'.'`  '``' "
        r4 += " '.`-...-'.'          "
        r5 += "   `-...-'            "
    print(r1)
    print(r2)
    print(r3)
    print(r4)
    print(r5)
def kfinder():
    RI = 0
    cp = len(cl)
    for i in range(0, len(cl)):
        cp -= 1
        if cl[cp] < cl[-1]:
            RI = 1
            return cp
            break
    if RI == 0:
        return 'n'
def next(m):
    global cl
    global g
    if cl[-1]:
        print('you lowered the worms tail by 1')
        if kfinder() == 'n':
            g = []
            b = cl[:(len(cl) - 1)]
            b.append(cl[-1] - 1)
            clprinter(b)
            print('it regenerated it`s body ' + str(m - 1) + ' times')
        else:
            g = cl[:(kfinder())]
            b = cl[(kfinder() + 1):(len(cl) - 1)]
            b.append(cl[-1] - 1)
            g += b
            clprinter(g)
            print('it regenerated a piece of it`s body ' + str(m - 1) + ' times')
        for i in range(0, m):
            g += b
        cl = g
    else:
        cl.pop()
        print('you cut of the worm`s 0 tail')
s = 1
step = 0
print('to do an attack on BEKLEMISHEV`S WORM, press enter')
clprinter(cl)
s += 1
while cl:
    if input() == '':
        step += 1
        next(s)
        clprinter(cl)
        s += 1
        print('to do next attack, press enter')
print(' ')
print('it took ' + str(step) + ' steps to kill BEKLEMISHEV`S WORM')
