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

    

  #once gussed, loop will be break
        break
    elif x > guess:
        print("You gussed too small")
    elif x < guess:
        print("you gussed too high!")


#if gussing is more than required gusses, 
#show this output

if count >= math.log(upper -minor +1 , 2):
    print("\nThe number is %d % x")
    print("\Btter luck next time!")