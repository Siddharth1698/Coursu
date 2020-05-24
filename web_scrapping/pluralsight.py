import requests
from bs4 import BeautifulSoup
import time
import re

#link for multiple catagory
stack = []
sd = "software-development"
cc = "cloud-computing"
ml = "machine-learning"
io = "it-ops"
its = "information-cyber-security"
dp = "data-professional"

stack = [sd,cc,ml,io,its,dp]  #list for diff links
i = 0   #loop variable for list

baseURL = "https://www.pluralsight.com/browse/" #base link to the course

course_title = []
course_level = []
course_link = []

#Req Fn start
def request(URL):	#Req function
	page = requests.get(URL)
	soup = BeautifulSoup(page.text, "html.parser")
	url = soup.find_all('a',class_="course-item columns") #course details class
	links=[]
	for links in url:
		courseTitle = links.find('div', class_="course-item__title").get_text()	#course title
		courseLevel = links.find('div', class_="course--item__list course-item__level").get_text()
		courseLink = links.get('href')	#course link
		course_title.append(courseTitle)
		course_link.append(courseLink)
		course_level.append(courseLevel)




#Req fn End


for i in range(len(stack)):
	link = baseURL+stack[i]
	request(link)




import pandas as pd
courses_df = pd.DataFrame({'course_title': course_title,
                          'course_link': course_link,
                          'course_level':course_level})
courses_df = courses_df.sort_values('course_title')
courses_df.to_csv('pluralsight_Courses.csv')
