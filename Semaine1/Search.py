
#Collection de numbers
numbers = []
nb = int(input("Combien de nombres : "))
for i in range(nb):
    nb = int(input(f"Nombre1{i+1}:"))
    numbers.append(nb)

#Affichache des numbers
print(numbers)

# Lire la valeur a rechercher.
search_nb = int(input("Quel nombre a chercher?"))

# Recherche sequentielle

position = -1
for i in range(len(numbers)):
    if(search_nb==numbers[i]):
        position=i
        break
if(position>-1):
    print(f"{search_nb} est a la position {position}")
else:
    print(f"{search_nb} n'existe pas dans le tableau")

# Recherche dichotomique lorsque le tableau est trie
""" 
found = False
begin=0
end=len(numbers)-1
while(not(found) and begin>end):
    mid = (begin+end)//2
    if(search_nb == numbers[mid]):
        found=True
        print("nombre trouve a la position : ", mid)
    else:
        if(search_nb <= numbers[mid]):
            end = mid-1
        else:
            begin = mid+1
            
if(not(found)):
    print("Nombre inexistant ")

"""


#Question 1: Completer le code necessaire pour afficher la position de la valeur maximale dans numbers



#Question 2: Completer le code necessaire pour afficher la position de la valeur minimale dans numbers



#Question 3: Ecrire le code necessaire pour verifier si le tableau numbers est trie en ordre croissant


#Question 4: Considerons que le tableau est trie en ordre decroissant. Implementer une methode de recherche dichotomique dans ce cas.