Title: How to Deploy a Streamlit App with Microsoft Azure
Date: 2019-12-29 08:11
Modified: 2019-12-29 08:11
Status: draft
Category: Python
Tags: streamlit, bokeh, engineering
Slug: streamlit-app-azure
Authors: Peter D. Kazarinoff

![streamlit bokeh heroku]({static}/posts/streamlit/images/file.png)

[**Streamlit**](https://streamlit.io/docs/) is a web app-building framework for Python. Streamlit is a way to create mostly simple single-page web apps that are easy to deploy. Streamlit is useful for engineers and data scientists who have some app functionality, like a plot that dynamically changes based on user interaction, but don't want to build out a full website using a web framework like Django or Flask. 

In this post, we will create a Streamlit app that displays a Bokeh plot and deploy it online with Azure

That's it! The Streamlit app should now be running on Azure.

### View the Streamlit App live on the web

Check the URL provided by Azure dashboard. The app works the same as when we ran it locally, but now it's live on the internet. Anyone with the URL can view our Streamlit app.

![app on Heroku]({static}/posts/streamlit/images/file.png)

The Streamlit app opens on a phone too. 

![app on Phone]({static}/posts/streamlit/images/file.png)

## Summary

In this post, we created a web app with Streamlit and deployed it on Microsoft's Azure cloud service
