Title: Thoughts on Software Design in Scientific Code
Date: 2021-02-19 08:11
Modified: 2021-02-19 08:11
Status: published
Category: Python
Tags: engineering, testing
Slug: thoughts-on-software-design-in-scientific-code
Authors: Peter D. Kazarinoff

[![fishing net]({static}/posts/testing_science_code/images/fishing-net.jpg)]({filename}/posts/testing_science_code/thoughts-on-software-design-in-science.md)

I listened to a few podcasts (TalkPython, Test and Code) that had a theme of:

 > **"How do we bring software design principles into science?"**

This got me thinking... There are a couple of ways software design could be incorporated into science and the code scientists write. The science I'm thinking about deals with the collection and analysis of data (that's almost all science right?). A few practices that could be incorporated into computer programs written by scientists that analyze science data are below. The ideas below are not meant to "fix" scientific computing or solve the problem of reproducibility in science. The thoughts below are just a couple of topics running through my head when I thought about: *How do we incorporate software design principles in science?*

## Version Control

![fishing net]({static}/posts/testing_science_code/images/notebooks.jpg)

Instead of naming files ```analysis-final.xlsx``` and ```analysis-final2.xlsx``` and ```analysis-final_v2_revisedpk.xlsx```, use a version control system like **git** and GitHub.com. If this practice is adopted, scientists can add meaningful commit messages with each code change. Version control could also be used as part of the peer-review paper writing process. One commit could be the paper manuscript before peer review and another commit could be the paper revisions after peer review. Other scientists could look at the commit history on GitHub to see how the paper changed based on the feedback the author received from reviewers.

## Code Review

![fishing net]({static}/posts/testing_science_code/images/map.jpg)

When an analysis is completed, scientists could review their code with a partner. Have someone else in the lab review the code, have someone else in the lab run the same code on their computer and give structured feedback about it. Scientists have practice reviewing paper drafts and experiment design. They could use that experience to help review an analysis that includes code.

## Section Code into Modules and Functions

![fishing net]({static}/posts/testing_science_code/images/package.jpg)

Some scientific code is written in one or two long scripts. Another software design principle scientists could adopt is **break code up into functions and modules** (different files). A long 2000 line script can be broken up into different functions and these functions can be pulled out into different modules, or put into different files. Two *rough* guidelines:

 * Each file should be able to fit on one screen
 * Each function should be 10 lines or less

These are not hard and fast rules, but something to aim for if a scientist doesn't know where to start.

The last software design principle we'll talk about in this post is testing.

![lab]({static}/posts/testing_science_code/images/lab.jpg)

## Testing

Testing is the last software design principle that could be brought into scientific code. Although data analysis and plotting don't particularly lend themselves to Test-driven Development (TDD). *How do you know what the result should be until you find the result?* The type of testing that does apply is **scientific code testing for reproducibility**. 

In this reproducibility testing mode, the things a scientist could test are:

 * Which Python version is running the code?
 * Which packages need to be installed?
 * What versions of those packages need to be installed?
 * Which character encoding is the code using (uft-8 anyone?)

## Conclusion

To wrap up. Some scientific code is difficult to test. But there are things scientists can do to make the code more portable and incorporate the ideas of software design into scientific code.

To help make a scientific script robust, consider trying the following:

 * Use version control, like git and GitHub
 * Participate in code review sessions with other researchers
 * Break long scripts into functions and separate files
 * Use testing to help ensure reproducibility

I'm planning on writing a follow up post that shows some of these ideas in a practical example.
