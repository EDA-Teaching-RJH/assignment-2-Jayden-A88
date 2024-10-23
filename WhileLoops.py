### Part Two -- your code goes here. 
import math
import random

def main():
    rn = random.randint(1, 100)
    no = int(input("Guess the number: "))                             
    rep(rn, no)
    
    
    
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