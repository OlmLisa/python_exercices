#!/usr/bin/python
# encoding: utf-8
#-------------------------------------------------------------------------------
# Name:        module Python
# Purpose:     TP sécurité : attaques par dictionnaires
#
# Author: Lisa OULMI, 3A IBC
#
# Created:     10/04/2020
# Copyright:   (c) Loulmi2020
 
#-------------------------------------------------------------------------------
## importation des librairies
import csv
import hashlib
import random
import os

### Utilsation du fichier.csv fourni par le professeur
### Récupérer la liste des prénoms, la liste des noms et la liste des password hashés

f=open('liste.csv')
fichierCSV=csv.reader(f, delimiter=";")
prenom = []
nom = []
password = []
## ajout des données respcetives dans les 3 listes
for ligne in fichierCSV:
    prenom.append(ligne[0])
    nom.append(ligne[1])
    password.append(ligne[2])

### test d'affichage des contenus des 3 listes
#print(prenom)
#print(nom)
#print(password)
#####################

## déclaration des fonctions pour différentes technique d'attaque par dictionnaire
    
def technique_nom_chiffre(nom, password): 
    test = 0
    ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range (0, len(ascii_letters)):
        lettre = ascii_letters[i]
        for date in range(1920,2000):
            new_date = str(date)
            new_nom = lettre+nom+new_date
            new_password = hashlib.md5(new_nom.encode()).hexdigest()
            if (new_password in password):
                print(new_password)
                print ("OK technique non chiffre")
                return new_password

def technique_nom(nom, password): 
   for i in range(0, 500):
       new_nom = nom
       new_nom = nom+str(i)
       print(new_nom)
       new_password = hashlib.md5(new_nom.encode()).hexdigest()
       if (new_password in password):
           print ("OK prenom sans rien")
           print(new_password)
           return new_password

 ###################################################           
def technique_prenom_voyelles(prenom, password):
    for nb in range(1000, 1500): # test divers ranges
        new_nom = prenom
        for lettre in prenom:
            if lettre in "AEIOUYaeéiouy":
                new_nom = new_nom.replace(lettre, str(nb))
        #print(new_nom)             
        new_password = hashlib.md5((new_nom.upper()).encode()).hexdigest()
          
        if (new_password in password):
            print ("OK nom voyelles")
            print("voila",new_password)
            return new_password
                        
def technique_prenom(nom, password):
    for i in range(0, 500):
        new_nom = nom
        new_nom = nom+str(i)
        new_password = hashlib.md5(new_nom.encode()).hexdigest()
        if (new_password in password):
            print ("OK prenom sans rien")
            print(new_password)
            return new_password
        
########################Test #####################
##for name in nom:
##    resultat = technique_nom_chiffre(name.lower(), password)
##    technique_nom(name, password)

########################################
##print(prenom)
##print()
##print(password)
##for firstname in prenom:
##    resultat = technique_prenom_voyelles(firstname, password)
##    #print("=================> voici le résultat",resultat)
##    technique_prenom(firstname, password)
##f.close()

##########################################

def technique_animaux(animal):
    liste_nb = [1,2,3,4,5,6,7,8,9]
    x = random.sample(liste_nb,3)
    print(x,animal,x)
##        print (
##        lettre = ascii_letters[i]
##        for date in range(1920,2000):
##            new_date = str(date)
##            new_nom = lettre+nom+new_date
##            new_password = hashlib.md5(new_nom.encode()).hexdigest();
##            if (new_password in password):
##                print ("OK")
##                print(new_password)
##                return new_password

def animaux(animal, password):
    new_animal= animal[::-1]
    new_animal_concat = new_animal+animal
    new_password = hashlib.md5(new_animal_concat.encode()).hexdigest();
    if (new_password in password):
        print ("OK animaux")
        print(new_password)
        return new_password
##fichier = open("dico_animaux.txt", mode="r",encoding="utf-8")
##for ligne in fichier:
##    animal = ligne[:-1]
##    resultat = animaux(animal, password)
##fichier.close()

### Affichage du Menu pour l'utilisateur attaquant
def Menu():
    titre = "**************\n*****MENU*****\n"
    print(titre)
    print("1-Technique_nom_chiffre")
    print("2-Technique_prenom_voyelles")
    print("3-Technique_animaux")
    print("4-Technique_prenom")
    print("5-Technique_nom")
    print("0-Quitter\n")

####    Menu pour le choix de la technique d'attaque
def SuperMenu():
    while True:
        ##os.system('cls' if os.name=='nt' else 'clear')
        Menu()  ### affichage du menu pou rappel
        choix = input("Tapez votre choix:") #Attente du choix de l'utilisateur
        if choix == "0":
            break
        elif choix == "1":
             for name in nom:
                resultat = technique_nom_chiffre(name.lower(), password)
                 
        elif choix == "2":
            for firstname in prenom:
                resultat = technique_prenom_voyelles(firstname, password)

        elif choix == "3":
            fichier = open("dico_animaux.txt", mode="r",encoding="utf-8")
            for ligne in fichier:
                animal = ligne[:-1]
                resultat = animaux(animal, password)
            fichier.close()
             
        elif choix == "4":
            for firstname in prenom:
                resultat = technique_prenom(firstname, password)
                    
        elif choix == "5":
            for firstname in prenom:
                resultat = technique_nom(firstname, password) 
        else:
            print("Entree invalide\n")

 ### Appel fonction Menu pou le choix de la technique
SuperMenu()




    
