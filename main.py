import random
print("The task is to guess the correct number (means the same number as assumed by the computer)")
print("Guess the number between 1-50" )
print("LET'S BREAK THE RECORD")
n= random.randint(1,50)

a=-1
guesses=1
while(a!= n):
    a=int(input("Guess the number:"))
    if(a>n):
        print("Enter the smaller number :( ")
        guesses=guesses+1
    elif(a<n):
        print("Enter the higher number :( ")
        guesses=guesses+1

print(f"Yeahhh!! You have guessed the number {n} correctly in {guesses} attempts :)")
     