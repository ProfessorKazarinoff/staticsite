# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 16:34:50 2017

@author: peter.kazarinoff
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 15:49:19 2017

@author: peter.kazarinoff
"""

# webscrape course information including credits, registration, fees and materials


import requests
import bs4
import pandas as pd
import numpy as np

#Fall 2017 URL
url ='https://www.pcc.edu/schedule/default.cfm?fa=dspCourse2&thisTerm=201704&crsCode=ENGR&subjCode=ENGR&crsNum=114&topicCode=GE&subtopicCode='
r = requests.get(url)
html = r.content
soup = bs4.BeautifulSoup(html, 'html.parser')
txt = soup.find("div", {"class": "small-12 columns"})
pTag = txt.p
written_text = pTag.text
print(written_text)
