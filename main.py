###### CONDITIONS ######

#1. if-elif-else
access = True
access = 1



print("1" == 1)

if access:
    print("Vous pouvez passer")
else:
    print("Ohhhhh")


#2. match-case - depuis python 3.10
"""
    peut travailler sur des motifs
"""
role = "adminx"
match role:
    case "admin" | "user":
        print("can access site")
    case "visitor":
        print("can register")
    case _:
        print("Unknown status")

#exemple 2 :using motifs
# loto = [13, 45, 5, 1]
loto = [13, 45, 8, 26, 1]
match loto:
    case [13, 45, 8, 26, 3]:
        print("Vous avez gagné le gros lot !")
    case [13, 45, 8, n1, n2] if n1 > 10:
        print("Vous avons 3 numéros sur les 5")
    case _:
        print("Mort, mort mort...")   