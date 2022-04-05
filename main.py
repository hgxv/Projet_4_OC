import model
import view


players = [
    ["z", "Kévin", "24/06/1995", "557"],
    ["a", "Célestin", "24/06/1995", "474"],
    ["b", "Tinatin", "24/06/1995", "22"],
    ["c", "Bysshe", "24/06/1995", "44"],
    ["d", "Lauressa", "24/06/1995", "21"],
    ["e", "Adelina", "24/06/1995", "100"],
    ["f", "Aziz", "24/06/1995", "1"],
    ["r", "Kirsti", "24/06/1995", "321"]
]

if __name__ == "__main__":

    model.Acteurs()
    print("Bienvenue sur le logiciel du tournoi")

#   Nos 8 faux joueurs sont ajoutés aux acteurs
    for player in players:
        model.Acteurs.joueurs.append(model.Player(player[0], player[1], player[2], player[3]))

    view.run()