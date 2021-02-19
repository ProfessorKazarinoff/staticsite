# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 16:34:50 2017

@author: peter.kazarinoff
"""

#webscrape multiple course information pages add information items to a dictionary

import requests
import bs4
import pandas as pd
import numpy as np
df = pd.DataFrame(index=np.arange(0,500),columns=('course number','course name'))
i=0
#Winter 2017 URL that lists all of the for-credit classes in Winter 2017
# Go to PCC.edu --> Class Schedule --> Winter 2018 Credit Classes
url = 'https://www.pcc.edu/schedule/default.cfm?fa=dspTopic&thisTerm=201801&type=Credit'
#url = 'https://www.pcc.edu/schedule/default.cfm?fa=dspTopicDetails&thisTerm=201704&topicid=MTH&type=Credit'
#url = 'https://www.pcc.edu/schedule/default.cfm?fa=dspTopicDetails&thisTerm=201704&topicid=ESOL&type=Credit'

r = requests.get(url)
html = r.content
soup = bs4.BeautifulSoup(html, 'html.parser')
url_dept_list =[]
for a in soup.select('div.indexlist a[href]'):
    code_url = a['href']
    pcc_url = 'https://www.pcc.edu/schedule/' + code_url
    url_dept_list.append(pcc_url)
print(url_dept_list)

for dept_url in url_dept_list:
    r = requests.get(dept_url)
    html = r.content
    soup = bs4.BeautifulSoup(html, 'html.parser')
    url_class_list =[]
    for a in soup.select('dl.course-list dd a[href]'):
        codeurl = a['href']
        pcc_url = 'https://www.pcc.edu/schedule/' + codeurl
        url_class_list.append(pcc_url)
    for class_url in url_class_list:
        r = requests.get(class_url)
        html = r.content
        soup = bs4.BeautifulSoup(html, 'html.parser')
        page_title = soup.h2.text
        print('\n' + page_title)
        course_number = page_title.split(' ',1)[0]
        course_name = page_title.split(' ',1)[1]
        df.loc[i] = [course_number, course_name]
        #course1_dict = {'number': course_number, 'name': course_name}
        print('course number: {}'.format(course_number))
        print('course name: {}'.format(course_name))
        
        print('class number ' +str(i+1))
        print()
        i=i+1
print(df)

# The dataframe may contain rows with 'Class' and 'Schedule' listed instead of 'ENGR101' intro to engineering. These can be cleaned out with:
df = df[df['course number'] !='Class']
df.to_csv('classes.csv')