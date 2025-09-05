x=list([2, 4, 7, 1, 6, 9, 4, 5])          #creates 2 random lists
y=list([5, 3, 6, 9, 2, 8, 8])
for a in x:             #picks up each value of entry in list x
    for b in y:             #picks up each value of entry in list y
        if a==b:           #checks for equality taking each value of x and each value of y
            print(a)             #prints common entries
