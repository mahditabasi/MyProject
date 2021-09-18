import numpy as np
import math
p = math.pi

m = int(input("Number of angeles: "))
z = int(input("closed traverse[1] open traverse[2] side adjusment[3] "))

if z == 1:
    angel = list(map(float, input("zavie ha: ").split(' ')[:m]))
    f_angel = ((np.sum(angel)) - ((2 * m) - 4) * 90)

    print(f_angel)

    c_angel = (-1 * f_angel) / m
    o = int(input("Number of couple: "))
    oo = int(input("Device error: "))
    ooo = (2.5 * oo * np.sqrt(len(angel) / oo))
    if f_angel <= ooo:
        angel2 = []
        for i in range(0,m):
            s = angel[i] + c_angel
            angel2.append(s)
        print(angel2)
    else:
        print('ERROR')

elif z == 2:
    angel = list(map(float, input("gizman ha: ").split(' ')[:m - 2]))
    gisement2 = list(map(float, input("zavie ha: ").split(' ')[:2]))
    f_angel = gisement2[0] - gisement2[1] + np.sum(angel) + (m * 180)

    print(f_angel)

    c_angel = (-1 * f_angel) / (m - 2)
    o = int(input("Number couple: "))
    oo = int(input("Device error: "))
    ooo = (2.5 * oo * np.sqrt(len(angel) / oo))
    if f_angel <= ooo:
        angel2 = []
        for i in range(0,m - 2):
            s = angel[i] + c_angel
            angel2.append(s)
        print(angel2)
    else:
        print("ERROR")

elif z == 3:
    side = list(map(float, input("The lengh of the sides: ").split(' ')[:m]))
    gisement1 = list(map(float, input("Gisements: ").split(' ')[:m]))
    gisement = []
    for i in range(0,m):
        x = np.deg2rad(gisement1[i])
        gisement.append(x)
    print(side)
    print(gisement)
    e = []
    for i in range(0,m):
        e1 = (side[i] * np.sin(gisement[i]))
        e.append(e1)
    n = []
    for i in range(0,m):
        n1 = side[i] * np.cos(gisement[i])
        n.append(n1)
    f_e = np.sum(e)
    f_n = np.sum(n)
    f = np.sqrt(np.power(f_e, 2) + np.power(f_n, 2))
    print(f)
    f_g = (np.arctan(f_e / f_n) * 180 / p)
    print(f_g)
    l = np.sum(side)
    print(l)
    error_r = f / l
    print(error_r)
    device_error = int(input("Device error fo angel: "))
    error_max = (2.5 * device_error) * (np.sqrt(2) / 4) * (np.sum(side)) * (np.sqrt(m / 2))
    if f <= error_max:
        xx = []
        yy = []
        for i in range(0,m):
            c_x = ((-1 * f_e) / l) * side[i]
            xx.append(c_x)
            c_y = ((-1 * f_n) / l) * side[i]
            yy.append(c_y)
        side_x = [1000]
        side_y = [1000]
        for j in range(0,m - 1):
            v = side_x[j] + e[j] + xx[j]
            side_x.append(v)
            vv = side_y[j] + n[j] + yy[j]
            side_y.append(vv)
        print(side_x)
        print(side_y)
    else:
         print("ERROR")