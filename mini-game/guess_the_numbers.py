from random import randint

nums = randint(1, 20)
counter = 0
chance = 5

print("---- Welcome To BlueYam Guess the number game. ----")
while counter < chance:
    try:
        answer = int(
            input(f"Enter a number between 1-20 (Attempt: {counter + 1}/{chance}): ")
        )
        counter += 1

        if answer == nums:
            print(f"Congrats. It was {nums}. You got it right in {counter} tries.")
            break
        elif answer < nums:
            print("Too low!")
        elif answer > nums:
            print("Too high!")
    except ValueError:
        print("Enter a whole, valid numbers please.")
