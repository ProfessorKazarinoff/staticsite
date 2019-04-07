Title: Django IoT Server - Part 13 Show the most recent data point
Date: 2019-04-07 09:21
Modified: 2019-04-07 09:21
Category: Django
Status: draft
Tags: python, IoT, django, server, sensor
Slug: django-iot-server-part13-most-recent-data-point
Authors: Peter D. Kazarinoff

In this post, we are going add a page to our Django IoT server that shows the most recent data point. 

 > https:myserver.com/channel/5/field/2/latest

 > https:myserver.com/api/channel/5/field/2/latest

If we request this URL, the HTML we get back just the most recent data point that has ```channel=5``` and ```field=2``` associated with them.

[TOC]

## Expected Behavior

 >  > https:myserver.com/channel/5/field/2/latest
 
This should give us the most recent data point from channel 5, field 2

## Project URL's

## Channel app URL's

## HTML template

## View

## Testing

Now that the channel view works, we are going to extend this behavior, so that we can view an inidvidual channel and an individual field.

## Expected Behavior

 >  > https:myserver.com/api/channel/5/field/2/latest
 
This should give us the most recent data point from channel 5, field 2 in json format


## Check Project URL's

## Channel app URL's

## HTML template

## View

## Testing

## Summary

This post, we reviewed how to output the results from just one channel and how to ouput the results of just one field in just one channel.

## Next Steps

In the next post, we will make our Django IoT server output just the most recient results from one channel and one field in json format.
