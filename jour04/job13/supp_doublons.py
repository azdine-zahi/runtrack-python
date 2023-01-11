def supp_doublons(my_list):
    # Créer un set pour stocker les éléments uniques
    unique_set = set()
    # Itérer sur la liste et ajouter les éléments uniques dans le set
    for item in my_list:
        unique_set.add(item)
    # Convertir le set en liste et la renvoyer
    return list(unique_set)

# Exemple d'utilisation
my_list = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
print(supp_doublons(my_list))  
# Affiche : [40, 10, 80, 50, 20, 60, 30]