# coding: utf-8

# In[98]:


# import packages
import pandas as pd
import requests
import bs4
import sys

print('Python version ' + sys.version)
print('Pandas version: ' + pd.__version__)
print('Requests version: ' + requests.__version__)
print('Beautiful Soup version: ' + bs4.__version__)


# In[99]:
def get_course_info(url):

#Scrape a course information page
# ENGR114 #url ='https://www.pcc.edu/schedule/default.cfm?fa=dspCourse2&thisTerm=201801&crsCode=ENGR&subjCode=ENGR&crsNum=114&topicCode=GE&subtopicCode=%20' 
# ENGR101 #url ='https://www.pcc.edu/schedule/default.cfm?fa=dspCourse2&thisTerm=201801&crsCode=ENGR&subjCode=ENGR&crsNum=101&topicCode=GE&subtopicCode=%20'
# ENGR211 #url ='https://www.pcc.edu/schedule/default.cfm?fa=dspCourse2&thisTerm=201801&crsCode=ENGR&subjCode=ENGR&crsNum=211&topicCode=GE&subtopicCode=%20'
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
	pre_reqs = page_text.split(' Prerequisites: ',1)[1]
	pre_reqs = pre_reqs.split('. Audit available.',1)[0]

	print('This is the course number: {}'.format(course_number))
	print('This is the course name: {}'.format(course_name))
	print('This is the course description: {}'.format(page_text))
	print('These are the course pre reqs: {}'.format(pre_reqs))
	print('This is the course CRN #: {}'.format(CRN))
	print('This is the course credits: {}'.format(course_credits))


# In[100]:


	table_object = soup.table


# In[101]:


	table_object


# In[102]:


	table_header_object = table_object.thead
	table_header_object


# In[103]:


	column_header_list = []
	for header in table_header_object.find_all('th'):
		column_header_list.append(header.text)
	print(column_header_list)


# In[104]:


	for data in table_object.find_all('tr', attrs={'class':'data-row'}):
		print(data)


# In[105]:


	for data_row in table_object.find_all('tr', attrs={'class':'data-row'}):
		print('!!!!!!!!!!!!!!!! New Data Row  !!!!!!!!!!!!!!!!!!!!!')
		for data in data_row.find_all('td'):
			print(data.text.lstrip().rstrip())
	print('DONE')    


# In[109]:


	df = pd.DataFrame(columns=['CRN','course number','course name','instructor','Campus / Bldg / Rm','Time','Days','Dates','Materials','More info'])
	df


# In[110]:


	for row,data_row in enumerate(table_object.find_all('tr', attrs={'class':'data-row'})):
		print('!!!!!!!!!!!!!!!! New Data Row  !!!!!!!!!!!!!!!!!!!!!')
		df.set_value(row,'course number',course_number)
		df.set_value(row,'course name',course_name)
		for i,data in enumerate(data_row.find_all('td')):
			df.set_value(row, column_header_list[i], data.text.lstrip().rstrip())
			print(data.text.lstrip().rstrip())
	print('DONE')
	df


# In[111]:


	for row,instructor in enumerate(table_object.find_all('tr', attrs={'class':'info-row'})):
		instructor_field = instructor.find_all('td')[1].text.lstrip().rstrip()
		instructor_name_long = instructor_field.split("Instructor: ",1)[1]
		instructor_name = instructor_name_long.split('\n',1)[0]
		df.set_value(row,'instructor',instructor_name)
	df

	return df

if __name__ == "__main__":
	# import packages
	import pandas as pd
	import requests
	import bs4
	import sys
	url = 'https://www.pcc.edu/schedule/default.cfm?fa=dspCourse2&thisTerm=201801&crsCode=MTH65&subjCode=MTH&crsNum=65&topicCode=MTH&subtopicCode=MATH'
	output = get_course_info(url)
	print(output)