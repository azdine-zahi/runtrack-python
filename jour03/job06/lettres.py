chaine = "abcdefghijklmnopqrstuvwxyz" * 10
longueur_de_chaine = len(chaine)
line = 1
i = 0
while i + line <= longueur_de_chaine:
  print(chaine[i:i+line])
  i += line
  line += 1