n=int(input("enter number of star lines")) #takes input from user
for i in range(n):   #decides the no of times the program will run
    for j in range(i,n):   #prints the number of empty spaces required in each line to make the star pattern right aligned
        print(' ',end=' ')
    for j in range(i+1):   #prints the number of stars required in each line according to the no of spaces already there
        print('*',end=' ')
    print()      #prints final program
