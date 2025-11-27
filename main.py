###### EP12 - MODULES ######

# (1) module : cest un fichier .py (exemple main.py est un module)

"""
 import module_name ==> importe tout le module
    use : module_name.paquet

 from module_name import paquet
"""
  
# import something 
from something import say_hello , get_max_number
from something import return_sum_of_two_numbers as sum

say_hello()
print(get_max_number(4,8))
print("sum:",sum(4,6))

if __name__ == '__main__':
    print("Je suis dans main")


# (2) paquet : c'est un dossier contenant 1 fichier __init__.py et un et modules (.py files): exemple => paquet /calcul