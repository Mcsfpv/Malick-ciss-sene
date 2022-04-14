#importation fonction aleatoire
import random
n = random.randint(0,10)

# jeux de deviner un nombre
def devinette():
    ''' permet de tester le programme en sachant le nombre choisi par le programmme
    print(n)   '''
    # initialisation du score
    score = 10

# entrer du nombre choisi par l utilisateur
    deviner = int (input("devinez le nombre choisi par l'ordinateur compris entre 0 a 10\n" ))
    
    while n != deviner:  
    # cas ou le nombre choisi par l utilisateur est plus petit
        if (n > deviner):
            score = score - 2
            print("\n------------------------------------")
            print(f"score:   {score}\n  ------------------------------------ reessayez")
            print("indice: vous avez donne un nombre plus petit " )
            print("\n------------------------------------")
            deviner = int(input("devinez le nombre choisi par l'ordinateur compris entre 0 a 10\n" ))
        
        # cas ou le nombre choisi par l utilisateur est plus grand
        elif(n < deviner) :
            score = score - 2
            print("\n------------------------------------")
            print(f"score:   {score}\n  + reessayez")
            print("indice: vous avez donne un nombre plus grand " )
            print("\n------------------------------------")
            deviner = int(input("devinez le nombre choisi par l'ordinateur compris entre 0 a 10\n" ))
        
        # cas l utilisateur a fait 5 tentative
        elif (score == 0):
            print("vous avez perdu ")
        else :
           break 
    print("bravo")



# programme de jeux pierre papier ciseaux
def ppc():
    print("bienvienue \n")
    print("\n------------------------------------")
    print("Le jeu du: Pierre - papier - Ciseaux")
    print("------------------------------------\n")
    
    score = 0
    deviner = None
    
    # combien de manche se deroule la parti
    r = int (input("En combien de tours se déroulera votre partie ?\n> "))
 
    #boucle par rapport au nombre r de la manche
    for turn in range(r):
        
        choix = random.randint(1,3)
        ''' permet de tester le programme en sachant le nombre choisi par le programmme
    print(n)   '''
        deviner = int (input("appuyez sur\n 1 pour pierre \n 2 pour papier \n 3 pour ciseaux\n" ))
        if (choix == deviner):
            print("\n------------------------------------")
            print(f" score =  {score}   \n vous etes a egalité")
            print("\n------------------------------------") 
        elif (choix == 1 and deviner == 2):
            score = score + 1
            print("\n------------------------------------")
            print(f" score =  {score}\n pas  mal \n papier gagne pierre")
            print("\n------------------------------------")
        elif (choix == 1 and deviner == 3):
            score = score - 1
            print("\n------------------------------------")
            print(f" score =  {score} \n dommage \n pierre gagne ciseaux")
            print("\n------------------------------------")
        elif (choix == 2 and deviner == 1):
            score = score - 1
            print("\n------------------------------------")
            print(f" score =  {score} \n dommage \n papier gagne pierre")
            print("\n------------------------------------")
        elif   (choix == 2 and deviner == 3):
            score = score + 1
            print("\n------------------------------------")
            print(f" score =  {score} \n  pas  mal \n ciseaux gagne papier ")
            print("\n------------------------------------")
        elif (choix == 3 and deviner == 1):
            score = score + 1
            print("\n------------------------------------")
            print(f" score =  {score} \n    pas  mal \n  pierre gange ciseaux")
            print("\n------------------------------------")
        elif (choix == 3 and deviner == 2):
            score = score - 1
            print("\n------------------------------------")
            print(f" score =  {score} \n   dommage  \n ciseaux gagne papier")
            print("\n------------------------------------")
        else:
            break
        
        

def main():
    print("bienvienue \n")
    print("\n------------------------------------")
    print("dans les  programme de jeux")
    print("------------------------------------\n")
    print("appuyer sur 1 \n")
    print("\n------------------------------------")
    print("jeux du: nombre")
    print("------------------------------------\n")
    print("appuyer sur 2 \n")
    print("\n------------------------------------")
    print("Le jeu du: Pierre - papier - Ciseaux")
    print("------------------------------------\n")
    # chois du jeux
    jeux = int (input("" ))
    if (jeux == 1):
        devinette()
    else:
        ppc()



main()   
       

