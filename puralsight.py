import requests 
from bs4 import BeautifulSoup
import time
import re


URL = "https://www.pluralsight.com/browse/machine-learning" #link to the course

def request():
	page = requests.get(URL)
	soup = BeautifulSoup(page.text, "html.parser")
	url = soup.find_all('a',class_="course-item columns")
	links=[]
	for links in url:
		print(links.get('href')) #link collection


request()


