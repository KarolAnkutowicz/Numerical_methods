print("Mamy uklad dwoch rownan liniowych:")
print("a11*x +a12*y = b1")
print("a21*x +a22*y = b2")
print("Podaj kolejne wspolczynniki a ja podam Ci rozwiazanie :)")
a11 = float(input("a11 = "))
a12 = float(input("a12 = "))
a21 = float(input("a21 = "))
a22 = float(input("a22 = "))
b1 = float(input("b1 = "))
b2 = float(input("b2 = "))

W = a11 * a22 - a12 * a21
Wx = (b1 * a22) - (a12 * b2)
Wy = (a11 * b2) - (b1 * a21)
if W == 0 :
    if Wx == 0 and Wy == 0 :
        print("Uklad ma niekskonczenie wiele rozwiazan...")
    else :
        print("Uklad nie ma rozwiazan :(")
else :
    x = Wx / W
    y = Wy / W
    print("Rozwiazanie ukladu to")
    print("x =", x)
    print("y =", y)
