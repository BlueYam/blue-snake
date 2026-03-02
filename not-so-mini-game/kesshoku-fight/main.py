from char import Bocchi, Nijika, Ryo, Kita
from battle import Battle

def main():
    roster = {
        "1": Bocchi(),
        "2": Nijika(),
        "3": Ryo(),
        "4": Kita()
    }

    print("Welcome to Kesshoku-Fight!")
    print("Choose your character:")
    for key, char in roster.items():
        print(f"{key}. {char.name}")

    p1_choice = input("\nSelect Player 1: ")
    p2_choice = input("Select Player 2: ")

    if p1_choice in roster and p2_choice in roster:
        p1 = type(roster[p1_choice])()
        p2 = type(roster[p2_choice])()
        
        game = Battle(p1, p2)
        game.start()
    else:
        print("Invalid selection. The band broke up.")

if __name__ == "__main__":
    main()