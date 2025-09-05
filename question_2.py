x=input("Enter the paragraph (max 100 words)")        #takes input from user
words=x.split()               #the split functions splits the paragraphs into individual word strings
limit=100                    #inputs limit into a variable
if len(words) > limit:      #checks to make sure the words entered arent over the limit
    print("error- too many words")           #error message
else:
            for l in words:              #picks a particular word string from the collection of word strings from the paragraph
               if l== l[::-1]:          #the slicing makes the string reversed and thus checks if the word reads the same forward and backward
                  print(l)              #prints the palindromes

               else:
                  print("no palindrome")                     
  
