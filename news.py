import  urllib2
from bs4 import BeautifulSoup


print("Enter the date(DD/MM/YY) to view headlines:")
date = raw_input()

date = date.replace("/","");

url = 'http://www.rediff.com/issues/' + date + 'hl.html'

page = urllib2.urlopen(url);
html = BeautifulSoup(page,"lxml")
count=0
for i in html.find_all('div',attrs={'id':'hdtab1'}):
    for j in i('a',attrs={'target':"_new"}):
        if count==0:
           count=count+1
           continue
        print(j.text)
        print(j.next_sibling)

