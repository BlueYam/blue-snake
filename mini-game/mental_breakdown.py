import os
import time
import sys
import random
import threading
import lyricsgenius
from dotenv import load_dotenv

load_dotenv()
GENIUS_ACCESS_TOKEN = os.getenv("GENIUS_ACCESS_TOKEN")

RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"
GLITCH_CHARS = ["@", "#", "$", "%", "*", "!", "?", "¡", "☠", "ø"]

def glitch_background():
    """Randomly flickers characters or colors in the background."""
    while True:
        if random.random() > 0.8:
            # Randomly jump cursor, print a glitch char, and jump back
            sys.stdout.write(f"\033[s\033[{random.randint(1, 20)};{random.randint(1, 50)}H{random.choice(GLITCH_CHARS)}\033[u")
            sys.stdout.flush()
        time.sleep(0.1)

def breakdown_print(text):
    if not text: return
    clean_text = text.replace("Embed", "").strip()

    for char in clean_text:
        # Variable Delay (Simulate stuttering)
        delay = random.uniform(0.01, 0.1)
        if random.random() > 0.95: 
            delay = random.uniform(0.5, 0.8) # Long pause/freeze
        
        # Random Capitalization
        if random.random() > 0.98:
            char = random.choice(GLITCH_CHARS)
        
        # Visual Stress (Flash red)
        if random.random() > 0.97:
            sys.stdout.write(RED + BOLD + char + RESET)
        else:
            sys.stdout.write(char)
            
        sys.stdout.flush()
        time.sleep(delay)
    print(f"\n{RED}SYSTEM_FAILURE_ERROR_0x999{RESET}")

def fetch_and_play(artist_name, song_title):
    if not GENIUS_ACCESS_TOKEN:
        print("Error: GENIUS_ACCESS_TOKEN missing.")
        return

    genius = lyricsgenius.Genius(GENIUS_ACCESS_TOKEN)
    genius.verbose = False
    
    noise_thread = threading.Thread(target=glitch_background, daemon=True)
    noise_thread.start()

    print(f"{BOLD}INITIATING PSYCHOSIS...{RESET}")
    try:
        song = genius.search_song(song_title, artist_name)
        if song:
            breakdown_print(song.lyrics)
        else:
            print("Target not found. Dissociating.")
    except Exception as e:
        print(f"CRITICAL OVERLOAD: {e}")

if __name__ == "__main__":
    fetch_and_play("VIOLENT VIRA", "Common Decency")