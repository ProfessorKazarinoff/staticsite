# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 15:49:19 2017

@author: peter.kazarinoff
"""

#webscrape multiple course information pages add information items to a dictionary

import requests
import bs4

url = 'https://www.pcc.edu/schedule/default.cfm?fa=dspTopicDetails&thisTerm=201704&topicid=GE&type=Credit'
#url = 'https://www.pcc.edu/schedule/default.cfm?fa=dspTopicDetails&thisTerm=201704&topicid=MTH&type=Credit'
#url = 'https://www.pcc.edu/schedule/default.cfm?fa=dspTopicDetails&thisTerm=201704&topicid=ESOL&type=Credit'

r = requests.get(url)
html = r.content
soup = bs4.BeautifulSoup(html, 'html.parser')
url_list =[]
for a in soup.select('dl.course-list dd a[href]'):
    codeurl = a['href']
    pcc_url = 'https://www.pcc.edu/schedule/' + codeurl
    url_list.append(pcc_url)
#print(url_list)

for url in url_list:
     r = requests.get(url)
     html = r.content
     soup = bs4.BeautifulSoup(html, 'html.parser')
     page_title = soup.h2.text
     print('\n' + page_title)
     course_number = page_title.split(' ',1)[0]
     course_name = page_title.split(' ',1)[1]
     course1_dict = {'number': course_number, 'name': course_name}
 
     print('course number: {}'.format(course_number))
     print('course name: {}'.format(course_name))