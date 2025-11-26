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