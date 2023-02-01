'''
x=int(input())
if x%2==0 :
    print ("pair")
else:
    print ("impair")
'''

'''                 ex7
x=int(input())
y=int(input())
z=int(input())

if x>y and x>z :
    print (x)
elif y>x and y>z :
    print (y)
elif z>x and z>y :
    print (z)
'''

'''
from math import * 
x=float(input("saisir votre rayon:"))

print(pi*x**2)
print(x*2*pi)
'''

'''
a=int(input("Entrez un nombre :"))
b=int(input("Entrez un nombre :"))
print(a//b, a%b)
'''

'''
x=0
for k in range(3,10) :
    x=x+1
print(x)
'''

'''
x=("*")
for i in range (1, 21) :
    t=i*7
    print(t)
    if t%3==0 :
        print("*")
'''

'''
x=("")
for i in range (1, 21) :
    t=i*7
    print(t)
    if t%3==0 :
        print("*")
'''

'''
t=1
for sqdsqdsqdsqdd in range (12) :
    t=t*3
    print(t, sqdsqdsqdsqdd)
'''

'''
k=input()
for k in str(k) :
    print(k)
'''

'''
from random import random, randint, randrange
x=randrange(10)
print("your guess?")
y=int(input())
for c in range (10):
    if y!=x :
        print("non, essayez encore")
        h=int(input())
    elif h==x :
        print("bingo")
'''

# ex1

'''
depose=1500
taux=0.015
scooter=1700
annees=0
while depose<scooter :
    depose=depose*(1+taux)
    annees=annees+1
print(annees)
'''

# ex1.2

'''
print("saisir la somme depose")
depose=int(input())
taux=0.015
print("saisir le nombre d'annees")
annees=int(input())
somme=depose*(1+taux)
print(somme)
'''

# ex1.3
'''
print("saisir la somme depose")
depose=int(input())
print("saisir le taux")
taux=float(input())
print("saisir le nombre d'annees")
annees=int(input())
somme=depose*(1+taux)
print(somme)
'''

# ex2
'''
papier=0.1
pli=0
while papier < 324000 :
    papier=papier*2
    pli=pli+1
print(pli)
'''

# Exercice 3

'''
from random import randrange
x=randrange(100)
#print(x)
print("your guess?")
y=int(input())
while True :
    if y>x :
        print("trop grand")
        y=int(input())
    elif y<x :
        print("trop petit")
        y=int(input())
    else :
        print("bingo")
        break
'''

'''
from random import randrange
x=randrange(100)
print(x)
print("your guess?")
y=int(input())
cptr=0
while True :
    cptr=cptr+1
    if y>x :
        print("trop grand")
        y=int(input())
    elif y<x :
        print("trop petit")
        y=int(input())
    else :
        print("bingo")
        print("vous avez fait", cptr, "essais")
        break
'''

'''
from random import randrange
x=randrange(100)
print(x)
min=1
max=100
guess=(min+max)//2
cptr=0
while x!=guess :
    cptr=cptr+1
    if guess>x:
        max=guess-1
    else:
        min=guess+1
    guess=(max+min)//2
print(guess)
print(cptr)
'''

'''
from random import randrange
x=randrange(100)
print(x)
min=1
max=100
cptr=0
cptr2=0
guess=(min+max)//2
print("ur guess?")
userguess=int(input())
while x!=guess :
    cptr=cptr+1
    if guess>x:
        max=guess-1
    else:
        min=guess+1
    guess=(max+min)//2

    cptr2=cptr2+1
    if userguess>x :
        print("trop grand")
        userguess=int(input())
    elif userguess<x :
        print("trop petit")
        userguess=int(input())
    elif cptr2>cptr:
        print("l'ordinateur a trouvé plus vite que vous")
        break
    elif userguess==x:
        print("bingo")
        print("vous avez fait", cptr2, "essais")
        break
print(guess, cptr)
'''

'''
n=int(input("entrez un nombre:"))
cpt=0
while n>0:
    n=n//10
    cpt=cpt+1
print(cpt)
'''

'''
for k in range(5, 0, -1) :
    for p in range (k, 0, -1) :
        print(p, end="")
    print()
'''

'''
for k in range(-10, 0):
    print(k)
'''

'''
n=int(input("Entrez un nombre \n"))
cpt=0
for k in range(1,n+1):
    if n%k==0:
        cpt+=1
if cpt==2:
    print(n, "est premier")
'''

