import requests 
from bs4 import BeautifulSoup
import time
import re


URL = "https://www.pluralsight.com/content/pluralsight/en/search.html?categories=course&q=Machine%20Learning" #link to the course

def request():
	page = requests.get(URL)
	soup = BeautifulSoup(page.text, "html.parser")
	url = soup.find_all('div')
	links=[]
	c=1
	for links in url:
		print(links) #getting link
		c+=1
	print("totel ",c)

request()


