# Duizelig6



i = 49
o = 1
o2 = 1
repeat = True
while repeat:
    print(str(o) + ' + ' + str(i) + ' + 1 = ' + str(o2))
    if o2 < 1000:
        o = o + i + 1
        o2 = o + i + 2
        i = i + 1
    elif o2 >= 1000:
        repeat = False
