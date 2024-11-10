import string
import random

longueur=int(input("Quel longueur pour le mot de passe ? Répondre par un nombre entier: "))

try:
    inclure_chiffre=bool(input("Mettre des chiffre ? Répondre par True ou False: "))
except ValueError:
    print("Erreur: La réponse doit être True ou False")

try:
    inclure_caractere_speciaux=bool(input("Mettre des cacrctère spéciaux ? Répondre par True ou False: "))
except ValueError:
    print("Erreur: La réponse doit être True ou False")

longueur=int(input("Quel longueur pour le mot de passe ? Répondre par un nombre entier: "))

def generer_mot_de_passe(longueur,inclure_chiffre,inclure_caractere_speciaux):
    caractere_du_mot_de_passe=string.ascii_letters
    
    if inclure_chiffre==True:
        caractere_du_mot_de_passe+=string.digits
    
    if inclure_caractere_speciaux==True:
        caractere_du_mot_de_passe+=string.punctuation

    mot_de_passe=''.join(random.choice(caractere_du_mot_de_passe) for _ in range(longueur))
    
    return mot_de_passe

if __name__=="__main__":
    longueur=int(input("Quel longueur pour le mot de passe ? Répondre par un nombre entier: "))

    try:
        inclure_chiffre=bool(input("Mettre des chiffre ? Répondre par True ou False: "))
    except ValueError:
        print("Erreur: La réponse doit être True ou False")

    try:
        inclure_caractere_speciaux=bool(input("Mettre des cacrctère spéciaux ? Répondre par True ou False: "))
    except ValueError:
        print("Erreur: La réponse doit être True ou False")

    longueur=int(input("Quel longueur pour le mot de passe ? Répondre par un nombre entier: "))

    print(generer_mot_de_passe(longueur,inclure_chiffre,inclure_caractere_speciaux))
    print(random.choice(string.ascii_letters))
    print(random.choice(string.digits))
