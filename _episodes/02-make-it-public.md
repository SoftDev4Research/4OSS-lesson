---
title: "Make source code publicly accessible from day one"
teaching: 0
exercises: 0
questions:
- "What are the benefits of making my software project public from the beginning?"
- "How do I make my project publicly accessible?"
- "What resources are available to help me document my software?"
- "What are the best practices in open software development?"
- "How do I publish my open source software?"
objectives:
- "create a new software project on GitHub"
- "list three things that should be included in 'bare minimum' software documentation"
- "explain the difference between user- and developer-oriented documentation"
- "describe three steps that can be taken to increase the (re)usability of software"
- "describe how external resources can be used at the stage of publishing OS software"
keypoints:
- "Services like GitHub can be used to make your project public and findable."
- "Using these tools appropriately encourages and credits contributions to the project."
- "Making your project public encourages better practices in developing and documenting software."
- "GitHub makes it easier to get a DOI and publish your software."
---

## Creating a project on GitHub

Perhaps the most important aspect of good research software is that it is accessible.
Even the fastest, most accurate, beautifully-written software can't fulfill its
potential if no-one but the developer knows that it exists. Luckily, the internet
and search engines have made it easier than ever before to find and compare software
and projects that could be used to research.

Software that is easy to find, clearly documented, and under regular,
visible development, is attractive to researchers who are keen not to waste time
on tools and resources that are difficult to use and/or error-prone. A software
project whose most recent version is available alongside a whole history of
the changes and contributions that have been made to that software, is
- more easily findable
- perceived as more trustworthy
- encouraging contributions and validation from the wider community
- able to give appropriate credit for contributions made in the past

Several publicly-accessible platforms exist online for hosting software projects.
GitHub is one of the most popular and comprehenive of these platforms, facilitating
licensing, documentation, and publication of code as well as providing a remote
version control repository.

> ## Challenge: Create a project on GitHub
> - make sure that you have a GitHub account
> - click "+ -> new repository"
> - choose a name
>   - this is more important than you might think
>   - some stuff to think about: https://opensource.guide/starting-a-project/#naming-and-branding-your-project
>   - make sure that you've ticked the "Initialize this project with a README" box
>   - you can add a license now as well
>   - you should have a good idea of what is the appropriate license for your project after the previous lesson (https://softdev4research.github.io/4OSS-lesson/04-use-license/index.html) but, if you need help choosing an license, you can also click on the "info" button next to the "add a license" dropdown, which will take you to https://choosealicense.com/.
{: .challenge}

- congratulations! you've created your first repository :)
- look at the README.md file
    - automatically displayed on the front page of your repository
    - project name and subheading emphasised by default, using Markdown syntax
    - _italics_, __bold__, [link](https://f1000research.com/articles/6-876/v1), list
- read more about Markdown here: https://guides.github.com/features/mastering-markdown/

> ## Challenge: Improve the README
>
> The README.md file that GitHub generated when we created the project is quite
> boring. Add some more content using some of the Markdown syntax introduced
> above. You could add a few sentences about the purpose of your software, some
> details of the author(s) and their affiliation(s), or anything else that you
> think is important.
{: .challenge}

- as well as the README & LICENSE `.md` files, a good software project should include guidance for contributing to the project (CONTRIBUTING.md - see lesson on contributions, governance, and communication), details of how to correctly cite the software after publication (CITATION.md - see later in this lesson), or even a `paper.md` file if the software is published via the Journal of Open Source Software (JOSS)
- making the project public at the start is not enough! See the [Software Carpentry lesson on Version Control with Git](http://swcarpentry.github.io/git-novice/) for advice on best practice in software version control.

> ## Discussion: How does version control help your project?
> #### 5 minutes
> You may already be aware of the benefits of software version control in relation to a programming project. In small groups, discuss how following best practices in version control, such as making regular, small, self-contained commits, and having project members work on branches to avoid conflicts, can benefit a project hosted publicly on GitHub.
> > ## Solution
> > As well as making it easier to collaborate and to track and revert changes in the code, following best practices in version control:
> > - keeps progress on your project visible
> > - encourages contributions and suggestions from the community
> > - facilitates recognition of contributions at time of publication
> > - promotes good programming practice amongst project members
> {: .solution}
{: .discussion}

- git SWC lesson
- OS naming & branding guide (https://opensource.guide/starting-a-project/#naming-and-branding-your-project)
- [Markdown guide](https://guides.github.com/features/mastering-markdown/)
- License recommendation episode
- contributing recommendation episode
- How to set up a repository on GitHub

## Documentation

- GitHub guide to GitHub Pages
- ReadTheDocs guide

## making software (re)usable

- good programming practice
  - SWC R & Python lessons
  - FAIR data & software lessons

## publishing

- GitHub guide to getting a DOI from Zenodo
- How to make your code citable using GitHub and Zenodo (https://github.com/OpenScienceMOOC/Module-5-Open-Research-Software-and-Open-Source/blob/master/content_development/Task_2.md)
- metadata recommendation (next lesson)
