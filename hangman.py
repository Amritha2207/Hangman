secretWord="hangman"
lettersGuessed=""
failureCount = 6

while failureCount > 0:
    guess = input("Enter a letter: ")

    if guess in secretWord:
        print(f"Correct!There is one or more {guess} in the secretWord.")
    else:
        failureCount -= 1
        print(f"Incorrect.There are no {guess} in the secret word.{failureCount} turn(s) left.")
    lettersGuessed = lettersGuessed + guess
    wrongLetterCount = 0
    for letter in secretWord:
        if letter in lettersGuessed:
            print(f"{letter}",end="")
        else:
            print("_",end="")
            wrongLetterCount += 1
    if wrongLetterCount == 0:
        print(f"Congratulations! The secret word was: {secretWord}.You Won!")
        break
else:
    print("Sorry!.You didnt win this time.Try Again.")
