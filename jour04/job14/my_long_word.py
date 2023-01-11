def long_mots(string, n):
    mots = string.split() # Split la string à travers la liste des mots
    
    length = 0
    for c in long_mots:
        length += 1
    long_mots = [word for word in mots if length > n] # garder le mot qui est plus long que n
    return long_mots

string = ("La peur est le chemin vers le côté obscur la peur mène à la colère la colère mène à la haine la haine mène à la souffrance”")
n = 3
print(long_mots(string, n))