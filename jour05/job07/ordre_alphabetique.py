def next_alphabetical_word(word):
    # Convertir le mot à une liste de caractère
    word = list(word)
    # Trouvez le caractère le plus à droite qui peut être remplacé par une valeur supérieure
    for i in range(len(word) - 1, -1, -1):
        if ord(word[i]) < ord('z'):
            break
    else:
        # Si aucun caractère de ce type n'est trouvé, le mot est déjà le plus grand possible
        return word
    # Changer le caractère pour le suivant dans l'alphabet
    word[i] = chr(ord(word[i]) + 1)
    # Trier les caractères restants dans leur ordre alphabétique
    word[i+1:] = sorted(word[i+1:])
    return "".join(word)

# Example usage
original_word = input("Enter a word: ")
next_word = next_alphabetical_word(original_word)
print("The next word in alphabetical order is:", next_word)