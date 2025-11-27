###### EP15 - Chaines de caractères ######
import datetime
#str : séquentiel, immuable, indexable,itérable

## I. INTRO
# (1)opérateurs : +, *, in

# (2) affichage [<début>:<fin>:<pas>]
s ="Baye Niass"
print(s[::2])
print(s[::-1]) #invrser chaine de caractère

# (3) quelques fonction natives : len, max,min

# (4) méthodes de séquence <sequence>.index()  <sequence>.count()

## II. FORMATAGE
print(f"Ma Beugue {s}")

print("*" *50)

now = datetime.datetime.now()
print(f"{now:%d-%m-%Y}")
