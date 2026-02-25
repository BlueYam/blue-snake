from random import choice, random

class Character:
    def __init__(self, name, battery, willpower, shame, money):
        self.name = name
        self.battery = battery
        self.willpower = willpower
        self.shame = shame
        self.money = money

    def take_damage(self, amount):
        if random() < 0.10:
            print(f"{self.name} dodge the attack!")
        else:
            self.battery -= amount
            print(f"{self.name} lost {amount} of Social Battery's!")

        if self.battery <= 0:
            print(f"{self.name} has turned into a slime!")
            exit()
    
    def gain_shame(self, amount):
        self.shame += amount
        print(f"{self.name} gained {amount} of Shame!")
        if self.shame >= 100:
            print(f"{self.name} implodes from the shame!")
            exit()

    def lower_shame(self, method, amount):
        if method == "hide":
            if self.willpower >= 20:
                print(f"{self.name} hide in a trashcan!")
                self.shame = max(0, self.shame - amount)
                self.willpower -= amount
                print(f"{self.name} lost {self.shame} in exchange for {self.willpower}")
            else:
                print(f"{self.name} doesn't have the willpower!")
        elif method == "bribe":
            if self.money >= 50:
                print(f"{self.name} bribed her friend to distract the stranger")
                self.shame = max(0, self.shame - amount)
                self.money -= 50
                print(f"{self.name} lost {self.shame} in exchange for ${self.money}")
            else:
                print(f"You're too broke to bribe anyone!")

    def be_normal(self, amount):
        self.willpower += amount
        print(f"{self.name} gained {amount} of Willpower!")
        if self.willpower >= 100:
            print(f"{self.name} has turned into a Giga Chad and left!")
            exit()

    def __str__(self):
        return f"--- {self.name} | Battery: {self.battery} | Willpower: {self.willpower} | Shame: {self.shame} ---"

    def ryo_support(self, target):
        if self.willpower >= 20:
            print(f"{self.name} plays a cool bass riff to distract the stranger!")
            target.battery += 10
            self.willpower -= 20
        else:
            print(f"{self.name} is staring blankly at a leaf.")        

enemy_move = choice(["Small Talk", "Intense Staring", "Close Talker", "Unexpected Wink"])
