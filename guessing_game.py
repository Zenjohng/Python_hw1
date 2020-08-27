# Number Guessing  Game
import random
#assign secrectNumber to random number from range 1-10, inclusive of 10
secrectNumber = random.randint (1, 11)
#initialize number or guesses to 1 and call it guess
numGuesses = 1
#prompt user to enter their name and enter their guess
name = int (input("Enter your name: ))
   print("name")
guess = int(input("Enter a guess:"))
   print("guess")

#create a while loop thats exits when the guess is equal to the secrect number
#guess the the secrectNumber if guess is > than secrect number the user is will recieve an alert that the number is less than guess
# if guess is < than secrect number the user is will recieve an alert the number isgreater than guess
 #if the guess is not equal to the secrect number, do the while loop.
while (guess != secrectNumber > 5):
    if guess > secrectNumber:
      print ("the secrect number is less than "+ str(guess))

      else:
        print ("the secrect number is greater than " + str(guess))
        numGuesses += 1
        if guess == number:
          break
        #The number of guesses is incremented by +1
        
        #if the guess is not equal to the secrect number, guess again. The user is prompted to ebnter a number
        guess = int (input("Enter a number"))

        print (" Zee gives congrats to" +str(name) +"! the number is" +str(secrectNumber))
        print ("it took you" +str(numGuesses) + "guesses. Great job!")
       

   



