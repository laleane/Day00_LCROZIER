def nombre_caracteres(chaine):
    count = 0
    for _ in chaine:
        count += 1
    return count

# Exemple d'utilisation de la fonction
chaine = "Bonjour, monde!"
resultat = nombre_caracteres(chaine)
print("Nombre de caractères dans la chaîne :", resultat)