'''
t=int(input("Entrez un nombre \n"))
for n in range(t):
    cpt=0
    for k in range(1,n+1):
        if n%k==0:
            cpt+=1
    if cpt==2:
        print(n, "est premier")
'''

'''
n = int(input("Entrez un nombre \n"))
p = 1
for k in range(1, n):
    p = p * k
print(p)
'''

'''
x=9
def fun(x) :
    x=x+4
    x=x*2
    x=x-5
    return x
print(fun(x))
'''
'''
x=9
def fun(x) :
    x=x+4
    x=x*2
    x=x-5
    print(x)
    return x
fun(x)
'''

'''
def carre(x) :
    return x*x
carre(2)
print(carre(15))
'''

'''
def coucou() :
    print("Bonjour, ça va ?")
coucou()
'''

'''
x=input("Votre nom?\n")
def prenom(x):
    print("Bonjour, "+x)
prenom(x)
'''

'''
def TestSiVoyelle(UneVoyelleOuPas):
    if UneVoyelleOuPas=="a" or UneVoyelleOuPas=="o" or UneVoyelleOuPas=="u" or UneVoyelleOuPas=="e" or UneVoyelleOuPas=="i" or UneVoyelleOuPas=="y":
        return True
    else :
        return False


def compteurVoyelle(chainedecarac) :
    cptr=0
    cptr2=0
    for UneVoyelleOuPas in chainedecarac:
        if TestSiVoyelle(UneVoyelleOuPas):
            cptr+=1
        else :
            cptr2+=1
    return cptr, cptr2

print(compteurVoyelle("aaaayyynnnbnbnbnbnbnb"))
print(compteurVoyelle("aaaayyynnnbnbnbnbnbnb"))
'''

'''
def pallindrome():
    mot = input("votre mot")
    n = len(mot)
    for k in range (n//2) :
        if mot[k]==mot[n-k-1] :
            return "Pallandrome"
        else :
            return "Pas pallandrome"
'''
'''
L5=[5,9,3,8,1,6,5,7,9,4,2]
print(L5)
L5[2:6]=[4]
print(L5)
'''

'''
L6=["cc", "dd", "bb", "a",]
print(L6)
L6.sort()
L6.reverse()
print(L6)
'''

'''
x=input("rentrez votre texte :")
y=x.split()
L1=y
print(L1)

for k in L1:
    if k[0]=="a" :
        print(k)
'''

'''
L1=[1,5,6,9,7,5,1,3]
sum=(L1)
print(sum)
'''

'''
V=[1, 2, 3, 4, 5, 9, 5, 2, 2, 2, 2, 2]
T=[]
for k in V:
    if k not in T:
        T.append(k)
        print(k)
'''

# ex X

'''
T=[]
V=[1, 2, 3, 4, 5, 9, 5, 2, 2, 2, 2, 2]
J=[]
for k in V:
    for i in T:
        if k==i and k not in J:
            J.append(k)

'''

# EXERCICE1

'''
words = ["chat", "chien", "souris",
"oiseau"]
for k in words :
    print(k)
'''

# EXERCICE2
'''
cptr=0
while cptr <= 10 :
    print(cptr)
    cptr=cptr+1
    if cptr==10:
        print("stop")
        break
'''

'''
shopping_list=[]
print("""Utilisez ces mots pour faire des modifications :\n
placement : pour choisir l'emplacement de votre mot
remove : pour enlever un mot de la liste
pop : pour enlever le dernier mot dans la liste
sort : trier ce liste en ordre alphabetique
reversesort : inverser l'ordre\n""")
while True :
    k=input("entrez vos mots: \t")
    if k == "done" :
        break
    elif k == "placement" :
        print(shopping_list)
        k=int(input("ou vous voulez l'inserer? (entrez un nombre)\n"))
        p=input("votre mot? \n")
        shopping_list.insert(k, p)
    elif k == "remove" :
        k = input("vous voulez supprimer quel mot? \n")
        if k in shopping_list :
            shopping_list.remove(k)
    elif k == "pop" :
        print("vous avez retiré le dernier élement \n"+k)
        shopping_list.pop()
    elif k == "sort" :
        print("Vous avez trié ce liste en ordre alphabetique \n")
        shopping_list.sort()
    elif k == "reversesort" :
        print("Vous avez inversé l'ordre \n")
        shopping_list.reverse()
    else :
        shopping_list.append(k)
    for z in shopping_list :
        print(z)
'''

