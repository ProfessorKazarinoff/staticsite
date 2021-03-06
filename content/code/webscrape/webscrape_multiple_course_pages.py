#webscrape multiple course information pages add information items to a dictionary

import requests
import bs4

url1 = 'https://www.pcc.edu/schedule/default.cfm?fa=dspCourse2&thisTerm=201704&crsCode=ENGR&subjCode=ENGR&crsNum=114&topicCode=GE&subtopicCode=&crnList=45437'
url2 = 'https://www.pcc.edu/schedule/default.cfm?fa=dspCourse2&thisTerm=201704&crsCode=ENGR&subjCode=ENGR&crsNum=100&topicCode=GE&subtopicCode=&crnList=40782,46630'
url3 = 'https://www.pcc.edu/schedule/default.cfm?fa=dspCourse2&thisTerm=201704&crsCode=ENGR&subjCode=ENGR&crsNum=211&topicCode=GE&subtopicCode=&crnList=40788,41369'
url4 = 'https://www.pcc.edu/schedule/default.cfm?fa=dspCourse2&thisTerm=201704&crsCode=ENGR&subjCode=ENGR&crsNum=102&topicCode=GE&subtopicCode=&crnList=40787'
url_list = [url1, url2, url3, url4]

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
