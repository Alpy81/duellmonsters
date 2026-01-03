# Beispiel Yu-Gi-Oh Karten

class Duellmonsters:
    def __init__(self):
        self.angriff = None
        self.verteidigung = None
        self.zauberstaerke = None
        self.element = None
        self.x_position = 10
        self.y_position = 10

    def move(self, x, y):
        self.x_position += x
        self.y_position += y

# Erstes Monster
jinzo = Duellmonsters()

jinzo.angriff = 2400
jinzo.verteidigung = 1200
jinzo.zauberstaerke = 0
jinzo.element = "Shadow"

# Funktion Bewegung
jinzo.move(15, 25)


# Zweites Monster
schwarzer_magier = Duellmonsters()

schwarzer_magier.angriff = 2600
schwarzer_magier.verteidigung = 1600
schwarzer_magier.zauberstaerke = 3
schwarzer_magier.element = "Mystic"

# Funktion Bewegung
schwarzer_magier.move(15, 27)

# Kampf
player_one = "Alpy"
player_two = "Alpay"
score = 0


move_player_one = input(player_one  + " ist am Zug: ")

# Spieler 1 
if move_player_one == "Angriff mit Jinzo":
    print(f" Jinzo greift an mit {jinzo.angriff}")
    battle_one = input("Angriffschaden geht durch durch die DEF. Drücke E für Berechnung: ")
    if battle_one == "e":
        damage_score_one = jinzo.angriff - schwarzer_magier.verteidigung 
    print(f"Alpay erleidet einen Schaden von {damage_score_one}")
    result = schwarzer_magier.verteidigung - damage_score_one
    print(f"Neuer Verteidigungswert von Schwarzer Magier ist {result}")
else:
    print("Jinzo in Verteidigungsmodus")

# Spieler 2 
move_player_two = input(player_two + " ist am Zug: ")

if move_player_two == "Angriff mit Magier":
    print(" Magier greift an mit 2600")
    battle_two = input("Berechnung des Schadens durch Drücken von E: ")
    if battle_two == "e":
        damage_score_two = schwarzer_magier.angriff - jinzo.angriff
        print(f"Alpy erleidet einen Schaden von {damage_score_two}" )
        print(f"Lebenspunkte von Alpy reduzieren sich um {damage_score_two}")
else:
    print("Schwarzer Magier ebenaflls in DEF-Mode.")