grimoire = []

print("--- THE GRIMOIRE OF UNFINISHED BUSINESS ---")
print("Every soul added is a weight upon your own.")

while True:
    action = input("\nAction (Invoke / Exorcise / Manifest / Depart): ").strip().lower()

    if action == "invoke":  # Add
        spirit = input("What burden shall we bind to this page? ")
        grimoire.append(spirit)
        print(f"The spirit of '{spirit}' is now bound to the ink.")
        
    elif action == "exorcise":  # Delete
        if not grimoire:
            print("The pages are blank. No spirits haunt you... yet.")
        else:
            print("Select the spirit to banish into the void:")
            for i, spirit in enumerate(grimoire):
                print(f" [{i}] - {spirit}")
            try:
                target = int(input("Index of the damned: "))
                banished = grimoire.pop(target)
                print(f"'{banished}' has been cast back into the ether.")
            except (ValueError, IndexError):
                print("The void does not recognize that number. The ritual fails.")

    elif action == "manifest":  # List
        if not grimoire:
            print("The ledger is hauntingly empty.")
        else:
            print(f"\n--- CURRENT WEIGHT ({len(grimoire)} Souls) ---")
            for i, spirit in enumerate(grimoire, 1):
                print(f"  {i}. {spirit}...")
            print("-----------------------------------")

    elif action == "depart":  # Quit
        if grimoire:
            print(f"You leave, but {len(grimoire)} spirits still follow in your shadow.")
        else:
            print("You slip away into the mist, unburdened.")
        break
    
    else:
        print(f"'{action}' is a word of power unknown to this book.")