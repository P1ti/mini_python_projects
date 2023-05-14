import random # import random module

max_number = input("Type a number ")
guesses = 0

if max_number.isdigit(): # daca raspunsul primit este string il convertesc in int
    max_number = int(max_number)

    if max_number <= 0:
        print("Type a number larger than 0 next time!")
        quit()
else:
    print("Please type a number next time!")
    quit()

# random_number = random.randrange(-1, 5) # random.randrange(start, stop) genereaza un numar care incepe de la numarul oferit ca punct de start
# adica -1, inclusiv numarul asta si pana la 5, dar fara 5, adica (-1, 0, 1, 2, 3, 4)
random_number = random.randint(0, max_number) # generez un numar random de la 0 pana la 5, inclusiv 5

while True:
    guesses += 1
    user_answer = input("Make a guess: ")
    if user_answer.isdigit():
        user_answer = int(user_answer)
    else: 
        print("Type a number next time!")
        continue # continua loopul de la linia 20, lasa userul sa dea un alt raspuns

    if user_answer == random_number:
        print("You got it!")
        break # daca numarul a fost gasit termina loopul
    elif user_answer > random_number: # verific unde se afla raspunsul primit fata de raspunsul userului
        print("You are above the number")
    else: 
        print("You were below the number!")

print("You got it in ", guesses, " guesses")