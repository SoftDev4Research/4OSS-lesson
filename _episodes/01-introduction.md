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

Scientific research nowadays relies heavily on the computational aspects provided by computer software, yet software is not always developed following practices that ensure its quality and sustainability. A publication that addresses this is the ([Four simple recommendations to encourage best practices in research software](https://f1000research.com/articles/6-876/v1)) which provides a simple, yet robust framework of simple recommendations that encourage the adoption of existing best practices in developing research software. These recommendations are designed around Open Science values, and provide practical suggestions that contribute to making research software and its source code more discoverable, reusable and transparent.

Based on these recommendations, this lesson focuses on providing both the underlying context as well as some practical exercises towards establishing their usefulness in the long term. The following episodes of this lesson are structured in the form of one episode per recommendation:

1. [Make source code publicly accessible from day one](../02-make-it-public/)
2. [Adopt a license and comply with the license of third-party dependencies](../03-use-license/)
3. [Define clear and transparent contribution, governance and communication processes](../04-contributions/)
4. [Make software easy to discover by providing software metadata via a popular community registry](../05-use-registry/)

## Open Science

"_When all researchers are aware of Open Science, and are trained, supported and guided at all career stages to practice Open Science, the potential is there to fundamentally change the way research is performed and disseminated. Fostering a scientific ecosystem in which research gains increased visibility, is shared more efficiently, and is performed with enhanced research integrity._" [Open Science Skills Working Group Report (2017)](https://ec.europa.eu/research/openscience/pdf/os_skills_wgreport_final.pdf#view=fit&pagemode=none)

Discussing best practices to develop research software is bound to touch on the subject of Open Science. Modern research relies on software, and building upon or reproducing that research requires access to the full source code behind that software ([ref](https://open-science-training-handbook.gitbook.io/book/examples-and-practical-guidance)). Sharing software used for research is one of the requirements for reproducibility. In addition to reproducibility, sharing software openly allows developers/scientists to receive career credit for their efforts, either through direct citation or via published software articles.

## FAIR principles

Though not all the recommendations from the FAIR data principles directly apply to software, there is good alignment between the discussed best practices and the FAIR data principles. The FAIR principles are a set of community-developed guidelines to ensure that data or any digital object are Findable, Accessible, Interoperable and Reproducible. The FAIR principles specifically emphasize enhancing the ability of machines to automatically find and use data or any digital object, and support its reuse by individuals. Standards for the description, interoperability, citation etc. are at the core of these principles ([ref](https://www.incf.org/activities/standards-and-best-practices/what-is-fair)).

The FAIR Guiding Principles, as described in [Scientific Data by Wilkinson et al](https://www.nature.com/articles/sdata201618):
- To be **Findable**
- To be **Accessible**
- To be **Interoperable**
- To be **Reusable**

## Why best practices in research software

There are many best practices currently in place that directly aim at and are tailored for software developers. These include aspects such as test-first programming and test coverage ([ref](https://github.com/r-lib/covr)), code quality ([ref](https://qaas.cyclopt.com/)), continuous integration ([ref](https://travis-ci.org)), etc. 

Most researchers who may need or want to develop software, do not have a software engineering background and are never taught the basic lab skills for research computing. This is why they might not know and therefore apply good programming practices (e.g. code modularisation, testing, annotation, etc.) [Wilson et al. 2017](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510). 
However, good practices in research software development are key to generating robust software and therefore reproducible research results. 

Often researchers do not know where to start. The 4OSS recommandations provide them with simple guidelines to incorporate good practices in software development and this lesson is aimed at teaching them how to smoothly adopt the 4OSS recommandations.

This lesson targets **scientists writing research software** but can also be of interest to a wider audience, particularly research funders, research institutions, journals, group leaders, and managers of projects producing research software. <br>

The adoption of these recommendations offers a simple mechanism for these stakeholders to promote the development of better software and an opportunity for developers to improve and showcase their software development skills.

## Starting with a couple of challenges

> ## Challenge 1: What are the challenges of making your project open?
> - Think about the challenges of making your project open
> - What do you need to do with your software in order to turn it into an open source project?
> - Discuss with a partner and make a list


> ## Challenge 2: Create a project on GitHub
> As we will see in the following, GitHub is a resource that can greatly facilitate the adoption of the 4OSS recommendations. It is not the only one of its kind and more resources will be described in these training materials in future development. 
> - You can find in the [Hello World guide](https://guides.github.com/activities/hello-world/) a description of what is GitHub and instructions on how to get started with GitHub. 
>  
> - Make sure that you have a GitHub account. If you need an account, please follow this [guide](https://services.github.com/on-demand/intro-to-github/create-github-account).
> - Following the [Hello World guide](https://guides.github.com/activities/hello-world/), create a new repository on GitHub.
> - To this aim, you have to choose a name for the new repository. This is more important than you might think and you can find [here](https://opensource.guide/starting-a-project/#naming-and-branding-your-project) some stuff to think about.
> - Make sure that you've ticked the "Initialize this project with a README" box
>
{: .challenge}

Congratulations, you've created your first repository! This is the first step towards making your source code publicly accessible from day one.
