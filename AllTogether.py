### Part Four -- your code goes here. 
import math
import random


def main():
    count = 0
    no_list = []
    
    while count < 10:
        rn = random.randint(1, 100)
        no_list.append(rn)
        count += 1
        
    print(no_list)
    main_2(no_list)

def main_2(no_list):
    for even_no in no_list[:]:
        while even_no % 2 == 0:
            no_list.remove(even_no)
            break
            
    print(no_list)
      
           
main()