Title: Django IoT Server - Part 14 Plot the data from one channel
Date: 2019-04-07 09:21
Modified: 2019-04-07 09:21
Category: Django
Status: draft
Tags: python, IoT, django, server, sensor
Slug: django-iot-server-part14-plot-data-from-one-channel
Authors: Peter D. Kazarinoff

In this post, we are going to modify the page on our Django IoT server that shows the data points from one server and one channel. In addiiton to a table which contains the data points we are going to add a plot which shows the most 10 recent data points. We will build the plot with a javascript framework called HighCharts.

 

[TOC]

## Expected Behavior

 > https:myserver.com/channel/5/field/2
 
This should show us a plot of the channel data

## Highcharts javacscrit framework

## modify HTML template

## View

## Testing

Now that the channel view works, we are going to extend this behavior, so that we can view an inidvidual channel and an individual field.

## Summary

This post, we reviewed how to output the results of just one field in just one channel and plot the data one a chart.

## Next Steps

In the next post, we will make our Django IoT server output just the most recient results from one channel and one field in json format.
