import time


class Battle:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def start(self):
        print(f"\n--- BATTLE START: {self.p1.name} vs {self.p2.name} ---")
        turn = 1

        while self.p1.is_alive() and self.p2.is_alive():
            print(f"\n--- Turn {turn} ---")
            self.execute_turn(self.p1, self.p2)
            if self.p2.is_alive():
                self.execute_turn(self.p2, self.p1)

            turn += 1
            time.sleep(1)

        winner = self.p1 if self.p1.is_alive() else self.p2
        print(f"\n{'=' * 20}")
        print(f"WINNER: {winner.name}!")
        print(f"{'=' * 20}")

    def execute_turn(self, attacker, defender):
        print(f"{attacker.name} uses {attacker.move_name}!")
        damage, is_crit = attacker.perform_attack(defender)
        msg = "CRITICAL HIT! " if is_crit else ""
        print(
            f"{msg}{defender.name} took {damage} damage! (HP: {max(0, defender.hp)}/{defender.max_hp})"
        )
