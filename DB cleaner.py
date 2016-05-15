#opens the scraped list, removes instances of "hot" and "tequila"
#and tries to format it by separating out the ages 
#(ie 'blanco', 'reposado', etc
#T_DB = open("TequilaDatabase.txt", "r+")
t_list = []
with open("TequilaDatabase.txt", "r+") as DB:
    for line in DB:
        t_list.append(line[:len(line)-1])
no_ws = [x for x in t_list if x not in ['','Hot']]
#removes 'hot' and
#white space
t_list_new = []
count= 0
s= " "
ages = {"blanco":";blanco;", "reposado":";reposado;", "anejo":";anejo;", \
        "silver":";silver;", "plata":";plata;", "platinum":";platinum;"}
reject_list = ["Hot", "Featured","Tequila", ['Hot']]
for tequila in t_list: #for each string (ie. tequila name)
    split_t = tequila.split() #turns each string into a list of the
    #individual words
    to_write = []
    if split_t == ['Hot'] or split_t == [""]:
        pass   #ie, if the list is not *just* "Hot" or empty, do this:
    else:
        for i in split_t:
            if i.lower not in reject_list:
                if i.lower() not in ages:
                    to_write.append(i)
                if i.lower() in ages:
                    to_write.append(ages[i.lower()])

                    
    t_list_new.append(s.join(to_write))

#removes fucking white space in the finished list
while '' in t_list_new:
	t_list_new.remove('')                    
                

'''
            if i in ["Tequila","Hot","Featured"]:   #gets rid of "Tequila" etc 
                split_t.remove(i)
            if i.lower() in ages:  #this is trying to format it
                #so that importing into a spreadsheet is easier
                print(split_t[0])
                loc = split_t.index(i)
                print(loc)
                split_t[loc] = ";" + i + ";"
                print(split_t[loc])
                print("")
'''
        #t_list_new.append(s.join(split_t))

    
        


with open("Cleaned_Tequila Database.txt", "w") as DB:
    for tequila in t_list_new:
        DB.write(tequila + "\n")




