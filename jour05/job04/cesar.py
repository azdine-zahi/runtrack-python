def chiffrement_cesar(message, decalage):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    message_chiffre = ""
    for lettre in message:
        lettre_chiffree = alphabet[(alphabet.index(lettre) + decalage) % 26]
        message_chiffre += lettre_chiffree
    return message_chiffre

print(chiffrement_cesar("xyz",3))