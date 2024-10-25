### Part Three -- your code goes here. 
def main():
    list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    list.remove(1)
    list.extend([7, 8])
    list2 = sorted(list)
    print(list2)
    
main()