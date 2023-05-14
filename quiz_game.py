print("Welcome to my biblical quiz!") # pentru a afisa text in consola se foloseste metoda print(). 
# Un string este incapsulat intre doua ghilimele

playing = input("Do you want to play the game (yes/no)? ") # afisez un prompt text si citesc raspunsul user-ului
# folosesc playing.lower() pentru a transforma raspunsul primit intr-un text lowerCase
if playing.lower() != "yes": # rezultatul acestei conditii este True
    quit() # daca raspunsul este orice altceva inafara de yes, atunci se termina rularea programului 

score = 0 # de fiecare data cand raspunsul este corect incrementez variabila scor

answer = input("Which is the first book of the Bible? ") # afisez un prompt text cu intrebarea si citesc raspunsul introdus de user
if answer.lower() == "genesis": # verific raspunsul cu o functie decizionala
    print("Correct!") # afisez daca raspunsul este corect
    score += 1
else: 
    print("Incorrect! The correct answer is \'genesis\'") # afisez daca raspunsul este gresit

answer = int(input("How many books has the Bible? "))
if answer == 66:
    print("Correct!")
    score += 1
else: 
    print("Incorrect! The correct answer is 66")

answer = input("Which is the first letter of Paul? ")
if answer.lower() == "1 Thessalonians":
    print("Correct!")
    score += 1
else: 
    print("Incorrect! The correct answer is \'1 Thessalonians\'")

answer = input("Which is the last book in the Bible? ")
if answer.lower() == "revelation":
    print("Correct!")
    score += 1
else: 
    print("Incorrect! The correct answer is \'revelation\'")

print("You got " + str(score) + " questions correct!")