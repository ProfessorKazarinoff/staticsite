Title: Using Altair to make stress-strain curves
Slug: altair-stress-strain-curves
Date: 2017-12-17 10:30
Status: Draft
Category: Python
Tags: python, jupyter, notebook, altair
JavaScripts: ipynb_mathjax_inline.js
BokehCSS: https://cdn.pydata.org/bokeh/dev/bokeh-0.12.5dev16.min.css
BokehJS: https://cdn.pydata.org/bokeh/dev/bokeh-0.12.5dev16.min.js
Author: Peter D. Kazarinoff
Summary: Below is a .md post with the drop in jupyter notebook that contains an altair plot.

## Code pulled from a jupyter notebook using liquid tags

{% if article.bokehcss and article.bokehjs %}
    <link rel='stylesheet' href='{{ article.bokehcss }}'>
    <script src="{{ article.bokehjs }}"></script>
{% endif %}

{% notebook ../code/altair/altair_test.ipynb %}