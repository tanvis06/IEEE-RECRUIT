cutoffs=list([("Pilani","CS",327),("Pilani","Chemical",247),("Pilani","MSc Eco",271),("Pilani","MSc Bio",236),("Goa","CS",301),("Goa","Chemical",239),("Goa","MSc Eco",263),("Goa","MSc Bio",234),("Hyderabad","CS",298),("Hyderabad","Chemical",238),("Hyderabad","MSc Eco",261),("Hyderabad","MSc Bio",234)])      #creates a list of the required informati
dictionary =  {}                        #creates an empty dictionary for us to add values
for campus, course, score in cutoffs:       #loop to create a dictionary key for every campus listed
    if campus not in dictionary:
        dictionary[campus] = {}        
    dictionary[campus][course] = score          #adds course as the secondary key inside the campus dictionary and sets the score as the value
print(dictionary)         #prints final dictionary
