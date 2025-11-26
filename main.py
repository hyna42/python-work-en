print("Hello World!")
# print("Hello World!")
c = "hello"


###### DATA TYPE ######
print(type(c))
#1. id(<object>)
print("identifiant de c =>",id(c))


#2. type(<object>)
print(type(4))
print(type(4.0))
print(type('4'))
print(type((4,))) #immuable, virgule obligatoirsi un seul élémenet de tuple
print(type([4])) #mutable
print(type({4}))

#3. isInstance(<object>, <classInfo>)
print("test valeur de vérité : 4 === string ? ", isinstance(4,int))