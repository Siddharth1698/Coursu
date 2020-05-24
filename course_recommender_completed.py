import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

###### helper functions. Use them when needed #######

def get_title_from_index(index):
    return df[df.index == index]["course_title"].values[0]
def get_index_from_title(title):
    return df[df.course_title == title]["index"].values[0]


##################################################

##Step 1: Read CSV File
df = pd.read_csv("complete_course_data.csv")

##Step 2: Select Features
features = ["course_title","platform","level"]

##Step 3: Create a column in DF which combines all selected features
for feature in features:
    df[feature] = df[feature].fillna('')

def combine_features(row):
    try:
        return row['course_title']+" "+row['platform']+" "+row['level']
    except:
        print ("Error:", row)	

df["combined_features"] = df.apply(combine_features,axis=1)



##Step 4: Create count matrix from this new combined column
cv = CountVectorizer()

count_matrix = cv.fit_transform(df["combined_features"])

##Step 5: Compute the Cosine Similarity based on the count_matrix
cosine_sim = cosine_similarity(count_matrix) 
course_user_likes = input("Search course of Your choice : ")

## Step 6: Get index of this courses from its title
course_index = get_index_from_title(course_user_likes)

similar_courses = list(enumerate(cosine_sim[course_index]))

## Step 7: Get a list of similar courses in descending order of similarity score
sorted_similar_courses = sorted(similar_courses,key=lambda x:x[1],reverse=True)[1:]

## Step 8: Print titles of 5 courses

pickle.dump(sorted_similar_courses,open("model.pkl","wb"))
model = pickle.load((open('model.pkl','rb')))