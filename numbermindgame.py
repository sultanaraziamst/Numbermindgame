import random
import math

#will enter input here

minor  = int(input("Enter minor bound:-"))

#will enter input here
upper  = int(input("Enter upper bound:-"))

#generate random number between 
#the minor and upper

x = random.randint(minor, upper)
print("\n\tYou'hv only",
round(math.log(upper-minor + 1 , 2)),
"chances to guess the integer!\n")


#initializing the number guesses. 

count = 0

#for calculation of minimum number of 
#guesses depend upon range

while count < math.log(upper-minor + 1, 2):
    count += 1

    #taking guessing number as input 
    guess = int (input("Guess a number:-"))
    
    #condition testing
    if x == guess:
        print("Congratulations you did it in ",
        count, " try")

      


