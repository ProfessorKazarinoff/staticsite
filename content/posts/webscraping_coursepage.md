Title: Using Python and Beautiful Soup to read course information
Date: 2017-09-19 19:36
Modified: 2017-09-20 19:50
Status: Draft
Category: Python
Tags: python, beautiful soup, web crawling, 
Slug: python-beautifulsoup-course-info
Authors: Peter Kazarinoff
Series: Webscrape with Python and BeautifulSoup
series_index: 2
Summary:

The webpages for the college that show course information all follow a similar pattern. They show the course number: ENGR114, the course title: Engineering Programming, the CRN(Course Record Number, a unique number for each section): 24356. A technique called web scraping can be used to store all of this information in variables that we can save for later.

We can use Python and a web package called beautiful soup to parse the raw html and pull out the relevant course information. 

Let’s start by opening up the terminal and creating a new directory for our project. Then we ```cd`` into that directory. I sometimes forget to do move into the directory after I create it. If you forget where you are the command ```pwd`` will *print working directory*. Then set up a new virtual environment called ```webscrape```. We will do this at the terminal using virtualenv.

```terminal
$ mkvirtualenv webscrape -p python3
(webscrape)$
````

You can see that your virtual environment was created by running the ```lsvirtualenv``` command. We can also check which version of python the new virtual environment is running using ```python —version```.

```terminal
(webscrape)$ lsvirtualenv

webscrape
=========

(webscrape)$ python —version
Python 3.6.2
```

Now we need to install the packages to get this web scrapping work done. ```Beautiful Soup 4``` is the main package we will need, but we also need to install ```requests``` to grab the webpage.

```
(webscrape)$ pip install beautifulsoup4
(webscrape)$ pip install requests
```

We can ensure these packages are installed using the ```pip freeze``` command
```
(webscrape)$ pip freeze
beautifulsoup4==4.6.0
certifi==2017.7.27.1
chardet==3.0.4
idna==2.6
requests==2.18.4
urllib3==1.22
```

With those installed we can do a simple call on beautiful soup using the python interpreter on the thermal

```
(webscrape)$ python
>>> import requests
>>> import bs4
>>> r = requests.get("https://www.pcc.edu/schedule/default.cfm?fa=dspCourse2&thisTerm=201704&crsCode=ENGR114&subjCode=ENGR&crsNum=114&topicCode=GE&subtopicCode=ST1&frmtype=ADV&crnList=45437")
>>>raw_html = r.text
