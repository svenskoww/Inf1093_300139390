{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "90dfc0e3-f395-4086-a7e8-b1a96e264ef0",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Entrez le nom de l'étudiant :  adam\n",
      "Entrez l'âge de l'étudiant :  0\n",
      "Voulez-vous ajouter un nouvel étudiant ? (1 pour oui, 0 pour non) :  1\n",
      "Entrez le nom de l'étudiant :  asd\n",
      "Entrez l'âge de l'étudiant :  555\n",
      "Voulez-vous ajouter un nouvel étudiant ? (1 pour oui, 0 pour non) :  0\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[('adam', 0), ('asd', 555)]\n"
     ]
    }
   ],
   "source": [
    "#Exercice 2 \n",
    "def build_list():\n",
    "    liste_etudiants = []\n",
    "    continuer = True\n",
    "\n",
    "    while continuer:\n",
    "        nom = input(\"Nom: \")\n",
    "        age = int(input(\"Age \"))\n",
    "        liste_etudiants.append((nom, age))\n",
    "\n",
    "        reponse = input(\"Voulez-vous ajouter un nouvel étudiant ? (1 pour oui, 0 pour non) : \")\n",
    "        if reponse == '0':\n",
    "            continuer = False\n",
    "\n",
    "    return liste_etudiants\n",
    "\n",
    "# Exemple d'affichage en dehors de la fonction\n",
    "liste_creee = build_list()\n",
    "print(liste_creee)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "7e3c6fda-df07-407b-b256-2f4af337d852",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "\n",
    "#Exercice 3 question 1\n",
    "def switch(liste, i, j):\n",
    "    if i < 0 or j < 0 or i >= len(liste) or j >= len(liste):\n",
    "        return \"Indices invalides\"\n",
    "    liste[i], liste[j] = liste[j], liste[i]\n",
    "    return liste"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "6c5ee372-b480-4bf9-963b-5a950038713f",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Iteration 1: [('Alice', 23), ('Bob', 21), ('Charlie', 25)]\n",
      "Iteration 2: [('Alice', 23), ('Bob', 21), ('Charlie', 25)]\n",
      "Iteration 3: [('Alice', 23), ('Bob', 21), ('Charlie', 25)]\n"
     ]
    }
   ],
   "source": [
    "#Exercice 3 question 2\n",
    "def switch(liste, i, j):\n",
    "    liste[i], liste[j] = liste[j], liste[i]\n",
    "\n",
    "def bubbleSort(liste):\n",
    "    n = len(liste)\n",
    "    for i in range(n):\n",
    "        for j in range(0, n-i-1):\n",
    "            # Comparer les noms des étudiants pour le tri alphabétique\n",
    "            if liste[j][0] > liste[j+1][0]:\n",
    "                switch(liste, j, j+1)\n",
    "        # Afficher la liste après chaque itération complète\n",
    "        print(f\"Iteration {i+1}: {liste}\")\n",
    "\n",
    "# Exemple d'utilisation\n",
    "liste_etudiants = [('Viny', 34), ('Ryan', 43), ('Tity', 31),('Antony',27),(\"Calvin\",39),('Lilian',27)]\n",
    "bubbleSort(liste_etudiants)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "04de4159-61bc-48b7-ad32-3866e692f5b6",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
