word = input("Enter a word:")
g = [] 
a = []
print("word is:", g)
while a != word: 
    full = input("Do you want to guess the full word?(Enter y or n)")
    if full == "y":
        guess = input("Enter a guess:")
        if guess == word:
            a = guess
        else:
            print("Guess is wrong")
    else:
        letter = input("Enter a letter:")
        if letter in word:
            g += letter
            a = "".join(g)
            print("Guess is correct")
            print(a)
        else: 
            print("Guess is wrong")
else: 
    print("You have guessed the word")