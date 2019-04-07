Title: Django IoT Server - Part 12 Show one channel and one field
Date: 2019-04-07 09:21
Modified: 2019-04-07 09:21
Category: Django
Status: draft
Tags: python, IoT, django, server, sensor
Slug: django-iot-server-part12-one-channel-one-field
Authors: Peter D. Kazarinoff

In this post, we are going add a page to our server that shows the results of one channel and one field. The general format of the url will be:

 > https:myserver.com/channel/5/field/2

If we request this URL, the HTML we get back should be all of the data points that have ```channel=5``` and ```field=2``` associated with them.

[TOC]

## Expected Behavior

 > https:myserver.com/channel/5
 
This should give us all the data points from channel 5 (all field numbers associated with channel 5)

## Project URL's

## Channel app URL's

## HTML template

## View

## Testing

Now that the channel view works, we are going to extend this behavior, so that we can view an inidvidual channel and an individual field.

## Check Project URL's

## Channel app URL's

## HTML template

## View

## Testing

## Summary

This post, we reviewed how to output the results from just one channel and how to ouput the results of just one field in just one channel.

## Next Steps

In the next post, we will make our Django IoT server output just the most recient results from one channel and one field in json format.
