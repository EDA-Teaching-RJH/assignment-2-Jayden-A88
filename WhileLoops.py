### Part Two -- your code goes here. 
import math

#Imports the maths commands.

import random

#Imports the random commands.

def main():
    rn = random.randint(1, 100)
    
    #Assigns the random numnber to rn
    
    no = int(input("Guess the number: "))   
    
    #The user input gets assigned to no
                              
    rep(rn, no)
    
    #Repeat loop, which asks for inputs untill the input matches the number generated.
    
    
    
def rep(rn, no):
    while rn != no:
        
        if no < rn:
            print("Too low!")
        else:
            print("Too high!")
        
        x = input("This is not the right number. Want to guess again? (yes/no): ").strip().lower()
        
        if x == "yes":
            no = int(input("Guess the number: "))
        elif x == "no":
            print("The number was", rn)
            print("Quiting Application...")
            break
    else:
        print("Correct. The number was", rn)
        print("Quiting Application...")
           
main()