# EX1

'''
liste=[]
while True :
    k=input("entrez vos mots: \t")
    if k == "done" :
        break
    elif k == "reverse" :
        liste.reverse()
    else :
        liste.append(k)
    for z in liste :
        print(z)
'''

# EX3

'''
liste=[]
liste2=[]
while True :
    
    k=input("entrez vos prenoms: \t")
    
    if k == "done" :
        break
    else :
        liste.append(k)

for mot in liste :
    if len(mot) >= 5 and mot[0]=="a" :
        liste2.append(mot)
        print(liste2)
'''

# EX4


'''
liste=[]

liste2=[]

while True :
    
    k=int(input("entrez vos chiffres: \t"))
    
    if k == 0 :

        break

    else :

        liste.append(k)

somme=0

for nombre in liste :

    if nombre%2 == 0 :
    
        somme=somme+nombre
    
        print(somme)
'''

# EX5


'''
liste=[]

liste2=[]


while True :
    
    k=input("entrez vos mots: \t")
    if k == "done" :
        break
    else :
        liste.append(k)

for mot in liste :

    if liste.count(mot) > 1 and mot not in liste2 :

        liste2.append(mot)

        print(liste2)
'''

'''
liste=[]
liste2=[]

while True :
    
    k=int(input("entrez vos mots: \t"))
    if k == "0" :
        break
    else :
        liste.append(k)
liste.sort()

for k in range (len(liste)-1) :
    dif = abs(liste[k]-liste[k+1])
    liste2.append(dif)
    max(liste2)
'''

# PENDU

'''
while True :
    for x in r :
        x=input("entrez votre lettre : ")
        if x in r :
            print("oui")
        else :
            print("non")
'''

# MA VARSION

'''
import random
r=["chat", "chien", "lion", "souris", "koala", "cochon", "cheval"]
c=random.choice(r)
print(c)
while True :
    x=input("entrez votre lettre : ")
    if x == c :
        print("gagné")
        break
    if x in c :
        print(x+" est present dans ce mot")
        print(x)
    else :
        print(x+" n'est est present dans ce mot")
'''

# Correction

'''
import random
L = ["chat", "chien", "lion", "souris", "koala", "cochon", "cheval"]
mot = random.choice(L)

c = len(mot)
t = 0
aff = ["_"]*len(mot)
trouv = ""
while True :
    n = input("entrez votre lettre : ")
    if n in mot :
        for i in range (len(mot)) :
            if mot[i] == n :
                aff[i]= n
                t+=1
        print(aff)
        print("Presente")
    else: 
        print("Non")
        c-=1
    
    if c == 0 :
        print("mort")
        break
    elif t == len(mot) :
        print("vous avez deviné")

'''

# version Tibo


'''
#Importation module random
import random

#Liste des mots
mots = ["sexe","bondage","sodomie","gangbang","bite","chatte","chibre","partouze","fétichiste","faciale","porno","stepmom",]

#Choix aléatoire
mot = random.choice(mots)

#Liste ok
ok = []

#Variable incorrectes
incorrectes = 0

#Mécanique du jeu
while True :
    etat = ""
    for lettre in mot:
        if lettre in ok :
            etat += lettre
        else :
            etat += "_"
    print(etat)
    
    
#Question
    devine = input("Trouve une lettre : ").lower()

#En cours de partie
    if devine in ok : 
        print("Tu as déjà tapé cette lettre")
    elif devine in mot :
        print("Bien joué")
        ok.append(devine)
    else : 
        print("Incorrecte")
        incorrectes +=1
    
#Vérification des lettres manquantes et fin de partie
    if "_" not in etat : 
        print("Bravo, vous avez gagné")
        break
   
    else: 
        if incorrectes == 10:
            print("Perdu, le mot était :", mot +".")
            break
'''

