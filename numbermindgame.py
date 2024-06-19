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


