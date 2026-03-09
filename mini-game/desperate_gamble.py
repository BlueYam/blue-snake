import time
import sys
from random import randint

# Function to give that "haunted typewriter" feel
def spectral_print(text, delay=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

fate = randint(1, 20)
life_essence = 5
attempts = 0

print("--- THE OSSUARY OF LOST NUMBERS ---")
spectral_print("The candles flicker. A spirit whispers a secret...")

while attempts < life_essence:
    try:
        remaining = life_essence - attempts
        print(f"\n[Essence Remaining: {'🕯️ ' * remaining}]")
        
        entry = input("Reach into the dark and pull out a number (1-20): ")
        val = int(entry)
        attempts += 1

        if val == fate:
            spectral_print(f"!!! ECSTASY !!! The number was {fate}.")
            spectral_print(f"You cheated the Grave in {attempts} breaths. This time.")
            break
        elif val < fate:
            spectral_print("The cold winds hiss... 'Higher,' it wails.")
        else:
            spectral_print("The earth trembles... 'Lower,' it moans.")
            
        if attempts == life_essence:
            spectral_print("\nYour light has gone out. The silence is eternal.")
            spectral_print(f"The number was {fate}. You are now part of the foundation.")

    except ValueError:
        spectral_print("That is not a number. The spirits do not appreciate your gibberish.")