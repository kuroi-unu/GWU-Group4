#GWU Group 4 Unubold, Qasim, Rachel
import turtle   #import turtle

print("Welcome to hangman.") #welcome message

wn = turtle.Screen()    #turtle window
wn.setup(width=400, height=600) #resizee window
puppet = turtle.Turtle()    #new turtle

#hangman platform
def platform():
    puppet.right(90)   
    puppet.forward(200)
    puppet.left(90)
    puppet.forward(50)
    puppet.forward(-100)
    puppet.forward(50)
    puppet.left(90)
    puppet.forward(200)
    puppet.right(90)
    puppet.forward(60)
    puppet.right(90)
    puppet.forward(30)

#hangman 
def head():
    puppet.right(90)   #head
    puppet.circle(10)
def body():
    puppet.penup() #body
    puppet.left(90)    
    puppet.forward(20)
    puppet.pendown()
    puppet.forward(50)
    puppet.forward(-40)
def r_arm():
    puppet.right(45)   #right arm
    puppet.forward(20)
    puppet.forward(-20)
def l_arm():
    puppet.left(90)    #left arm
    puppet.forward(20)
    puppet.forward(-20)
    puppet.right(45)
def r_leg():
    puppet.forward(37) #right leg
    puppet.right(45)
    puppet.forward(20)
    puppet.forward(-20)
def l_leg():
    puppet.left(90)    #left leg
    puppet.forward(20)
    puppet.forward(-20)
    
def hangman():  #creates a function
    life = 6    #6 lives, one for each of the body part - head, body, 2 arm, 2 legs = 6
    guessed_letter = []     #empty lists
    joined_letter = []
    win = True  
    word = input("Enter word:") #input for word 
    print("You have ", life, "lives remaining.")

    for x in range(len(word)):  #creates underscores for length of word
        guessed_letter.append("_")

    while win == True: 
        if life == 1:   #lose condition ; when lives reach 0 the player loses
            win = False
        elif joined_letter == word: #Win condition ; Check if word is guessed or not, if yes you win and break 
            print("You win! The word was:", word)
            wn.reset()  #reset turtle window
            break
        
        print("Gussed letters:", guessed_letter)    #displays underscores so user can see 
                                                    #how many letters they need
        full = input("Do you want to guess the full word?(Enter y or n)") #guess word or letter
        #if you enter anything besides y or n the above input will be constantly asked until you do
        if full == "y": #loop for word
            guess = input("Enter guess:")
            if guess == word:   #check if full word guess is correct
                joined_letter = guess
                print("Correct")
            else:
                print("Incorrect, Please try again!")
                life = life - 1
                if life == 5:   #check life and call hangman body part to draw on turtle window
                    head()
                elif life == 4:
                    body()
                elif life == 3:
                    r_arm()
                elif life == 2:
                    l_arm()
                elif life == 1:
                    r_leg()
                print("You have ", life, "lives remaining.")
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
                life = life - 1 
                if life == 5:   #check life and call hangman body part to draw on turtle window
                    head()
                elif life == 4:
                    body()
                elif life == 3:
                    r_arm()
                elif life == 2:
                    l_arm()
                elif life == 1:
                    r_leg()
                print("You have ", life, "lives remaining.")
                
    
    else: #if life is 0 you lose. 
        l_leg() #draw left leg of hangman 
        print("You lose! You have ran out of life.The word was:", word)
        wn.reset()

platform() #calls function platform once when program is ran
hangman()   #calls funtion hangman once when program is ran
count = 0
while count < 1:    #creates loop 
    restart = input("Do you want to play again? Enter y or n:") 
    if restart == "y":  #if user wants to play again calls function hangman
        platform()  #calls function if player wants to play again
        hangman()
    elif restart == "n": #if user doesn't want to play again ends loop
        print("Goodbye")
        break   #breaks the infinite loop
