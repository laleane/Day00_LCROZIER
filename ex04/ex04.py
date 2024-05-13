import random

def tri_croissant_sans_sort(tableau):
    # Boucle pour trier le tableau par ordre croissant
    for i in range(len(tableau)):
        for j in range(i+1, len(tableau)):
            if tableau[j] < tableau[i]:
                # Échanger les éléments si nécessaire
                tableau[i], tableau[j] = tableau[j], tableau[i]
    return tableau

# Génération d'un tableau d'entiers aléatoires avec plus de 15 indices
tableau = [random.randint(0, 100) for _ in range(20)]

# Affichage du tableau initial
print("Tableau initial :", tableau)

# Appel de la fonction pour trier le tableau par ordre croissant
tableau_trie = tri_croissant_sans_sort(tableau)

# Affichage du tableau trié
print("Tableau trié :", tableau_trie)