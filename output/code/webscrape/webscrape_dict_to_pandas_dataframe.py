#webscrape course information into objects with attributes

import requests
import bs4
import pprint
import pandas as pd

url1 = 'https://www.pcc.edu/schedule/default.cfm?fa=dspCourse2&thisTerm=201704&crsCode=ENGR114&subjCode=ENGR&crsNum=114&topicCode=GE&subtopicCode=ST1&frmtype=ADV&crnList=45437'
url2 = 'https://www.pcc.edu/schedule/default.cfm?fa=dspCourse2&thisTerm=201704&crsCode=ENGR211&subjCode=ENGR&crsNum=211&topicCode=GE&subtopicCode=ST1&crnList=40788,41369'
url3 = 'https://www.pcc.edu/schedule/default.cfm?fa=dspCourse2&thisTerm=201704&crsCode=ENGR221&subjCode=ENGR&crsNum=221&topicCode=GE&subtopicCode=ST1'
url_list = [url1, url2, url3]
#url_list = [url2]

df = pd.DataFrame(columns=['course number', 'course name', 'course department'])

for url in enumerate(url_list):
    r = requests.get(url)
    html = r.content
    soup = bs4.BeautifulSoup(html, 'html.parser')
    page_title = soup.h2.text
    print('\n' + page_title)
    course_number = page_title.split(' ',1)[0]
    course_name = page_title.split(' ',1)[1]
    #df.append=([course_name,course_number,'ENGR'])

print(df)