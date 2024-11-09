
def brute_force(mot_de_passe_a_trouver, longueur_max, intervalle):
        caracteres = string.ascii_letters + string.digits + string.punctuation
        essais = 0
        last_notification_time = time.time() 
        essais_1 = essais
        nombre_essais_total = sum(len(caracteres) ** longueur for longueur in range(1, longueur_max + 1))
        
        for longueur in range(1, longueur_max + 1):
            for combinaison in itertools.product(caracteres, repeat=longueur):
                essais += 1
                tentative = ''.join(combinaison)
                                        
                if tentative == mot_de_passe_a_trouver:
                    return tentative, essais
                else:
                    return tentative
                # Informer l'utilisateur à intervalles dynamiques
                heure = time.time()
                last_time = last_notification_time
                last_notification_time = informer_utilisateur_et_essais_effectues(essais, last_notification_time, intervalle, essais_1, nombre_essais_total)
                
                if heure - last_time >= intervalle:
                    essais_1 = essais
                
        return None, essais
if __name__ == "__main__":
    import itertools
    import string
    import MotDePasse.Generateur_de_mot_passe
    import time

    def informer_nombre_dessais_par_sec(essais, last_time, essais_1):
        time_2 = time.time()
        essais_2 = essais
        essais_par_sec = (essais_2 - essais_1) / (time_2 - last_time)
        return essais_par_sec, essais_1

    def estimer_temps_restant(essais, nombre_essais_total):
        time_actuel = time.time()
        essais_restants = nombre_essais_total - essais
        temps_restant = essais_restants / (essais/(time_actuel-start_time))  # moyenne des essais par seconde
        return temps_restant

    def informer_utilisateur_et_essais_effectues(essais, last_time, intervalle, essais_1, nombre_essais_total):
        current_time = time.time()
        if current_time - last_time >= intervalle:
            essais_par_sec, essais_1 = informer_nombre_dessais_par_sec(essais, last_time, essais_1)
            temps_restant = estimer_temps_restant(essais, nombre_essais_total)
            temps_restant = temps_restant * 0.80  # Correction : point au lieu de virgule
            print("")
            print(f"{essais:,} essais déjà effectués, recherche en cours...")
            print(f"Essais par seconde: {essais_par_sec:,.0f}")
            print(f"Temps estimé restant: {temps_restant:,.0f} secondes ({temps_restant/60:,.1f} minutes) "
                f"ou ({temps_restant/3600:,.1f} heures) ou ({temps_restant/86400:,.1f} jours) "
                f"ou ({temps_restant/31536000:,.1f} ans)")
            return current_time
        return last_time

    

    # Exemple d'utilisation
    try: 
        longueur_max = int(input("Quel est la longueur max du mot de passe? "))  # longueur maximum pour chaque essai
    except ValueError:
        print("Erreur: entrez un entier valide")
        exit(1)

    try:
        intervalle = int(input("À quel intervalle de temps entre chaque fois que l'on vous informe de l'avancée? (en secondes): "))
    except ValueError:
        print("Erreur: entrez un entier valide")
        exit(1)

    mot_de_passe_secret = MotDePasse.Generateur_de_mot_passe.generer_mot_de_passe(longueur_max, True, True)

    # Donne la durée du craquage
    start_time = time.time()

    # Code à mesurer
    try:
        mot_de_passe_trouve, nombre_essais = brute_force(mot_de_passe_secret, longueur_max,intervalle)
    except MemoryError:
        print("Erreur: la mémoire est insuffisante pour exécuter ce programme.")
        end_time = time.time()
        elapsed_time = end_time - start_time
        elapsed_time_en_minutes = elapsed_time/60
        print(f" en {elapsed_time:,.0f} secondes soit {elapsed_time_en_minutes:,.1f} minutes soit {elapsed_time/3600:,.1f} heures soit {elapsed_time/86400:,.1f} jours soit {elapsed_time/31536000:,.1f} ans.")

    end_time = time.time()
    elapsed_time = end_time - start_time
    elapsed_time_en_minutes = elapsed_time / 60

    if mot_de_passe_trouve:
        print(f"Le mot de passe est: {mot_de_passe_trouve} découvert après {nombre_essais:,} essais en {elapsed_time:.0f} secondes "
            f"soit {elapsed_time_en_minutes:.1f} minutes soit {elapsed_time/3600:,.1f} heures "
            f"soit {elapsed_time/86400:,.1f} jours soit {elapsed_time/31536000:,.1f} ans avec une moyenne de {nombre_essais/elapsed_time:,.0f} essais par seconde.")
    else:
        print(f"Mot de passe non trouvé après {nombre_essais:,} essais. Après {nombre_essais:,} essais en {elapsed_time:.0f} secondes "
            f"soit {elapsed_time_en_minutes:.1f} minutes soit {elapsed_time/3600:,.1f} heures "
            f"soit {elapsed_time/86400:,.1f} jours soit {elapsed_time/31536000:,.1f} ans avec une moyenne de {nombre_essais/elapsed_time:,.0f} essais par seconde.")


