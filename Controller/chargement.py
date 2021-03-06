from tinydb import TinyDB
from Model import model


db = TinyDB("db.json")
players_table = db.table("players")
tournois_table = db.table("tournois")


def serialize_player(player):
    """Serialize un joueur donné"""
    serialized_player = {
        "nom": player.nom,
        "prenom": player.prenom,
        "date": player.date,
        "classement": player.classement,
        "id": player.id,
    }
    return serialized_player


def serialize_match(match):
    """Serialize un match donné"""
    serialized_match = {
        "joueur1": match.joueur1,
        "joueur2": match.joueur2,
    }
    return serialized_match


def serialize_tour(tour):
    """Serialize un tour donné"""
    serialized_matchs = []
    for match in tour.liste_matchs:
        serialized_matchs.append(serialize_match(match))

    serialized_tour = {
        "nom": tour.nom,
        "players": tour.players,
        "liste_matchs": serialized_matchs,
    }
    if hasattr(tour, "heure_debut") is True:
        serialized_tour["heure_debut"] = tour.heure_debut
    if hasattr(tour, "heure_fin") is True:
        serialized_tour["heure_fin"] = tour.heure_fin
    return serialized_tour


def serialize_tournoi(tournoi):
    """Serialize un tournoi donné"""
    serialized_tours = []
    for tour in tournoi.liste_tours:
        serialized_tours.append(serialize_tour(tour))

    serialized_tournoi = {
        "nom": tournoi.nom,
        "lieu": tournoi.lieu,
        "date": tournoi.date,
        "players": tournoi.players,
        "timer": tournoi.timer,
        "description": tournoi.description,
        "nombre_tours": tournoi.nombre_tours,
        "liste_tours": serialized_tours,
        "tour_actuel": tournoi.tour_actuel,
        "score_table": tournoi.score_table,
        "already_played": tournoi.already_played,
    }
    return serialized_tournoi


def deserialize_player(player):
    """Deserialize un joueur donné"""
    nom = player["nom"]
    prenom = player["prenom"]
    date = player["date"]
    classement = player["classement"]
    id = player["id"]
    model.Acteurs.joueurs.append(model.Player(nom, prenom, date, classement, id))


def deserialize_tournoi(tournoi):
    """Deserialize un tournoi donné"""
    players = tournoi["players"]

    liste_tours = []
    for tour in tournoi["liste_tours"]:
        liste_tours.append(deserialize_tour(tour))

    nom = tournoi["nom"]
    lieu = tournoi["lieu"]
    date = tournoi["date"]
    timer = tournoi["timer"]
    nombre_tours = tournoi["nombre_tours"]
    description = tournoi["description"]
    tour_actuel = tournoi["tour_actuel"]
    score_table = tournoi["score_table"]
    already_played = tournoi["already_played"]
    tournament = model.Tournoi(
        nom,
        lieu,
        date,
        players,
        timer,
        description,
        tour_actuel,
        score_table,
        already_played,
        nombre_tours,
    )
    model.Acteurs.tournois.append(tournament)
    tournament.liste_tours = liste_tours
    return tournament


def deserialize_tour(turn):
    """Deserialize un tour donné"""
    liste_matchs = []
    for match in turn["liste_matchs"]:
        liste_matchs.append(deserialize_match(match))

    nom = turn["nom"]
    players = turn["players"]

    tour = model.Tour(nom, players)
    tour.liste_matchs = liste_matchs

    if "heure_debut" in turn:
        tour.heure_debut = turn["heure_debut"]

    if "heure_fin" in turn:
        tour.heure_fin = turn["heure_fin"]

    return tour


def deserialize_match(match):
    """Deserialize un match donné"""
    joueur1 = match["joueur1"][0]
    joueur2 = match["joueur2"][0]
    score1 = match["joueur1"][1]
    score2 = match["joueur2"][1]

    match = model.Match(joueur1, joueur2, score1, score2)

    return match


def charge_data():
    """Effectue la deserialization de toutes les données"""
    serialized_players = players_table.all()
    serialized_tournois = tournois_table.all()

    for player in serialized_players:
        deserialize_player(player)

    for tournoi in serialized_tournois:
        deserialize_tournoi(tournoi)


def save_data():
    """Effectue la serialization de toutes les données"""
    players_table.truncate()
    tournois_table.truncate()

    for player in model.Acteurs.joueurs:
        players_table.insert(serialize_player(player))

    for tournoi in model.Acteurs.tournois:
        tournois_table.insert(serialize_tournoi(tournoi))
