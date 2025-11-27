###### BOUCLES ######

#.1 while
"""
break -> sort de la boucle
continue -> relancer tout de suite une itération (ne pas exécuter la suite)

"""
i=0
while i < 5:
    # if i==3:
    #     continue
    print("hello",i+1,"time")
    i+=1
else:
    print("fin de la boucle") #while can use else , execute at end when false

#2. for
name = "Baye"
for n in name:
    print(n)