###### EP15 - Chaines de caractères ######
from datetime import datetime
#str : séquentiel, immuable, indexable,itérable

## I. INTRO
# (1)opérateurs : +, *, in

# (2) affichage [<début>:<fin>:<pas>]
s ="Baye Niass"
print(s[::2])
print(s[::-1]) #invrser chaine de caractère

# (3) quelques fonction natives : len, max,min

# (4) méthodes de séquence <sequence>.index()  <sequence>.count()

## II. FORMATAGE :f-string f""
print(f"Ma Beugue {s}")


now = datetime.now()
print(f"{now:%d-%m-%Y}")
print("*" *100)

print(f"Je m'appelle {s.upper()}")

pi = 314159
number = 42
print(f"Le nombre pi arrondi  à 2 décimales est : {number:>10}")

"""
    Les f-string permettent d'ajouter des variables et des expressions dans des chaines de caractères, ils permettent également des des formattage avancées tels que : 
    
    * arrondir des flottants à un certain décimal avec le spécificatern :.2f
    * ajouter des sépaateur de miliers avec :,
    * remplissage de nombre avec des zero exempel :04 (4 nombre)
    * fromatage de pourcentage : :.1% (1 chiffre après la virgule)
    * alignement et largeur minimale : < (gauche), > (droite), ^ (centre)
    * gestion des dates et des heures



"""