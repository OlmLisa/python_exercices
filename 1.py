from math import sqrt
## Exercice 1
##temps = 6.892
##distance = 19.7
##vitesse = distance / temps
##print("vitesse=", vitesse)
##print("vitesse = {:.2f} m/s". format(vitesse))
      

## Exercice 2
##nom = input("Votre nom : ")
##age = float(input ("age :"))
##print ("Nom : ", nom)
##print ("Age : ", age)

## Exercice 3
##i = float(input("Votre flottant : "))
##if (i < 0 ):
##    print("Erreur le flottant doit être >=0.")
##else:
##    y= sqrt(i)
##    print("La racine de", i, "est", y)
##print("Au revoir.")

## Exercice 4
mot1 = input("Votre mot1 : ")
mot2 = input ("Votre mot2 : ")
l1 = len(mot1)
l2 = len(mot2)
if(l1 > l2):
    print ("Le plus petit est", mot2)
else:
    print ("Le plus petit est", mot1)

