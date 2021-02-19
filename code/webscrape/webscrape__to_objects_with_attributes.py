#webscrape course information into objects with attributes

import requests
import bs4

class course:

    def __init__(self):
        self.number = []
        self.name = []
        self.dept = []

url1 = 'https://www.pcc.edu/schedule/default.cfm?fa=dspCourse2&thisTerm=201704&crsCode=ENGR114&subjCode=ENGR&crsNum=114&topicCode=GE&subtopicCode=ST1&frmtype=ADV&crnList=45437'
url2 = 'https://www.pcc.edu/schedule/default.cfm?fa=dspCourse2&thisTerm=201704&crsCode=ENGR211&subjCode=ENGR&crsNum=211&topicCode=GE&subtopicCode=ST1&crnList=40788,41369'
url3 = 'https://www.pcc.edu/schedule/default.cfm?fa=dspCourse2&thisTerm=201704&crsCode=ENGR221&subjCode=ENGR&crsNum=221&topicCode=GE&subtopicCode=ST1'
#url_list = [url1, url2, url3]
url_list = [url1]

course1=course()

for url in url_list:
    r = requests.get(url)
    html = r.content
    soup = bs4.BeautifulSoup(html, 'html.parser')
    page_title = soup.h2.text
    print('\n' + page_title)
    course_number = page_title.split(' ',1)[0]
    course_name = page_title.split(' ',1)[1]
    course1.name=course_name
    course1.number=course_number

    print('course number: {}'.format(course1.number))
    print('course name: {}'.format(course1.name))
