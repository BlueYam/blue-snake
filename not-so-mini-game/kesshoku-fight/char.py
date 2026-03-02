import random

class Character:
    def __init__(self, name, hp, attack, defense, move_name):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.defense = defense
        self.move_name = move_name

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        actual_damage = max(0, damage - (self.defense // 2))
        self.hp -= actual_damage
        return actual_damage

    def perform_attack(self, target):
        crit = 1.5 if random.random() < 0.2 else 1.0
        damage = int(self.attack * crit)
        dealt = target.take_damage(damage)
        return dealt, crit > 1.0

class Bocchi(Character):
    def __init__(self):
        super().__init__("Hitori 'Bocchi' Gotoh", 80, 25, 5, "Cyber-Psychosis Shred")

class Nijika(Character):
    def __init__(self):
        super().__init__("Nijika Ichiji", 100, 18, 10, "Dorito Drum Barrage")

class Ryo(Character):
    def __init__(self):
        super().__init__("Ryo Yamada", 110, 15, 15, "Bass Slap (Debt Collection)")

class Kita(Character):
    def __init__(self):
        super().__init__("Ikuyo Kita", 120, 16, 8, "Kita-aura Flash")