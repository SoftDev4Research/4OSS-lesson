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
- "They are not tailored to software developers, but rather to a wider audience"
---

Scientific research relies on computer software, yet software is not always developed following practices that ensure its quality and sustainability. One of the most recent publications ([Four simple recommendations to encourage best practices in research software](https://f1000research.com/articles/6-876/v1)) provided a simple, yet robust framework of simple recommendations that encourage the adoption of existing best practices in developing research software. These recommendations are designed around Open Science values, and provide practical suggestions that contribute to making research software and its source code more discoverable, reusable and transparent.

Based on these recommendations, this lesson focuses on providing both the underlying context as well as some practical exercises towards establishing their usefulness in the long term. The consequent episodes of this lesson are structured in the form of one episode per recommendation;
1. Make source code publicly accessible from day one
2. Make software easy to discover by providing software metadata via a popular community registry
3. Adopt a license and comply with the license of third-party dependencies
4. Define clear and transparent contribution, governance and communication processes

## Open Science

"_When all researchers are aware of Open Science, and are trained, supported and guided at all career stages to practice Open Science, the potential is there to fundamentally change the way research is performed and disseminated, fostering a scientific ecosystem in which research gains increased visibility, is shared more efficiently, and is performed with enhanced research integrity._" [Open Science Skills Working Group Report (2017)](https://ec.europa.eu/research/openscience/pdf/os_skills_wgreport_final.pdf#view=fit&pagemode=none)

Discussing best practices in developing research software, one is bound to touch on the subject of Open Science. Modern research relies on software, and building upon—or reproducing—that research requires access to the full source code behind that software ([ref](https://open-science-training-handbook.gitbook.io)). Sharing software used for research (whether computational in nature, or that relies on any software-based analysis/interpretation) is a necessary, though not sufficient, condition for reproducibility. In addition to reproducibility, sharing software openly allows developers to receive career credit for their efforts, either through direct citation or via published software articles. We are going to be discussing all these aspects in the following lesson.

## FAIR principles

The FAIR principles are a set of community-developed guidelines to ensure that data or any digital object are Findable, Accessible, Interoperable and Reproducible. The FAIR principles specifically emphasize enhancing the ability of machines to automatically find and use data or any digital object, and support its reuse by individuals. Standards for the description, interoperability, citation etc. are at the core of these principles ([ref](https://www.incf.org/activities/standards-and-best-practices/what-is-fair)).

The FAIR Guiding Principles, as described in [Scientific Data by Wilkinson et al](https://www.nature.com/articles/sdata201618):
- To be **Findable**
- To be **Accessible**
- To be **Interoperable**
- To be **Reusable**

## Why best practices in research software

There are many best practices currently in place that directly aim and are tailored for software developers. These includes aspects such as test-first programing and test coverage ([ref](https://github.com/r-lib/covr)), code quality ([ref](https://qaas.cyclopt.com/)), continuous integration ([ref](https://travis-ci.org)), etc. Unlike many software development best practices, this lesson aims to target a wider audience, particularly research funders, research institutions, journals, group leaders, and managers of projects producing research software. The adoption of these recommendations offer a simple mechanism for these stakeholders to promote the development of better software and an opportunity for developers to improve and showcase their software development skills.
