Title: Building an IoT Server with flask and Python - Part 5 Adding a Database
Date: 2018-09-10 09:01
Modified: 2018-09-10 09:01
Status: draft
Category: flask
Tags: python, flask, thingspeak, mobile, IoT, sensor
Slug: flask-iot-server-database
Authors: Peter D. Kazarinoff

This is the fifth part of a series of posts about building an Internet of Things (IoT) server with **flask**, Python and ESP8266 microcontrollers. In this post we'll add a sqlite3 database to our **flask** IoT server to store all the temperature data points that come in from our ESP8266-based WiFi weather stations. We will also build out the main page of the **flask** IoT server site to display the most recent data points pull from the database.

[TOC]

## Introduction

In the last post, we built in some validation to our web API so that only certain API keys and mac addresses are allowed. We also used Python's **datetime** module to add a time stamp to each data point as it comes in. 

This is great, but it would be really nice to _save_ every datapoint that comes in. Right now, when a new data point comes into our server, the previous data point is erased.  

There are a couple of ways we could store the temperature data that comes in from our ESP8266-baed WiFi weather stations:

 * Save the data in a text file. Append new a line to the text file for each new data point.
 * Save the data in a .csv file. Add a new line for each data point, seperate fields on one line with a comma or tab.
 * Save the data in a pandas dataframe. Store the data points as rows in the dataframe. 
 * Use a database to store the data points. Each data point saved as a record in the database. 
 
 Of the four options above, I decided to use a sqlite3 database to store the data coming in from the **flask** IoT server web API.

## Why an sqlite3 database?

Why use an sqlite3 database? One of the key reasons is that the **sqlite3** module is part of the Python Standard Library. We don't have to install any external packages to use **sqlite3**. A sqlite3 database is also light-weight and won't take up a lot of space on our server. But the real reason I choose to use **sqlite3** is that the library has good documentation and I can build off the sqlite3 examples of others. 

## Database design
 
Before adding any data to the database, we need to think a little bit about database design. 

Our sqlite3 database is going to be a a pretty simple database. I sort of think of the database itself as a Microsoft Excel workbook, a whole Microsoft Excel **_.xlsx_** file. We will only employ one _table_ in our sqlite3 database. I think a database table is kind of like a sheet or tab in Microsoft Excel file. Each data point from the WiFi weather stations will represent one _record_ in the database. I kind of think of a record as one row in a Microsoft Excel file. 

The web API we built brings in a couple of identifiers for each datapoint. Based on an a valid URL such as:

> https://mydomain.com/update/API_key=PHDNGI2345/mac=6c:rf:7f:2b:0e:g8/field=1/data=72.3
 
In the URL above we've provided:

 * ```update``` (to tell the IoT server to save the data point, not just serve a webpage)
 * ```API_key = PHDNGI2345``` (to identify the user)
 * ```mac = 6c:rf:7f:2b:0e:g8``` (to identify the ESP8266-based WiFi weather station)
 * ```field = 1``` (to specify this is a temperature data point, not a humidity data point)
 * ```data = 72.3``` (to specify the temperature is 72.3 degrees)

 Our database needs to be able to save these four fields:

 * ```API_key```
 * ```mac```
 * ```field```
 * ```data```

As well as these two additional fields:

 * ```date``` and ```time```
 * some sort of primary key that uniquley identifies each record

Two example records on our database might look like:

| primary_key | API_key | mac | field | data | data_time |
| --- | --- | --- | --- | --- | --- |
| 1 | PHDNGI2345 | 6c:rf:7f:2b:0e:g8 | 1 | 72.3 | 2018-09-10 08:23:45 PM |
| 2 | PHDNGI2345 | 6c:rf:7f:2b:0e:g8 | 1 | 83.2 | 2018-09-11 09:45:01 AM |

## Prototype the sqlite3 database

I didn't have a lot of experience building or using databases before this **flask** IoT server project. Before I started coding, I tried out a couple of **sqlite3** commands in a jupyter notebook.

{% notebook ../code/flask/sqlite_play.ipynb %}

## Add the sqlite database to the server

OK- after playing around with **sqlite3**, we can now add some code to our flask IoT server web API. Let's code in a database connection, cursor object creation and record execution. This code belongs in the ```/update/...``` route.

```python
@app.route("/update/API_key=<api_key>/mac=<mac>/field=<int:field>/data=<data>", methods=['GET'])
def write_data_point(api_key, mac, field, data):
    if (api_key == API_KEY and mac == MAC_ADDRESS):
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        t = datetime.datetime.now(tz=pytz.utc)
        date_time_str = t.isoformat()
        c.execute("INSERT INTO data VALUES(:Id, :API_key, :date_time, :mac, :field, :data)",
              {'Id': None,
              'API_key': api_key,
              'date_time': date_time_str,
              'mac': mac,
              'field': int(field),
              'data': round(float(data), 4)})
        conn.commit()
        c.close()
        conn.close()

        return render_template("showrecent.html", data=data, time_stamp=date_time_str)

    else:
        return render_template("403.html")
```

At the top of this main script, we'll also include a couple of lines to create the database when the **flask** app starts:

```python
if not os.path.isfile('data.db'):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE data (
        Id INTEGER PRIMARY KEY AUTOINCREMENT, 
        API_key text,
        date_time text,
        mac text,
        field integer,
        data real
        )""")
    conn.commit()
    conn.close()
```

## Update the main webpage with the newest database entry

Next, we'll update the main page of the **flask** IoT server, the home or ```/``` route.

```python
@app.route("/")
def index():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT data, date_time, MAX(rowid) FROM data WHERE field=?", ('1',))
    row1 = c.fetchone()
    c.execute("SELECT data, date_time, MAX(rowid) FROM data WHERE field=?", ('2',))
    row2 = c.fetchone()
    c.close()
    conn.close()
    data1 = str(round((float(row1[0]) * 1.8) + 32))
    data2 = str(round((float(row2[0]) * 1.8) + 32))
    time_str1 = row1[1]
    t1 = dateutil.parser.parse(time_str1)
    t_pst1 = t1.astimezone(pytz.timezone('US/Pacific'))
    time_stamp1 = t_pst1.strftime('%I:%M:%S %p   %b %d, %Y')
    time_str2 = row2[1]
    t2 = dateutil.parser.parse(time_str2)
    t_pst2 = t2.astimezone(pytz.timezone('US/Pacific'))
    time_stamp2 = t_pst2.strftime('%I:%M:%S %p   %b %d, %Y')
    return render_template("showdoubletemp.html", data1=data1, time_stamp1=time_stamp1, data2=data2,time_stamp2=time_stamp2)

```

## Restart the server

Restart the **flask** IoT server with the following command:

```bash
$ sudo systemctl stop flaskapp
$ sudo systemctl start flaskapp
$ sudo systemctl status flaskapp
# ctrl-c to exit
```

## Summary 

It works! We have a working sqlite3 database. Each time the web API is hit with a web browser, the data point is saved as a record in the database. Each time we go to the main page of the **flask** IoT server site, we see the most recent temperature posted.

## Next steps 
 In the next post, we'll upload new **_.py_** files to our ESP8266-based WiFi weather stations. This will give the WiFi weather stations the ability to post temperature data to our **flask** IoT server web API.