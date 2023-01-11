def test(nombre):
    if nombre > 0:
        print("positif")
    
    elif nombre < 0:
        print("negatif")

    else:
        print("c'est un zero")


    test(12)
    test(-18)
    test(0)