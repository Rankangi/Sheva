liste = []
liste.append(12) # Ajouter un élément
print(liste)
print(len(liste)) #Taille de la liste
print(liste[0]) #Sélection premier élt
del liste[0] #Suppression un elt
print(liste)
liste.append(1)
liste.append(15)
liste[1] = "Bonjour" # Modification d'un elt
liste.append("Hello")
print(liste)

n = len(liste)
print("Entré for")
for i in range(n): #Boucle for
    if liste[i] != "Bonjour": #condition if
        print(liste[i])
    else:
        print("Salut") #exemple else
    print(i)
print("Sorti for")
print(n)

for elt in liste: # Autre parcours de liste
    print(elt)

i=0
while i!=10: # Boucle while
    print(i)
    i += 1

n = len(liste)
print("Entré while")
i = 0
while i!=n:
    if liste[i] != "Bonjour": #condition if
        print(liste[i])
    else:
        print("Salut") #exemple else
    print(i)
    i += 1
print("Sorti while")
print(n)