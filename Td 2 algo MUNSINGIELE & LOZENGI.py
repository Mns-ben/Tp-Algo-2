class Client:
    def __init__(self, nom, date_naissance, numero_telephone, facture_dollars):
        self.nom = nom
        self.date_naissance = date_naissance
        self.numero_telephone = numero_telephone
        self.facture_dollars = facture_dollars


class GestionnaireClients:
    def __init__(self):
        self.clients = []  # Liste vide pour stocker les clients

    def ajouter_client(self, client):
        """Ajoute un client à la liste."""
        self.clients.append(client)

    def supprimer_client(self, nom_client):
        """Supprime un client de la liste en utilisant son nom."""
        for client in self.clients:
            if client.nom == nom_client:
                self.clients.remove(client)
                print(f"Client {nom_client} supprimé avec succès.")
                return
        print(f"Client {nom_client} non trouvé dans la liste.")

    def rechercher_client(self, nom_client):
        """Recherche un client dans la liste en utilisant son nom."""
        for client in self.clients:
            if client.nom == nom_client:
                print(f"Client trouvé : {client.nom}")
                print(f"Date de naissance : {client.date_naissance}")
                print(f"Numéro de téléphone : {client.numero_telephone}")
                print(f"Facture en dollars : ${client.facture_dollars : .2f}")
                return
        print(f"Client {nom_client} non trouvé dans la liste.")

# Exemple d'utilisation :
gestionnaire = GestionnaireClients()

# Ajout de clients
nouveau_client1 = Client(nom="POLYTECHNIQUE", date_naissance="2001-10-01", numero_telephone="+243 0818140560", facture_dollars=150.75)
nouveau_client2 = Client(nom="Beni lozengi", date_naissance="1990-07-20", numero_telephone="+243 818140120", facture_dollars=200.50)

gestionnaire.ajouter_client(nouveau_client1)
gestionnaire.ajouter_client(nouveau_client2)

# Recherche d'un client
gestionnaire.rechercher_client("POLYTECHNIQUE")

# Suppression d'un client
gestionnaire.supprimer_client("Beni lozengi")


class ImportateurCDR :

    def __init__(self):
        self.pile_dictionnaires = []  # Pile vide pour stocker les dictionnaires

    def lire_fichier_cdr(self, nom_fichier):
        """Lit le fichier CDR et génère des dictionnaires."""
        try:
            with open(nom_fichier, 'r') as fichier:
                lignes = fichier.readlines()
                for ligne in lignes:
                    # Analyse chaque ligne et crée un dictionnaire
                    identifiant, type_appel, date_heure, appelant, appele, duree, taxe = ligne.strip().split(',')
                    dictionnaire_cdr = {
                        'identifiant': identifiant,
                        'type_appel': type_appel,
                        'date_heure': date_heure,
                        'appelant': appelant,
                        'appele': appele,
                        'duree': float(duree),
                        'taxe': float(taxe)
                    }
                    self.pile_dictionnaires.append(dictionnaire_cdr)
            print(f"Importation réussie depuis le fichier {nom_fichier}.")
        except FileNotFoundError:
            print(f"Le fichier {nom_fichier} n'a pas été trouvé.")

    def afficher_pile(self):
        """Affiche les dictionnaires empilés."""
        for dictionnaire in self.pile_dictionnaires:
            print(dictionnaire)

# Exemple d'utilisation :
importateur = ImportateurCDR()
importateur.lire_fichier_cdr("fichier_cdr.txt")  # Remplacez par le nom de votre fichier CDR
importateur.afficher_pile()


class FactureGenerator:
    def __init__(self):
        # Taux pour SMS
        self.taux_sms_meme_reseau = 0.001
        self.taux_sms_autre_reseau = 0.002

        # Taux pour appel d'une minute
        self.taux_appel_meme_reseau = 0.025
        self.taux_appel_autre_reseau = 0.05

        # Taux pour Internet (1 Mo)
        self.taux_internet = 0.03

    def calculer_montant_sms(self, meme_reseau: bool) -> float:
        """
        Calcule le montant pour un SMS en fonction du réseau.
        :param meme_reseau: True si le SMS est vers le même réseau, False sinon.
        :return: Montant du SMS.
        """
        if meme_reseau:
            return self.taux_sms_meme_reseau
        else:
            return self.taux_sms_autre_reseau

    def calculer_montant_appel(self, meme_reseau: bool) -> float:
        """
        Calcule le montant pour un appel d'une minute en fonction du réseau.
        :param meme_reseau: True si l'appel est vers le même réseau, False sinon.
        :return: Montant de l'appel.
        """
        if meme_reseau:
            return self.taux_appel_meme_reseau
        else:
            return self.taux_appel_autre_reseau

    def calculer_montant_internet(self, quantite_mo: int) -> float:
        """
        Calcule le montant pour Internet en fonction de la quantité de données (en Mo).
        :param quantite_mo: Quantité de données en Mo.
        :return: Montant pour Internet.
        """
        return self.taux_internet * quantite_mo

# Exemple d'utilisation
facture_gen = FactureGenerator()
montant_sms = facture_gen.calculer_montant_sms(meme_reseau=True)
montant_appel = facture_gen.calculer_montant_appel(meme_reseau=False)
montant_internet = facture_gen.calculer_montant_internet(1)

print(f"Montant SMS (même réseau) : ${montant_sms : .3f}")
print(f"Montant appel (autre réseau) : ${montant_appel : .3f}")
print(f"Montant Internet (1 Mo) : ${montant_internet : .3f}")


class StatistiquesClient:
    def __init__(self):
        self.nbre_appels = 0
        self.nbre_sms = 0
        self.gigaoctets_utilises = 0

    def ajouter_appel(self):
        """
        Incrémente le nombre d'appels.
        """
        self.nbre_appels += 1

    def ajouter_sms(self):
        """
        Incrémente le nombre de SMS.
        """
        self.nbre_sms += 1

    def ajouter_gigaoctets(self, quantite_go):
        """
        Ajoute la quantité de gigaoctets utilisés.
        :param quantite_go: Quantité de gigaoctets à ajouter.
        """
        self.gigaoctets_utilises += quantite_go

    def afficher_statistiques(self):
        """
        Affiche les statistiques d'utilisation.
        """
        print(f"Nombre d'appels : {self.nbre_appels}")
        print(f"Nombre de SMS : {self.nbre_sms}")
        print(f"Gigaoctets utilisés : {self.gigaoctets_utilises} Go")

# Exemple d'utilisation
client_stats = StatistiquesClient()
client_stats.ajouter_appel()
client_stats.ajouter_sms()
client_stats.ajouter_gigaoctets(2)
client_stats.ajouter_gigaoctets(1.5)

client_stats.afficher_statistiques()
