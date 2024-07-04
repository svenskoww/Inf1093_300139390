import os

def listing_directory(directory):
    files = []
    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)):
            file_name, ext = os.path.splitext(file)
            size = os.path.getsize(os.path.join(directory, file)) / (1024 * 1024)  
            files.append((file_name, ext, size))
    return files


directory_path = r'C:\Users\cantw\OneDrive\Documents\Semaine 2' #j'ai utilise mon repertoire pour cet exemple
liste_fichiers = listing_directory(directory_path)
print(liste_fichiers)
