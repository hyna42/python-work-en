###### EP11 - FONCTION ######

# (1) définition fonctiuon
def print_menu():
    print("------MENU PRINCIPAL------")
    print("1.Effectuer une commande")
    print("2.Annuler une commande")
    print("3. Afficher l'aide")
    print("4.Quitter")

print_menu()

# (2) fonction avec paramètre obligatoire

def says(author, message):
    print(author, ":", message)

says("Amadou","hello world")
says("Baye","dieuredieufé Niass")

# (3) fonction avec paramètre optionnels
def create_player(name,level=1):
    print(name, "de niveau",level)

create_player("Chuck",7)
create_player("Daddy")

# (4) fonction renvoyant un résultat
def sum_integer(a,b):
    return a + b
result = sum_integer(4,8)
print(type(result))
print(result)

# (5) fonction anonyme
double = lambda n : n*2
print(double(2))
