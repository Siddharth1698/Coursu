import requests 
from bs4 import BeautifulSoup
import time

keyword = "machine learing" #keyword want to search 

def request():
	URL = "https://www.edx.org/search?tab=course&q="+keyword
	page = requests.get(URL)
	soup = BeautifulSoup(page.content, 'lxml')
	tag = soup.find(lambda tag: tag.name == 'div' )
	print(page)
	print(tag)
	#tables = soup.find_all('ul')
	#initialCount = len(tables)
	#return initialCount	

request()


