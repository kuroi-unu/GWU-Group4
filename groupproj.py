#GWU Group 4 Unubold, Qasim, Rachel

print("Welcome to hangman") #welcome message

def hangman():  #creates a function
    guessed_letter = []     #empty lists
    joined_letter = []

    word = input("Enter word:") #input for word 

    for x in range(len(word)):  #creates underscores for length of word
        guessed_letter.append("_")

    while joined_letter != word: #Check if word is guessed or not
        print("Gussed letters:", guessed_letter)    #displays underscores so user can see 
                                                    #how many letters they need
        full = input("Do you want to guess the full word?(Enter y or n)") #guess word or letter
        #if you enter anything besides y or n the above input will be constantly asked until you do
        if full == "y": #loop for word
            guess = input("Enter guess:")
            if guess == word:
                joined_letter = guess
                print("Correct")
            else:
                print("Incorrect, Please try again!")
        elif full == "n":   #loop for letter
            letter = input("Enter letter:")
            if letter in word:  #check if entered letter is in word
                for i, x in enumerate(word): #going through word and replacing underscore with letter
                    if  x == letter:
                        guessed_letter[i] = letter
            
                joined_letter = "".join(guessed_letter) #joining the letters
                print("Correct")
            else: 
                print("Incorrect, Please try again!")
    
    else: #if word is guessed display otherwise loop will continue
        print("You win! The word was:", word)

hangman()   #calls funtion hangman once when program is ran
count = 0
while count < 1:    #creates loop 
    restart = input("Do you want to play again? Enter y or n:") 
    if restart == "y":  #if user wants to play again calls function hangman
        hangman()
    elif restart == "n": #if user doesn't want to play again ends loop
        print("Goodbye")
        break   #breaks the infinite loop


#need a losing condition
#need to import turtle and draw hangman