'''
liste_prenoms = ["Alexandre","Amandine","Anna"]

print(liste_prenoms)


x=input("Entre le prenom que tu veux modifier : ")
y=input("Entre le prenom que tu veux : ")
for x in liste_prenoms :
    if x == "Anna" :
        liste_prenoms[-1] = y


print(liste_prenoms)
z=input("Rentrez les nouveaux prenom : ")
liste_prenoms.append(z)
liste_prenoms.insert(3,"Yvette")
liste_prenoms.sort()
liste_prenoms[1:3]
print(liste_prenoms)
liste_prenoms[0:2]=["Paul","Jacques"]
print(liste_prenoms)
print(len(liste_prenoms))
print(liste_prenoms[-1])
print(liste_prenoms[-3])
print(liste_prenoms)
liste_prenoms.append("Eléonore")
liste_prenoms.extend(["Audrey","Ophélie"])
print(liste_prenoms)
del liste_prenoms[1:3]
print(liste_prenoms)
liste_prenoms.pop(4)
print(liste_prenoms)
liste_prenoms.remove("Paul")
print(liste_prenoms)
liste_prenoms.clear()
print(liste_prenoms)

liste_garcons=["Alexandre","Alexis"]
liste_filles=["Delphine","Zoe"]
liste_prenoms=[liste_garcons,liste_filles]
print(liste_prenoms)
print(liste_prenoms[1])
print(liste_prenoms[1][0])
print(liste_prenoms[1][0][0:4])
'''

'''
l1=[]

for i in range(5) :
    x=input("Entrez les prenoms : ")
    l1.append(x)
print(l1)

for word in l1:
    if word[0] == 'A':
        print("les prénoms de la liste commençant par la lettre A sont "+word)
'''

'''
l1=[]
l2=[]
l3=[]
while True :
    chiffres=input("rentrez vos chiffres : ")
    if chiffres == "stop" :
        break
    if chiffres not in l1 :
        l1.append(chiffres)
    else :
        l2.append(chiffres)
    print(l1)
    print(l2)
'''

'''
dictionnaire={ "chat" : "animal domestique", "arbre" : "plante à tronc", "ordinateur" : "appareil électronique"}
print(dictionnaire.keys())
print(dictionnaire.values())
for x in dictionnaire.items() :
    print(x)

print(dictionnaire.get("chat"))

definition_chat=dictionnaire.get("chat")
print(definition_chat)

dictionnaire.pop("chat")

print(dictionnaire)
'''

'''
contacts = {"nom":"John Doe", "téléphone":"555-555-5555", "email":"johndoe@example.com"}

print(contacts.get("téléphone"))
contacts["téléphone"]="555-555-5556"
print(contacts.get("téléphone"))
print(contacts.items())

contacts["ville"] = "New York"
print(contacts.items())

contacts.pop("ville")
print(contacts.items())
'''

'''
employes={}
employes["personne0"]={"nom":"Jane", "poste":"directeur", "salaire":75000, "ancienneté":5}
employes["personne1"]={"nom":"Jojo", "poste":"dsi", "salaire":76000, "ancienneté":9}
employes["personne2"]={"nom":"Jiji", "poste":"rh", "salaire":32000, "ancienneté":2}
employes["personne3"]={"nom":"tutu", "poste":"tech", "salaire":20220, "ancienneté":3}

for info in employes.items() :
    print(info)

for key in employes.keys(): 
   print(employes[key]["nom"])

for employes in employes.values(): 
   print(employes["salaire"])

#for employes in employes.items():
'''

'''
question1 = """Quel célèbre dictateur dirigea l'URSS du milieu des années 1920 à 1953 ?
a) Trotski
b) Molotov
c) Staline
d) Lenin"""
question2 = """Quel pays a remporté la coupe du monde de football en 2014 ?
a) Italie 
b) Allemagne
c) Argentine
d) Brezil"""
question3 = """Quelle profession est concernée par le serment d'Hippocrate ?
a) Juge 
b) Medecin
c) Pharmacien
d) Avocat"""

questions=[question1, question2, question3]
responses=["a", "c", "b"]
cptr=0
for i in range(len(questions)) :
    print(questions[i])
    user_input = input()
    if user_input == responses[i] :
        cptr=cptr+1
        print("Bonne reponse\n")
    else :
        print("Mauvaise reponse\n")

print(f"Vous avez eu {cptr} de bonnes reponses sur {len(questions)}")
'''


'''
scrabble = {"A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1, "J": 8, "K": 10, "L": 1, "M": 2,
            "N": 1, "O": 1, "P": 3, "Q": 8, "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "W": 10, "X": 10, "Y": 10, "Z": 10}


def points(mot):
    total = 0
    for letter in mot:
        total = total + scrabble[letter]
    return total


print(points(mot="QSDLJKNHIO"))
'''



#kjs


















