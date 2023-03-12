import os

while True:
    cree_fichier = input("Do you want to create a file in the current directory ? (y/n) : ")
    if cree_fichier.lower() == 'y':
        file_name = input("Enter the file name: ") + ".txt"
        #créer un chemin d'accès complet pour le fichier à partir du chemin du répertoire de travail actuel et du nom du fichier
        file_path = os.path.join(os.getcwd(), file_name)
        break
    elif cree_fichier.lower() == 'n':
        file_path = input("Enter the .txt file path: ")
        break
    else:
        print("Incorrect input. Please enter 'y' or 'n'.")

# Vérifie que le fichier est bien de type .txt
if not file_path.endswith(".txt"):
    print("The file must be a '.txt' file.")
else:
    stop_word=input("Enter your Stop Word: ")
    while True:
        title = input("Enter a title (or '" + stop_word + "' to quit): ")
        if title == stop_word:
            break
        with open(file_path, 'a') as f:
            f.write(title + "\n")
    print("Titles have been added to the file.")
