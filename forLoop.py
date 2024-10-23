### Part One -- your code goes here. 
import math     #This imports the maths module into the program

def main():     #Defines the function main
    base = list(range(1, 11, 1))        #This makes a list from 1 to 10 using "range()", and then puts it in a list using "list()". It is then labled "base".
    for x in base:      #This is a for loop which assigns "x" to be each value in the "base" function.
        print("The square of", x, "is", pow(x, 2))      #This prints the square of x - all the values in the list.

main()