Title: Oregon Engineering College Transfer App - Part 1: Motivation
Date: 2020-08-23 12:40
Modified: 2020-08-23 12:40
Status: draft
Category: django
Tags: python, django, web app
Slug: oregon-engineering-college-transfer-app-part-1-motivation
Authors: Peter D. Kazarinoff
Series: Oregon Engineering College Transfer App
Series_index: 1

[![django pony]({static}/posts/transfer_app/images/django_pony.png)]({filename}/posts/transfer_app/part1_motivation.md)

This is the first part of a multi-part series on building a web app with Python and Django. The web app or website will act as a resource for Engineering students in Oregon Community Colleges that want to transfer to 4-year Universities. The transfer web app will show which classes from their community college engineering program will transfer for which classes in a 4-year University engineering program. In this first post, we'll review the motivation for the project and my initial idea of what the finished app will look like.

# The Oregon Engineering College Transfer Web App

What does that even mean? Students at community colleges in Oregon State, including Portland Community College, Mount Hood Community College, Linn Benton Community College, Lane Community College and Clackamas Community College can transfer to 4-year universities in Oregon State such as Portland State University, Oregon State University and Oregon Institute of Technology to finish their 4-year college engineering degress.

Although there is some standardization in college engineering course offerings in all the Oregon colleges, there are also a lot of differences. For example, ENGR is the course code used at Portland Community College, but ME is the course code used at Portland State for Mechanical Engineering courses.

Because of these differences in course numbering between colleges, it is useful for students to have an equivalency table that shows which of their community college courses counts for which of the 4-year university courses. Agreements between community colleges and universities about which courses transfer are called _articulation agreements_.

# Examples of Articulation Agreements

What is an _articulation agreement?_. An articulation agreement is an agreement between two educational institutions (such as an agreement between two colleges) about what courses at each school lead to the same learning outcomes and can be substitutes for each other. For example at Portland Community College, the Calculus I class is called MTH251. At Portland State, Calculus I is also called MTH251. These two classes lead to the same student learning outcomes and are "equivalent" classes. So when a student takes MTH251 at Portland Community College and transfer to Portland State, they get credit for Calculus 1, just like a student who took MTH251 at Portland State. PCC MTH251 = PSU MTH251.

A written agreement that formally states PCC's MTH251 counts for PSU's MTH251 is an articulation agreement. For a class to "officially transfer", an articulation agreement needs to be in place. 

# Why do we need a Transfer App?

Well, it seems sort of obvious that two classes both called Calculus I, but taught at colleges in Oregon and both with the course code of MTH251 should be "equivalent". But not all classes are so clear cut. For example, all three of the classes below are Circuits 1 and part of a Mechanical and Electrical Engineering degree, but each has a different course number depending on the college.

 * Portland Community College: ENGR 221 Electrical Circuits I
 * Oregon State University: ENGR 201
 * Portland State University: ECE 241

How would a student know that their ENGR221 class is equivalent to another college's ENGR201 class? That's kind of confusing. The web application we are going to build is going to show these course equivalencies for all of the engineering classes at Oregon Community Colleges and all of the engineering classes at Oregon public universities.

# Does this type of website already exhist?

Well sort of. First there are web pages hosted by each University and each community college that shows which courses transfer from or to their school. But students in Oregon really have to go to each University website to make shure. Some of these web pages are hard to find, and if you take a class at a smaller community college, you might not see your courses listed. 

There is a similar website for California Community Colleges and California State 4-year colleges which has the same functionality that we are going to build. A link and image for California's assist.org site is below.

[https://assist.org/](https://assist.org/)

[![assist website]({static}/posts/transfer_app/images/assist_dot_org.png)](https://assist.org/)

# What's Next?

So now we know what we are building: A website that shows which community college engineering classes transfer for which university classes in Oregon. In the next post, we are going to set up our development environment and start coding. Our development environment is the tools we are going to use to build the website.
