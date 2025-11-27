###### EP12 - MODULES ######

# module - paquet

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