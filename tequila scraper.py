from bs4 import BeautifulSoup
import requests
from datetime import datetime

'''

http://www.tequila.net/advanced-tequila-search/tag/tnom/1122/
'''
file_name = "Tequila_database_{}.txt".format(str(datetime.now().day) + "-" + str(datetime.now().month))
open("file_name", "w")
TequilaDatabase = open("file_name", "w")

a = 1050 #1000 for whole range
b = 1100 #2000 for whole range
t_list = []
pages_visited = 0
successful_pages = 0
for n in range(a,b): #change to (1000,2000) to get the entire range
    results = True
    page_num = 1
    while results == True:
        r = requests.get("http://www.tequila.net/advanced-tequila-search/tag/tnom/{}.html?page={}".format(str(n),str(page_num)))
        pages_visited += 1
        site = r.text
        soup = BeautifulSoup(site, "html.parser")
        #checks to see if page returns no results
        #if returns no results, there will be a
        #link saying "return to previous page"
        #looks for that link
        checker = soup.find_all("a")
        for link in checker:
            link_h = link.get("href")
            if link_h == "javascript:window.history.go(-1)":
                results = False
        if results == False:
            break
        g_data = soup.find_all("div", {"class":"jrContentTitle"})
        s = " "
        for item in g_data:
            
            '''i = item.text
            split_i = i.split()
            print("Split I =")
            print(split_i)
            for t in split_i:
                if t.lower() == "hot" or t.lower() == "tequila":
                    split_i.remove(t)
                else:
                    pass
        new_item = s.join(split_i)
        TequilaDatabase.write(new_item + "\n")
        t_list.append(new_item)
        '''
            t_list.append(item.text) #[:(len(item.text)-7)]
            TequilaDatabase.write(item.text + "\n")
        
            
            #print(item.text[:(len(item.text)-7)])
        page_num += 1
        successful_pages += 1
    print(n)


TequilaDatabase.close()

print("There were {} pages visited, and {} successful pages loaded.".format(pages_visited, successful_pages))

'''
n = 1122
page_num = 4
r = requests.get("http://www.tequila.net/advanced-tequila-search/tag/tnom/{}.html?page={}".format(str(n),str(page_num)))
site = r.text
soup = BeautifulSoup(site, "html.parser")
t_list = []
checker = soup.find_all("a")
for link in checker:
    link_h = link.get("href")
    if link_h == "javascript:window.history.go(-1)":
        print("404!!")
#print(checker)
'''    


'''
g_data = soup.find_all("div", {"class":"jrContentTitle"})
for item in g_data:
    t_list.append(item.text[:(len(item.text)-7)])
    print(item.text[:(len(item.text)-7)])
'''

#print(t_list)
