###### EP12 - MODULES ######


"""
# il existe 2 types d'erreurs en python : 
    1. Les erreurs (irrécupérables) : lors du développement : débogage
        -> sont gérées avec les ASSERTIONS , via le mot clé assert

    2. les erreurs d'exécution (valider les données utiliateurs, gérer les ressources). 
        -> on utilise le bloc de code `try except` pour englober le code qui peut etre la source de l'erreur

"""


# (1) - Erreurs irrecuperables
#Exemple d'assertion
def record_party(number_of_players):
    assert 0 < number_of_players <= 10, "Nombre de participants entre 0 et 10"
    print("Assertion de",number_of_players,"joueurs")

record_party(1)


# (2) Erreur d'éxécution
players_strength = 100
bonus =0
try:
    bonus = int(input("appliquer un bonus : "))
except Exception as err:
    print("Le bonus est incorect",type(err))
else:
    players_strength += bonus
finally:
    #lever une exception le le score dépasse 200, ensuite ramener le nb a 200
    if players_strength > 200:
        players_strength = 200
        raise ValueError("Niveau maximum de Force atteint.")
    print("FORCE :",players_strength)
