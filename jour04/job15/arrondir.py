numbers = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

# arrondir les nombres à l'entier le plus proche
rounded_numbers = [round(num) for num in numbers]

# trier la liste dans l'ordre croissant
sorted_numbers = sorted(rounded_numbers)

print(sorted_numbers)