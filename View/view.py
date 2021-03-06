from Controller import rapports
from Controller import chargement
from Controller import tournoi
from View import inputs
from Model import model
import time


def Menu():
    """Affiche le menu principal"""

    print("\nVeuillez choisir un menu :")
    print("")
    print("[1] Menu des tournoi")
    print("[2] Menu des joueurs")
    print("[3] Afficher la liste de...")
    print("[4] Sauvegarder")
    print("[5] Quitter")
    print()
    reponse = input()
    match reponse:
        case "0":
            print(model.Player.id_list)

        case "1":
            MenuTournoi()

        case "2":
            MenuJoueurs()

        case "3":
            MenuListes()

        case "4":
            chargement.save_data()
            print("\nDonnées sauvegardées\n")

        case "5":
            quit()

        case _:
            print("\nCommande non reconnue\n")


def MenuListes():
    """Affiche le menu Rapports"""

    print("\n[1] Tous les joueurs")
    print("[2] Tous les joueurs d'un tournoi")
    print("[3] Tous les tournois")
    print("[4] Tous les tours d'un tournoi")
    print("[5] Tous les matchs d'un tournoi")
    print()

    response = input()
    match response:
        case "1":
            print("\nAfficher par ordre...\n")
            print("[1] Alphabétique")
            print("[2] Classement\n")
            rapports.show_players("all", input())

        case "2":
            tournament = inputs.last_tournois()
            print("\nAfficher par ordre...\n")
            print("[1] Alphabétique")
            print("[2] Classement\n")
            rapports.show_players(tournament, input())

        case "3":
            rapports.showTournois()

        case "4":
            rapports.showTours()

        case "5":
            rapports.show_tournoi_matchs()


def MenuJoueurs():
    """Affiche le menu Joueur"""

    print("\n[1] Ajouter un joueur")
    print("[2] Modifier un joueur")
    print()
    match input():
        case "1":
            tournoi.add_player()

        case "2":
            player = tournoi.search_player()
            inputs.modify_player(player)


def MenuTournoi():
    """Affiche le menu Tournoi"""

    print("\n[1] Créer un tournoi")
    print("[2] Reprendre un tournoi")
    print()
    reponse_tournoi = input()

    match reponse_tournoi:

        case "1":
            tournament = tournoi.create_tournoi()
            print("\nVoulez vous lancer le tournoi maintenant ?\n")
            print("[1] Oui")
            print("[2] Non\n")
            reponse_start_tournoi = input()

            match reponse_start_tournoi:

                case "1":
                    tournoi.run_tournoi(tournament)

                case _:
                    pass

        case "2":
            tournoi.reprendre_tournoi()


def run():
    """Défini un cycle de Menu"""
    while True:

        print()
        Menu()
        print()

        # Sauvegarde les données à chaque cycle, "au cas où"
        chargement.save_data()
        time.sleep(1)
