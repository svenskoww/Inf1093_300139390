#question 2 exercice 1 
def quicksortbyage(students):
    if len(students) <= 1:
        return students

    pivot = students[0]
    gauche = [student for student in students[1:] if student[1] < pivot[1]]
    droite = [student for student in students[1:] if student[1] >= pivot[1]]

    return quicksortbyage(gauche) + [pivot] + quicksortbyage(droite)

#liste initail
students = [
    ("viny", 34), ("ryan", 43), ("tity", 31), ("antony", 27),
    ("calvin", 39), ("lilian", 27), ("merlin", 19), ("rachy", 25)
]

# tri rapide
students_tries = quicksortbyage(students)
students_tries

#question 2 exercice 2
# liste etudiants
students = [("Antony", 27), ("Calvin", 39), ("Lilian", 27), ("Merlin", 19), ("Rachy", 25), ("Ryan", 23), ("Tity", 31), ("Viny", 34)]

#recherche dichotomique
def searchByName(name, students):
    debut = 0
    fin = len(students) - 1
    
    while debut <= fin:
        milieu = (debut + fin) // 2
        nom, age = students[milieu]
        
        if nom == name:
            return age
        elif nom < name:
            debut = milieu + 1
        else:
            fin = milieu - 1
    
    return None

#example
age_rachy = searchByName("Rachy", students)
print(f"age de Rachy est {age_rachy}")

age_viny = searchByName("Viny", students)
print(f"age de Viny est {age_viny}")

#question 1  exercice 3
# list des etudiants
students = [("antony", 27), ("calvin", 39), ("lilian", 27), ("merlin", 19), ("rachy", 25), ("ryan", 43), ("tity", 31), ("viny", 34)]


# fct affichage de nom
def printNames(students):
    for student in students:
        print(student[0])

#example
printNames(students)

#question 2 exercice 3
# liste etudiants
students = [("antony", 27), ("calvin", 39), ("lilian", 27), ("merlin", 19), ("rachy", 25), ("ryan", 43), ("tity", 31), ("viny", 34)]
#fct pour affichage de nom
def printRecNames(students, index=0):
    if index < len(students):
        print(students[index][0])
        printRecNames(students, index + 1)

#example
printRecNames(students)

