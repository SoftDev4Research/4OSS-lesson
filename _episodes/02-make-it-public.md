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

When first creating a project, you will need to make a decision about what the project
will be called. This is also the appropriate time to consider other factors that
will have an impact on how people perceive and interact with your project. Bear in
mind that the health and longevity of an open source software project relies on
external contributions, so work to make yours welcoming and inclusive. For more
on this topic, and other advice on starting an open source project, check out the
[Open Source Guide on naming & branding](https://opensource.guide/starting-a-project/#naming-and-branding-your-project).

> ## Challenge: Create a project on GitHub
> - make sure that you have a GitHub account
> - click "+ -> new repository"
> - choose a name
>   - this is more important than you might think
>   - some stuff to think about: https://opensource.guide/starting-a-project/#naming-and-branding-your-project
>   - make sure that you've ticked the "Initialize this project with a README" box
>
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

- as well as the README & LICENSE `.md` files, a good software project might include guidance for contributing to the project (CONTRIBUTING.md - see lesson on contributions, governance, and communication), details of how to correctly cite the software after publication (CITATION.md - see later in this lesson), or even a `paper.md` file if the software is published via the Journal of Open Source Software (JOSS)
- you should have a good idea of what is the appropriate license for your project after the previous lesson (https://softdev4research.github.io/4OSS-lesson/04-use-license/index.html) but, if you need help choosing an license, you can also click on the "info" button next to the "add a license" dropdown, which will take you to https://choosealicense.com/
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

## Documentation

To make people using or contributing, a software needs to be documented.

> ## Discussion
>
> - What experiences have you had with good or bad documentation?
> - What was important for you **as a user**?
> - What was important for you **as a developer**?
>
{:.discussion}

The documentation of a software should be developed to target two types of audience: the end-users and the potential contributors (usually developers).

For end-user, a good documentation should clearly state what problems the software is designed to solve and who the target audience is. Installation instruction should be added clearly-stated list of dependencies. Ideally these should be handled with an automated package management solution. The documentation should also depict some examples of how to use the software (ideally to solve real-world analysis problems), explanation of the expected inputs and outputs.

The software API should be documented to a suitable level. In the best documentation, all functions/methods are documented including example inputs and outputs.

> ## Notes
>
> As an example, the [Journal of Open Source Software requirements](https://joss.readthedocs.io/en/latest/review_criteria.html#documentation) has defined that a software can be accepted for publication if it has at least in its documentation:
> - A statement of need: Do the authors clearly state what problems the software is designed to solve and who the target audience is?
> - Installation instructions: Is there a clearly-stated list of dependencies? Ideally these should be handled with an automated package management solution.
> - Example usage: Do the authors include examples of how to use the software (ideally to solve real-world analysis problems).
> - Functionality documentation: Is the core functionality of the software documented to a satisfactory level (e.g., API method documentation)?
>
{: .callout}


> ## Challenge
> Try to use the following software (link...)
>
> 1. What information was missing?
> 2. Talk to your neighbour and see if your lists agree.
>
> > ## Solution
> > - No input definition
> > -
> {:.solution}
{:.challenge}

One of the main challenge of documentation is to keep it up-to-date, following the evolution of the software. To avoid this issue, a good documentation follow these recommendations:
- The documentation is in the same place as your code, i.e. in the code repository (not on some webserver or a wiki page)
- The documentation is written in a lightweight markup (Markdown, reStructuredText) to simplify the contributions
- The API documentation is embedded inside the functions
- The maintainers of the software ask contributors to also contribute documentation when they contribute code (*connects to the community episode*)
- A Frequently Asked Question page is filled with every particular question about the code

The simplest documentation is the `README.md` file. For more visibility, a small website can be easily created to host the documentation, for example using the [GitHub pages](https://pages.github.com/) or [ReadTheDoc](https://readthedocs.org/).

> ## Challenge
>
> Create a simple page of documentation for your software using the [GitHub page](https://pages.github.com/)
>
> > ## Solution
> >
> > - Create a `docs` folder at the root of your repository
> > - Add an `index.md` file there
> > - Fill the `index.md` with minimum documentation mentioned before
> > - Commit and push it to GitHub
> > - Go to the repository on GitHub
> > - Click on `Setting` on the top
> > - Scroll to `GitHub Pages`
> > - Select `master branch /docs folder` as source
> > - Click on `Save`
> > - Copy the link that should now appear
> > - Check it
> > - Go back to the root repository on GitHub
> > - Click on the `Edit` button
> > - Paste the link to `Website`
> > - Click on `Save`
> >
> {:.solution}
>
{:.challenge}

More complex documentation can be also be generated using [Sphinx](http://www.sphinx-doc.org/en/master/). For example, the docstrings for each function could be extracted to populate an extensive API documentation. Even complex, this documentation can be stored on GitHub: it is only text.

Good documentation can make a big difference on how a software is used but also in creating a community around it to support it.

## making software (re)usable

As we discussed earlier, a piece of research software can be considered successful
if many people find it useful and cite it. As well as providing good documentation,
there are other steps that you should take to encourage people to use and contribute
to your research software.

> ## Challenge
>
> Think about a negative experience that you've had with a piece of software.
> What could have been done to improve your experience? Discuss this with the
> person next to you. Based on this discussion, can you make any recommendations
> to the rest of the group around how to encourage other people to use their
> research software?
>
{:.challenge}

- installation
- info on dependecies, requirements
    - files that provide detail on this
    - containerisation
    - mention mybinder.org
- interface
- good coding practices and following standards
    - helps with re-use, adaptation, contribution
    - link to SWC programming lessons & FAIR Data & Software Workshop material (https://events.tib.eu/fair-data-software/)
    - tests can help with installation, debugging, encourage better issue reporting

- good programming practice
  - SWC R & Python lessons
  - FAIR data & software lessons

## publishing

- GitHub guide to getting a DOI from Zenodo
- How to make your code citable using GitHub and Zenodo (https://github.com/OpenScienceMOOC/Module-5-Open-Research-Software-and-Open-Source/blob/master/content_development/Task_2.md)
- metadata recommendation (next lesson)
