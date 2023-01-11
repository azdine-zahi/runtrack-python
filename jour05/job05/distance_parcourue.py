def distance_parcourue(nombre_marches, hauteur_marche):
    distance_aller_retour = 2 * nombre_marches * hauteur_marche / 100
    distance_par_jour = distance_aller_retour * 5
    distance_par_semaine = distance_par_jour * 7
    return distance_par_semaine

nombre_marches = 10
hauteur_marche = 20
resultat = distance_parcourue(nombre_marches, hauteur_marche)
print(f"Pour {nombre_marches} marches de {hauteur_marche} cm, le gardien parcours {resultat:.2f} m par semaine.")