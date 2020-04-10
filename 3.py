## OULMI LISA 3-A blockchain

## Exercice 15:
liste =[17, 38, 10, 25, 72]
liste.sort()
liste.append(12)
print(liste)
liste.reverse()
print(liste)
for i in range (0, len(liste)):
    nombre = liste[i]
    if nombre == 17:
        print(i)
print ("fin de la boucle")
liste.remove(38)
print (liste)
for i in range (2, 4):
    nombre = liste[i]
    print(nombre)
print ("fin de la sous-liste du 2e au 3e élément")
for i in range (0, 2):
    nombre = liste[i]
    print(nombre)
print ("fin de la sous-liste du début au 2e élément")
for i in range (3, len(liste)):
    nombre = liste[i]
    print(nombre)
print ("fin de la sous-liste du 3e à la fin de la liste")
print(liste)

## Exercice 16:
chaine = input("Votre chaine : ")
chaine_inverse = ""
for lettre in chaine:
   chaine_inverse = lettre + chaine_inverse 
print (chaine_inverse)

## Exercice 17: Palindrome

## Exercice 18:
email = input("Votre email : ")
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
if(re.search(regex,email)):  
    print("Email OK valide")  
else:  
    print("Email invalide")

## Exercice 19:
truc  = []
machin =[1.1, 1.2, 1.3, 1.4, 1.5]
if (len(truc) != 0):
    for i in range (0, len(truc)):
        nombre = truc[i]
        print(nombre)
    print ("fin de la boucle truc")
if (len(machin) != 0):
    for i in range (0, len(machin)):
        nombre = float(machin[i])
        print(nombre)
    print ("fin de la boucle machin")

## Exercice 20:
print([i for i in range(0,4)])
print([i for i in range(4,8)])
print([i+2 for i in range(2,9)])
chose =[0, 1, 2, 3, 4, 5]
print([i for i in range(0,len(chose)) if i==3 or i==6])
