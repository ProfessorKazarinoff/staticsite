Title: Thoughts on How to Test Science Code
Date: 2021-02-17 08:11
Modified: 2021-02-17 08:11
Status: draft
Category: Python
Tags: engineering,testing
Slug: thouhts-on-how-to-test-science-code
Authors: Peter D. Kazarinoff

![fishing net]({static}/posts/testing_science_code/images/fishing-net.jpg)

I have been at a couple meetups (at PyData PDX) and heard a few podcasts (TalkPython) that had a theme of:

 > **"How do we bring software design princpals into science?"**

This got me thinking... There are a couple ways software design could be incorporated into science. The science I'm thinking about deals with the collection and analysis of data (that's almost all science right?). A few practices that could be incorporated into computer programs that analyze science data are below. The ideas below are not ment to "fix" scientific computing or solve the problem of reproducability in science. The thoughts below are just a couple topics running through my head when I thought about *How do we bring software design principals into science?*

## Version Control

![fishing net]({static}/posts/testing_science_code/images/notebooks.jpg)

Instead of ```myscript-final.xlsx``` and ```myscript-final2.xlsx``` and ```myscript-final_v2_revisedpk.xlsx```, use a version control system like **git** and Github.com. If this practice is adopted, scientists can add meaningful commit messages with each code change. Version control could also be used as part of the peer-review paper writing process. One commit could be the paper manuscript before peer review and another commit could be the paper revisions after peer review. Other scientists could look at the commit history on GitHub to see how the paper changed based on the feedback the author recieved from reviewers.

## Code Review

![fishing net]({static}/posts/testing_science_code/images/map.jpg)

When an analysis is completed, scientists could review their code with a partner. Have someone else in the lab review the code, have some one else run the same code on their computer and give structured feed-back to the author about it. Scientists have practice reviewing paper drafts. Scientists could use that experience to help review an analysis that includes code.


## Section Code into Modules and Functions

![fishing net]({static}/posts/testing_science_code/images/package.jpg)

Some scientific code is written in one or two long scripts. Another software design principal scientists could adopt is **break code up into functions and modules** (different files). A long 2000 line script can be broken up into different functions and these functions can be pulled out into different modules, or put into different files. Two rough guidlines:

 * Each file should be able to fit on one screen
 * Each function should be 10 lines or less

These are not hard and fast rules, but something to aim for if a scientists doesn't know where to start.

The last software design principal we'll talk about in this blog post is testing.

## Conclusion

To wrap up. Some scientific code is difficult to test. But there are things we can do to make the code more portable and incorporate the ideas of software design into scientific code.

To help make a scientific script testable, consider trying the following:

 * break a long script into functions and seperate files
 * include one main fuction
 * assign functions inputs and outputs. If no output makes sense, return ```True```
 * functions which produce plots should output ```fig``` and ```ax``` objects.
