def nature_triangle(a, b, c):
    longueur_max=max(a, b, c):

    if longueur_max==a and b + c > a or longueur_max==b and a + c > b or longueur_max==c and a + b > c
        if (a == b == c):
            print("ce triangle est équilatéral")

        elif (a == b != c or b == c != a or a == c != b):
            print("Ce triangle est isocèle")
        
        elif (a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2):
            print("Ce triangle est rectangle")
        
        elif a**2 + b**2 == c**2 and a == b != c or b**2 + c**2 == a**2 and b == c != a or a**2 + c**2 == b**2 and a == c != b:
            print("Ce triangle est rectangle et isocèle")

        else:
            print("Ce triangle est quelconque")

    else:
        print(" le triangle n'est pas constructible")



nature_triangle(6, 6, 6)
nature_triangle(3, 3, 6)
nature_triangle(3, 4, 5)
nature_triangle(5, 5, 7.07107)
nature_triangle(2, 5, 6)
nature_triangle(3, 4, 9)

