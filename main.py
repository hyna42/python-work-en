###### EP14 - DECORATEURS ######
"""
    le décorateur @ va changer le comportement d'une fonction (la fonction décorée) sans modifier le comportement de celle-ci
"""
import sys
#Exemple 1
def logger(func):
    def wrapper(*args, **kwargs):
        print("Appel de la fonction",func.__name__)
        return func(*args, **kwargs)
    return wrapper


@logger
def hello():
    print("says hello")


@logger
def sum(a,b):
    return a + b


hello()
print(sum(1,3))


#Exemple 2
"""
    L'idée ici c'est de créer un décorateur qui limite le nombre de compression possible à n fois (pour les utilisateurs non-premium)
"""
def limit_use(max_uses=1):
    def decorateur(func):
        func.number_uses = 0

        def wrapper(*args,**kwargs):
            if func.number_uses >= max_uses:
                print("Limite atteinte en tant qu'utilisateur gratuit",file=sys.stderr)
                return None
            func.number_uses += 1
            return func(*args,**kwargs)
        return wrapper
    return decorateur




@limit_use(3)
def compress_pdf():
    print("Compression d'un document PDF ...")

def join_pdf():
    print("Fusion d'un document PDF ...")


for i in range(0,5):
    compress_pdf()
    join_pdf()
