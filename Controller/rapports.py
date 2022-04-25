from Model.model import Acteurs
from Model.model import Player
from Controller import tournoi
from tabulate import tabulate


def showPlayers(what, ordre):

    match what:
        case "all":
            joueurs = Acteurs.joueurs

        case tournoi:
            joueurs = []
            for joueur in tournoi.players:
                joueurs.append(Player.find_by_id(joueur))
            print(joueurs)

    match ordre:

        case "1":
            joueurs.sort(key=lambda Player: Player.__str__())
            print("Ordre alphabétique :\n")

        case "2":
            joueurs.sort(key=lambda Player: int(Player.classement))
            print("Par classement :\n")

        case _:
            return print("\nCommande non reconnue\n")

    noms = []
    prenoms = []
    dates = []
    classements = []

    for joueur in joueurs:
        noms.append(joueur.nom)
        prenoms.append(joueur.prenom)
        dates.append(joueur.date)
        classements.append(joueur.classement)

    print(
        tabulate(
            {
                "Noms": noms,
                "Prenoms": prenoms,
                "Date de naissance": dates,
                "Classement": classements,
            },
            headers="keys",
        )
    )
    print()


def showTournois():

    noms = []
    lieux = []
    dates = []
    timers = []
    tours_actuel = []
    nombre_tours = []
    descriptions = []

    for tournoi in Acteurs.tournois:
        noms.append(tournoi.nom)
        lieux.append(tournoi.lieu)
        dates.append(tournoi.date)
        timers.append(tournoi.timer)
        tours_actuel.append(tournoi.tour_actuel)
        nombre_tours.append(tournoi.nombre_tours)
        descriptions.append(tournoi.description)

    print(
        tabulate(
            {
                "Nom": noms,
                "Lieu": lieux,
                "Date": dates,
                "Timer": timers,
                "Tour actuel": tours_actuel,
                "Nombre de tours": nombre_tours,
                "Description": descriptions,
            },
            headers="keys",
        )
    )
    print()


def showTours():
    tournament = tournoi.search_tournoi()

    noms = []
    heure_debut = []
    heure_fin = []

    for tour in tournament.liste_tours:
        noms.append(tour.nom)
        heure_debut.append(tour.heure_debut)
        if hasattr(tour, "heure_fin") == True:
            heure_fin.append(tour.heure_fin)
        else:
            heure_fin.append("Pas terminé")

    print(
        tabulate(
            {"Nom": noms, "Heure de début": heure_debut, "Heure de fin": heure_fin},
            headers="keys",
        )
    )
    print()


def show_tournoi_matchs():
    tournament = tournoi.search_tournoi()
    for tour in tournament.liste_tours:
        print("\n" + tour.nom + " :\n")
        joueurs1 = []
        joueurs2 = []
        vs = []
        scores = []
        for match in tour.liste_matchs:
            joueurs1.append(Player.find_by_id(match.joueur1[0]).__str__())
            joueurs2.append(Player.find_by_id(match.joueur2[0]).__str__())
            vs.append("vs")
            scores.append(match.show_score())
        print(
            tabulate(
                {"Joueur 1": joueurs1, "Vs": vs, "Joueur 2": joueurs2, "Score": scores},
                headers="keys",
            )
        )
        print("\n\n")
