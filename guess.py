import random


fruits = [
    "apple", "mango", "grape", "peach", "lemon",
    "guava", "papaya", "cherry", "banana", "orange",
    "melon", "plum", "apricot", "fig", "lime",
    "kiwi", "pear", "berry", "coconut", "pineapple",
    "lychee", "avocado", "passion", "jackfruit", "dragonfruit",
    "watermelon", "blueberry", "raspberry", "strawberry", "tangerine"
]

animals = [
    "tiger", "elephant", "dolphin", "penguin", "giraffe",
    "zebra", "lion", "cheetah", "gorilla", "panther",
    "jaguar", "wolf", "bear", "eagle", "shark",
    "octopus", "crocodile", "flamingo", "kangaroo", "koala",
    "leopard", "mongoose", "platypus", "hedgehog", "chameleon",
    "alligator", "rhinoceros", "hippopotamus", "chimpanzee", "orangutan"
]

countries = [
    "brazil", "france", "japan", "india", "canada",
    "egypt", "kenya", "mexico", "spain", "italy",
    "china", "russia", "ghana", "turkey", "greece",
    "sweden", "norway", "poland", "austria", "belgium",
    "nigeria", "ethiopia", "morocco", "malaysia", "vietnam",
    "argentina", "colombia", "portugal", "thailand", "indonesia"
]

all_words = fruits + animals + countries



repeat = True

while repeat:
    guess_word = random.choice(all_words)  #pick new word at randowm each time
    guesses = ""
    chances = 10

    if guess_word in animals:
        print("It is an animal")

    if guess_word in fruits:
        print("It is a fruit")
    if guess_word in countries:
        print("It is a country")        

    while chances > 0:
        
        failed = 0
        display = []
        for char in guess_word:
            if char in guesses:
                display.append(char)
            else:
                display.append("_")
                failed += 1

        print(" ".join(display))

        
        if failed == 0:
            print("Congrats! You win!")
            print("The word was:", guess_word)
            break

        #player input
        guess = input("Guess a character: ").lower()
        guesses += guess

        
        if guess not in guess_word:
            chances -= 1
            print("Wrong guess!")
            print(f"You have {chances} chances left.")
        else:
            print("Correct!")

    
    if chances == 0:
        print("You lost! The word was:", guess_word)

    
    again = input("Retry? Press Y to continue or N to stop: ").upper()
    if again == "N":
        repeat = False

print("Thanks for playing!")