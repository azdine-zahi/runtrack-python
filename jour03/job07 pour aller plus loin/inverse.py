def inverse_chaine(chaine):
    chaine_inverse = ""
    i = len(chaine) - 1
    while i >= 0:
        chaine_inverse =  chaine_inverse + chaine[i]
        i = i - 1
    return chaine_inverse
chaine = input("Veuillez saisir une phrase à inverser : ")
chaine_inverse = inverse_chaine(chaine)
print(chaine_inverse)