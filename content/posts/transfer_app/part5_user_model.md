Title: Oregon Engineering College Transfer App - Part 5: User Model
Date: 2018-10-17 12:40
Modified: 2018-10-17 12:40
Status: draft
Category: django
Tags: python, django, web app
Slug: oregon-engineering-college-transfer-app-part-5-user-model
Authors: Peter D. Kazarinoff
Series: Oregon Engineering College Transfer App
Series_index: 5
Summary: This is the fifth part of a multi-part series on building a web app with Python and Django. The web app will act as a resource for Engineering students at Oregon Community Colleges that want to transfer to 4-year Universities. The transfer web app will show which classes from their community college engineering program will transfer to which classes in a 4-year University engineering program. In this fifth post, we'll build a user model that will allow us to add new users, allow users to login, and allow users to logout.

Summary: This is the fifth part of a multi-part series on building a web app with Python and Django. The web app will act as a resource for Engineering students at Oregon Community Colleges that want to transfer to 4-year Universities. The transfer web app will show which classes from their community college engineering program will transfer to which classes in a 4-year University engineering program. In this fifth post, we'll build a user model that will allow us to add new users, allow users to login, and allow users to logout.

[TOC]

## What is a user model?

The Oregon Transfer App has two purposes. The first purpose is to be a place that community college students can go to see which classes at a community college transfer to a specific 4-year university in Oregon. The second purpose is to be a place where administrators at 4-year universities can go and post transfer class equivalencies. The 4-year college administrators set which classes transfer and the students see which classes transfer. We need to build a user model so that the 4-year university administrators can login, then build and modify transfer equavalencies that students can see. Students (or any other user) will not have to login to see which classes transfer. Students (or any other regular user) will not have the ability to set which classes transfer, just see which classes transfer. So a user model for the 4-year University administrators is needed.

## What do users need to be able to do?

The 4-year University administrators need to be able to do a couple things:

### Transfer App site privileges

 * log into the Transfer App site
 * Create a new 4-year University
 * Create classes at that 4-year University
 * Create and edit classes 2-year community college
 * Create and edit classes at 2-year community college

### Transfer App user actions

 * Create a new user, set username and password
 * Log in
 * Log out
 * Reset password
 * Retrieve forgetten password
 * ?Maybe set and update a profile?

We'll build some of these Transfer App user actions in this post.

## Create the users app

## Create a user model

## Create users with the django admin

## Make sign-up page

## Make login page

## Make logout page

## Test user functionality

## Summary

## Future Work

Next, we'll provide a way for users to change their passwords. We will also build a way for users to get an email if they forget thier password.