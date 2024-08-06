#Exercice 1
### Question 1 

#On declare note liste Id Grade
listIdGrade = [(202401, 17), (202402, 59),(202403, 73),(202404, 90),(202406, 77),(202408, 59),(202409, 93),(202410, 74) ]
# On affiche notre liste 
print(listIdGrade)

### Question 2

# ici j'ai defini ma full list comme liste vide
fullList = []
# on declare la liste IDName
listIdName = [(202401, "Anani"), (202402, "Simon"),(202403, "Pierre"),(202404, "Kylian"),(202405, "Alphonse"),(202406, "Joshua"),(202407, "Colince"),(202408, "Khristian"),(202409, "Zinedine"),(202410, "Didier") ]
for matricule, nom in listIdName:
    for mat, note in fullList:
        if matricule == mat:
            fullList.append((matricule, nom, note))
 #On affiche notre liste           
print("fullList:", fullList)

#Exercice 2 
### Question 1
def searchNameById(name, listIdName):
    for candidat in listIdName:
        if candidat[1] == name:
            return candidat[0]
    return 0

listIdName = listIdName = [(202401, "Anani"), (202402, "Simon"),(202403, "Pierre"),(202404, "Kylian"),(202405, "Alphonse"),(202406, "Joshua"),(202407, "Colince"),(202408, "Khristian"),(202409, "Zinedine"),(202410, "Didier") ]
# saisie de l'utilisateur
nom_rechercher = input("entrez le nom a rechercher: ")
matricule = searchNameById(nom_rechercher, listIdName)
if resultatid:
    print(f"Le matricule de {nom_rechercher} : {matricule}")
else:
    print(f"0")
    
### Question 2 
def searchGradeByIdSeq(id, listIdGrade):
    for matricule in listIdGrade:
        if matricule[0] == id:
            return matricule[1]
    return 0
listIdGrade =  [(202401, 17), (202402, 59),(202403, 73),(202404, 90),(202406, 77),(202408, 59),(202409, 93),(202410, 74) ]
 # saisie du matricule 
matricule_rechercher = int(input("entrez le matricule a rechercher: "))
note = searchGradeByIdSeq(matricule_rechercher, listIdGrade)
if note:
    print(f"La note du matricule {matricule_rechercher} est de {note}")
else:
    print(f"0")

### Question 3 

def buildListSeq(listIdName, listIdGrade):
    fullList = []
    for candidat in listIdName:
        matricule = candidat[0]
        nom= candidat[1]
        note = searchGradeByIdSeq(matricule, listIdGrade)
        fullList.append([matricule, nom, note])
    return fullList
#On declare nos liste precedentes 
listIdName =  [(202401, "Anani"), (202402, "Simon"),(202403, "Pierre"),(202404, "Kylian"),(202405, "Alphonse"),(202406, "Joshua"),(202407, "Colince"),(202408, "Khristian"),(202409, "Zinedine"),(202410, "Didier") ]
listIdGrade = [(202401, 17), (202402, 59),(202403, 73),(202404, 90),(202406, 77),(202408, 59),(202409, 93),(202410, 74) ]
# construction de la liste complete
fullList = buildListSeq(listIdName, listIdGrade)
for candidat in fullList:
    print(fullList)

#Exercice 3 
### Question 1

#j'ai choisi d'utiliser le tri rapide
# definition de la boucle 
def quickSortlistIdGrade(std):
    if(len(std)<=1):
        return std
    pivot = std.pop()
    petit = []
    grand = []
    for i in range(len(std)):
        if(std[i][1] <= pivot[1]):
            petit.append(std[i])
        else:
            grand.append(std[i])
    
    return quickSortByAge(petit) + [pivot] + quickSortByAge(grand)

# on declare notre liste au'on souhaite trier
listIdGrade = [(202401, 17), (202402, 59),(202403, 73),(202404, 90),(202406, 77),(202408, 59),(202409, 93),(202410, 74) ]
# affichage de la liste trier
print(quickSortlistIdGrade(listIdGrade))

### Question 2

def searchgradebyIddicho(matricule, notes):
    gauche, droite = 0, len(notes) - 1
    while gauche <= droite:
        milieu = (gauche + droite) // 2
        if notes[milieu]["matricule"] == matricule:
            return notes[milieu]["note"]
        elif notes[milieu]["matricule"] < matricule:
            gauche = milieu + 1
        else:
            droite = milieu - 1
    return 0  

# Listeidbygrade trier par selection
ListIdbyGrade = [
    {"matricule": 202401, "note": 17},
    {"matricule": 202402, "note": 59},
    {"matricule": 202408, "note": 59},
    {"matricule": 202403, "note": 73},
    {"matricule": 202410, "note": 74},
    {"matricule": 202406, "note": 77},
    {"matricule": 202404, "note": 90},
    {"matricule": 202409, "note": 93},
]
# demande de saisie du matricule rechercher
matricule = int(input("entrez le matricule a rechercher: "))
note = searchgradebyIddicho(matricule, notes)
#on affiche la note du matricule
print(f"la note du matricule  {matricule} est {note}")


### Question 4
# Pour moi, la recherche dichotomique est la technique a plus facile a utiliser pour effectuer une recherche,cela est du a son utilisation de la division absolue qui rend l'exercice plus facile, de plus la recherche dichotomique elimine soit une liste grande soit une liste petite ce qui rend la recherche plus precise