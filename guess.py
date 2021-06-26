from random import randint

start = 1 

end = 1000

value = randint(start ,end)

print("The Computer choose a number Between ", start,"and", end)

guess = None

while guess != value:
    text = input("Guess the number: ")
    guess = int(text)

    if guess < value:
        print("The number is Higher")
    elif guess > value:
        print("The number is Lower")

print("Congratulation!!! You guessed the number. You Won 🔥💥")
        