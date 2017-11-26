Title: Using Python and Beautiful Soup - webscrape into objects with attributes
Date: 2017-09-20 10:12
Modified: 2017-09-20 19:55
Status: Draft
Category: Python
Tags: python, beautiful soup, web scraping, object-oriented programming 
Slug: python-and-beautifulsoup-webscrape-objects-with-attributes
Authors: Peter Kazarinoff
Series: Webscrape with Python and BeautifulSoup
series_index: 3
Summary:

In the previous post we scraped a couple of college course web pages and pulled out the course number and name. As a refresher, pull up the conda prompt from the windows start menu and ```activate``` the ```webscrape``` virtual environment.

```terminal
C:\Users\user.name>activate webscrape

(webscrape) C:\Users\user.name>
````

Are the modules beautiful soup and requests installed in the virtual environment? We can check with ```pip freeze```

```terminal


```

Then run our old script by ```cd``` ing into the directory with the webscrape_course_page.py file. .

```terminal
(webscrape) C:\Users\user.name\Documents\staticsite\content\code>python webscrape_multiple_course_pages.py

ENGR114 Engineering Programming
This is the course number: ENGR114
This is the course name: Engineering Programming
````

Let's modify this to find the course name and number of another engineering class. The url of ENGR221 Electrical Cirtuits I course is:
https://www.pcc.edu/schedule/default.cfm?fa=dspCourse2&thisTerm=201704&crsCode=ENGR221&subjCode=ENGR&crsNum=221&topicCode=GE&subtopicCode=ST1
We can add that to a list of url's at the top of our code. First Save as to create the file webscrape_multiple_course_pages.py. Then add the following to the top of the code:

```terminal
#Scrape multiple course information pages

import requests
import bs4

url1 = 'https://www.pcc.edu/schedule/default.cfm?fa=dspCourse2&thisTerm=201704&crsCode=ENGR114&subjCode=ENGR&crsNum=114&topicCode=GE&subtopicCode=ST1&frmtype=ADV&crnList=45437'
url2 = 'https://www.pcc.edu/schedule/default.cfm?fa=dspCourse2&thisTerm=201704&crsCode=ENGR211&subjCode=ENGR&crsNum=211&topicCode=GE&subtopicCode=ST1&crnList=40788,41369'
url3 = 'https://www.pcc.edu/schedule/default.cfm?fa=dspCourse2&thisTerm=201704&crsCode=ENGR221&subjCode=ENGR&crsNum=221&topicCode=GE&subtopicCode=ST1'
url_list = [url1, url2, url3]
```

Now we can integrate over the urls in ```url_list``` using a four loop to find the course name and number of the three courses. Note that you need the colon ```:``` as part of the code

```
for url in url_list:

```

Now we need to indent the lines within our for loop. Remember in python that simply means indenting them. You could also add 4 spaces to the begining of each line:
```
for url in url_list:
    r = requests.get(url)
    html = r.content
    soup = bs4.BeautifulSoup(html, 'html.parser')
    page_title = soup.h2.text
    print('\n' + page_title)
    course_number = page_title.split(' ',1)[0]
    course_name = page_title.split(' ',1)[1]

    print('course number: {}'.format(course_number))
    print('course name: {}'.format(course_name))
```
I added a new line with the ``` '\n' ``` character. Remember to use the reverse backslash, not the regualar backslash. Adding a new line will seperate out the courses into sections when it's printed to the command window. This just makes it easier for me to read. When I run the script, I get the following output:

```
(webscrape) C:\Users\user.name\Documents\staticsite\content\code>python webscrape_multiple_course_pages.py

ENGR114 Engineering Programming
course number: ENGR114
course name: Engineering Programming

ENGR211 Statics
course number: ENGR211
course name: Statics

ENGR221 Electrical Circuits I
course number: ENGR221
course name: Electrical Circuits I
```

So what's up next? Well, it is kind of a pain to cut and paste all of the individual course page url's from the web browser. Let's see if we can get these url's pragmatically instead...