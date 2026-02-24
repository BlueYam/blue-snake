from random import randint

money = 2000
pin = randint(1, 5)

print("---- WELCOME TO THE CRAZY ATM ----")
print(f"(Psst... the secret pin is {pin})")

guess = int(input("Guess the PIN (1-5) to enter: "))

if guess != pin:
    print("WRONG! I'm keeping your 2000 bucks. Goodbye!")
else:
    print("\nLucky guess... I'll let you in this time.")
 
    while True:
        print(f"\n[ Current Balance: ${money} ]")
        action = input("What now? (add / withdraw / quit): ").lower()

        if action == "add":
            amount = int(input("How much are you giving me? "))
            money += amount
            print(f"I guess I'll take that ${amount}...")

        elif action == "withdraw":
            amount = int(input("How much do you want? "))
            if amount > money:
                print("Nice try! You aren't that rich.")
            else:
                money -= amount
                print(f"Fine. Here is your ${amount}. My vault feels empty now.")

        elif action == "quit":
            print("Don't come back soon!")
            break 
        
        else:
            print(f"I don't speak '{action}'. Try again!")