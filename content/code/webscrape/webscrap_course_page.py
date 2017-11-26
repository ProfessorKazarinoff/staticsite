#Scrape a course information page

import requests
import bs4
url = 'https://www.pcc.edu/schedule/default.cfm?fa=dspCourse2&thisTerm=201704&crsCode=ENGR211&subjCode=ENGR&crsNum=211&topicCode=GE&subtopicCode=ST1'
#url = 'https://www.pcc.edu/schedule/default.cfm?fa=dspCourse2&thisTerm=201704&crsCode=ENGR114&subjCode=ENGR&crsNum=114&topicCode=GE&subtopicCode=ST1&frmtype=ADV&crnList=45437'
url = 'https://www.pcc.edu/schedule/default.cfm?fa=dspCourse2&thisTerm=201704&crsCode=ENGR101&subjCode=ENGR&crsNum=101&topicCode=GE&subtopicCode=101'
r = requests.get(url)
html = r.content
soup = bs4.BeautifulSoup(html, 'html.parser')
page_title = soup.h2.text
page_text = soup.find('div', attrs={'id':'content'}).find('p').text.splitlines()[0]
CRN = soup.find('tr',attrs={'class':'data-row'}).td.text
course_credits = soup.find('dd').text
print(page_title)
course_number = page_title.split(' ',1)[0]
course_name = page_title.split(' ',1)[1]

print('This is the course number: {}'.format(course_number))
print('This is the course name: {}'.format(course_name))
print('This is the course description: {}'.format(page_text))
print('This is the course CRN #: {}'.format(CRN))
print('This is the course credits: {}'.format(course_credits))