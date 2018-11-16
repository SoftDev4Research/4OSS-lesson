---
title: "Introduction"
teaching: 10
exercises: 0
questions:
- "Why are best practices necessary in research software?"
- "How Open Source can help with better quality of software?"
objectives:
- "Basics of Open Science in research software"
- "Introduction to the FAIR principles"
keypoints:
- "Best practices in research software are tied to the FAIR principles"
- "The discussed best practices are not tailored to software developers, but rather to a wider audience"
---

In recent years, scientific research has become more data driven and data intensive and it is no longer possible to carry out the analysis without the use of computers and research software. Unfortunately, software is not always developed following best practices that ensure its quality and sustainability.[Four simple recommendations to encourage best practices in open research software](https://f1000research.com/articles/6-876/v1)) is a publication that addresses this issue by providing a simple, yet robust framework of recommendations that encourage the adoption of existing best practices in research software development. These recommendations are designed around Open Science values, and provide practical suggestions that contribute to making research software and its source code more discoverable, reusable and transparent.

These recommendations recognise that not everyone can or want to make their software open from day one, but we encourage you to learn from the recommendations and adapt them to your needs. For example, you can have a private repository, you can and should still have a license, make contributions clear, and have a registry of your software. 

This lesson explains the concepts behind four recommendations and teaching practical skills necessary for their implementation. The lesson is divided into four episodes, each focusing on one recommendation.

1. [Make source code publicly accessible from day one](../02-make-it-public/)
2. [Adopt a license and comply with the license of third-party dependencies](../03-use-license/)
3. [Define clear and transparent contribution, governance and communication processes](../04-contributions/)
4. [Make software easy to discover by providing software metadata via a popular community registry](../05-use-registry/)

## Open Science

"_When all researchers are aware of Open Science, and are trained, supported and guided at all career stages to practice Open Science, the potential is there to fundamentally change the way research is performed and disseminated. Fostering a scientific ecosystem in which research gains increased visibility, is shared more efficiently, and is performed with enhanced research integrity._" [Open Science Skills Working Group Report (2017)](https://ec.europa.eu/research/openscience/pdf/os_skills_wgreport_final.pdf#view=fit&pagemode=none)

Discussing best practices to develop research software is bound to touch on the subject of Open Science. Modern research relies on software, and building upon or reproducing that research requires access to the full source code behind that software ([ref](https://open-science-training-handbook.gitbook.io/book/examples-and-practical-guidance)). Sharing software used for research is one of the requirements for reproducibility. In addition to reproducibility, sharing software openly allows developers/scientists to receive career credit for their efforts, either through direct citation or via published software articles.

## FAIR principles

Though not all the recommendations from the FAIR data principles directly apply to software, there is good alignment between the practices discussed here and the FAIR data principles. The FAIR principles are a set of community-developed guidelines to ensure that data or any digital object are Findable, Accessible, Interoperable and Reusable. The FAIR principles specifically emphasize enhancing the ability of machines to automatically find and use data or any digital object, and support its reuse by individuals. Standards for the description, interoperability, citation etc. are at the core of these principles ([ref](https://www.incf.org/activities/standards-and-best-practices/what-is-fair)).

The FAIR Guiding Principles, as described in [Scientific Data by Wilkinson et al](https://www.nature.com/articles/sdata201618):
- To be **Findable**
- To be **Accessible**
- To be **Interoperable**
- To be **Reusable**

## Why best practices in research software

There are many best practices currently in place that directly aim at and are tailored for software developers. These include aspects such as test driven development and test coverage ([ref](https://github.com/r-lib/covr)), code quality ([ref](https://qaas.cyclopt.com/)), continuous integration ([ref](https://travis-ci.org)), etc. 

Most researchers who may need or want to develop software, do not have a formal software engineering training. This is why they might not be aware of good programming practices (e.g. code modularisation, testing, annotation, etc.) [Wilson et al. 2017](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510). 
However, good practices in research software development are key to generating good quality software and therefore reproducible research results. 

The 4OSS recommandations provide simple guidelines to incorporate good practices in reserch software development and this lesson teaches how to adopt the 4OSS recommandations.

This lesson targets **scientists writing research software** but can also be of interest to a wider audience, particularly research funders, research institutions, journal editors, group leaders, and managers of projects producing research software. <br>

The adoption of these recommendations offers a simple mechanism for these stakeholders to promote the development of better software and an opportunity for developers to improve and showcase their software development skills.

## Starting with a couple of challenges

> ## Challenge 1: What are the challenges of making your project open?
> - Think about the challenges of making your project open.
> - What do you need to do with your software in order to turn it into an open source project?
> - Discuss with a partner and make a list


> ## Challenge 2: Create a project on GitHub
> GitHub is a source code hosting service that facilitates collaborative software development.
> - [Hello World guide](https://guides.github.com/activities/hello-world/) describes  what is GitHub and contains instructions on how to get started with GitHub. 
>  
> - You will need to created the GitHub account if you don't have one already. If you need an account, please follow [this guide](https://services.github.com/on-demand/intro-to-github/create-github-account).
> - Follow the [Hello World guide](https://guides.github.com/activities/hello-world/) to create a new repository on GitHub.
> - You will need to choose a name for your new repository. This is more important than you might think and you can read more on this topic in [Naming and Branding Your Project](https://opensource.guide/starting-a-project/#naming-and-branding-your-project) guide.
> - Make sure that you've ticked the "Initialize this project with a README" box
>
{: .challenge}

Congratulations, you've created your first repository! This is the first step towards making your source code publicly accessible from day one.
