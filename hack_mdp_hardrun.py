import itertools
import string
import Generateur_de_mot_passe
import time

def estimer_temps_restant(essais, nombre_essais_total):
    time_actuel = time.time()
    essais_restants = nombre_essais_total - essais
    temps_restant = essais_restants / (essais/(time_actuel-start_time))#moyenne des essais par seconde
    return temps_restant

def brute_force(mot_de_passe_a_trouver, longueur_max):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    essais = 0
    nombre_essais_total = sum(len(caracteres) ** longueur for longueur in range(1, longueur_max + 1))
    informer_utilisateur_sur_le_temps=True

    # Générer toutes les combinaisons possibles jusqu'à la longueur spécifiée
    for longueur in range(1, longueur_max + 1):
        for combinaison in itertools.product(caracteres, repeat=longueur):
            essais += 1
            tentative = ''.join(combinaison)
            
            if tentative == mot_de_passe_a_trouver:
                return tentative, essais
           
            heure_actuel = time.time()
            if heure_actuel - start_time >= 180 and informer_utilisateur_sur_le_temps==True:#si le temps écoulé est supérieur à 10s et inférieur à 10,00001s , on affiche l'estimation de temps restant
                temps_restant =estimer_temps_restant(essais, nombre_essais_total)
                print(f"Temps estimé restant: {temps_restant:.0f} secondes ({temps_restant/60:.1f} minutes) ou ({temps_restant/3600:.1f} heures) ou ({temps_restant/86400:.1f} jours) ou ({temps_restant/31536000:.1f} ans) " )
                informer_utilisateur_sur_le_temps=False
    return None, essais

# Exemple d'utilisation
longueur_max = int(input("quel est la longueur max du mot de passe?: "))  # longueur maximum pour chaque essai
mot_de_passe_secret = Generateur_de_mot_passe.generer_mot_de_passe(longueur_max,True,True)#génération d'un mot de passe


#Donne la durée du craquage
start_time = time.time()

# Code à mesurer
try:
    mot_de_passe_trouve, nombre_essais = brute_force(mot_de_passe_secret, longueur_max)
except MemoryError:
    print("Erreur: la mémoire est insuffisante pour exécuter ce programme.")
    end_time = time.time()
    elapsed_time = end_time - start_time
    elapsed_time_en_minutes = elapsed_time/60
    print(f" MemoryError: en {elapsed_time:,.0f} secondes soit {elapsed_time_en_minutes:,.1f} minutes soit {elapsed_time/3600:,.1f} heures soit {elapsed_time/86400:,.1f} jours soit {elapsed_time/31536000:,.1f} ans.")
end_time = time.time()
elapsed_time = end_time - start_time
elapsed_time_en_minutes = elapsed_time/60

if mot_de_passe_trouve:
    print(f"Le mot de passe est: {mot_de_passe_trouve} découvert après {nombre_essais:,} avec une moyenne de {nombre_essais/elapsed_time:,.0f} essais en {elapsed_time:,.0f} secondes soit {elapsed_time_en_minutes:,.1f} minutes soit {elapsed_time/3600:,.1f} heures soit {elapsed_time/86400:,.1f} jours soit {elapsed_time/31536000:,.1f} ans.")
else:
    print(f"Mot de passe non trouvé après {nombre_essais:,} essais. Avec une moyenne de {nombre_essais/elapsed_time:,.0f} essais en {elapsed_time:,.0f} secondes soit {elapsed_time_en_minutes:,.1f} minutes soit {elapsed_time/3600:,.1f} heures soit {elapsed_time/86400:,.1f} jours soit {elapsed_time/31536000:,.1f} ans.")
