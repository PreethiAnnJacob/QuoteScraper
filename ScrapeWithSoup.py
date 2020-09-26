import requests # send HTTP requests and recive responses using python
import html5lib # An HTML parser
from bs4 import BeautifulSoup # Web scraper
import csv # file to read/write Comma Separated Value(.csv)

#pretty print the [parsed HTML content from the requested website
URL="https://www.passiton.com/inspirational-quotes"
response = requests.get(URL)
rawHTML = response.content 
soup = BeautifulSoup(rawHTML,'html5lib') #parse tree

# pretty print in the console
# print(soup.prettify())

'''Save the HTML content to file'''
#Specify encoding=UTF-8 to avoid issues in converting to string
with open("output.html", "w",encoding='utf-8') as file:
    file.write(str(soup))

'''Scraping quotes and related other items from HTML'''
#List to store quotes
quotes=[]
table=soup.find('div',attrs={'id':'all_quotes'})
for row in table.findAll('div',attrs={"class":"col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top"}):
	quote={} # empty dictionary
	quote['theme']=row.h5.text
	quote['url']=row.a['href']
	quote['img']=row.img['src']
	quote['lines']=row.img['alt'].split("#")[0]
	quote['author']=row.img['alt'].split("#")[1]
	quotes.append(quote)

'''Save quotes to csv file'''
filename="quotes.csv"
with open(filename,'w',newline='\n') as file:
	# DictWriter can map dictionary to rows
	w=csv.DictWriter(file,['theme','url','img','lines','author'])
	# write  row with the fieldnames specified
	w.writeheader()
	#write values into the 
	for quote in quotes:
		w.writerow(quote)

