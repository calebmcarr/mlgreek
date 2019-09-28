from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

#Set up appropriate urls
url = 'http://www.poesialatina.it/_ns/Greek/testi/p/MappaProsaGr.html'
text_url = 'http://www.poesialatina.it/_ns/Greek/testi'

#Initiate BS object
html = urlopen(url)
bs = BeautifulSoup(html.read(), 'html.parser')
links = []
#collect all div object with authors
#returns divs filled with links to greek text
authors = bs.findAll('div',{'class':'collapse list-group-submenu'})
for i in range(len(authors)):
    for j in range(40):
        try:
            if 'href'in str(authors[i].contents[j]):
                #if there is a link, get it and append the link so it can be searched
                link = authors[i].contents[j].get('href')
                #each link has the Unix .. designator so the first two characters are ripped off
                link = link[2:]
                link = text_url+link
                links.append(link)
            else:
                pass
        except:
            pass
links = links[1:]
#With all links compiled, grab the text out of them

#compile needed regex expressions
r1 = re.compile(r'\W')
r2 = re.compile(r'\d')

#Double for loop to get the text for every html file gathered
#and turn it into a .txt file
for i in range(len(links)):
    try:
        complete_text = []
        html2 = urlopen(links[i])
        bs2 = BeautifulSoup(html2.read(), 'html.parser')
        lines = bs2.findAll('p')
        for j in range(len(lines)):
            #regex splits get rid of unwanted characters
            text = ' '.join(r1.split(lines[j].text))
            text = ' '.join(r2.split(text))
            complete_text.append(text)
        #Following is some poor man's Regex
        title = links[i].strip(text_url)
        title = title.strip('.html')
        title = title.replace('/','_')
        title = './Texts/'+title+'.txt'
        f = open(title,'w')
        f.write(' '.join(complete_text))
        f.close()
        print('File '+str(i)+" added.  Title: "+links[i])
    except:
        print('File '+str(i)+'failed.')
