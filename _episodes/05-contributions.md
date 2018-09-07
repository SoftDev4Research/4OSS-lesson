---
title: "Define clear and transparent contribution, governance and communication processes"
teaching: 90
exercises: 45
questions:
  - "How does someone start contributing to my project?"
  - "What do I need to consider about project design and governance?"
  - "How do people communicate within the project?"
objectives:
  - "Design the minimum guidelines for people to contribute and engage with the project"
  - "Define how you would support your contributors"
  - "Establish roles, expectations and processes around contributions to the project"
  - "Create communication strategies among people in the project"
keypoints:
  - "Having clear guidelines for contribution makes it easier for others to contribute to the project, improving it and increasing its sustainability."
  - "Having a governance structure that is appropriate for the size of the project, will support its growth, and make it more welcoming to new contributors."
  - "Clarifying project goals and ways of communication saves time for current and new contributors."
---

## Clear and transparent contributions

So far, you have a github repository to share your project, you've added a `README`, 
`LICENCE` and metadata to it. Now, to make things even better, why not think about
 inviting others to make contributions to your project!

We can start discussing some of the aspects that you as project owner
should have in mind to make contributions as clear and transparent as possible.

> ## Discussion: What are the benefits of having external contributions in your project?
> #### Time: 3 min
> Think and list how your project might benefit from having people contributing to it.
> What kind of challenges do you expect will arise from having outside contributors to your project?
> Which strategies can you put in place to mitigate these challenges?
>
> > ## Outcome
> >
> > In this discussion, learners should acknowledge the importance of contributors
> > in the development of the project.
> {: .solution}
{: .discussion}

## Focus on contributors

Making your project open provides a great opportunity for the community to 
contribute to its enhacement. Think about the involvement and contributions from
the general audience, and the specific audience, like developers, designers and users.
Both of these groups of people can improve their reviewing skills and make 
high quality impactful decisions in the project. They can also connect with like-minded
people while building the profile of active contributor in the project.

### Welcome your contributors!

Make your contributors feel welcome, treat them well, respond to their queries
and allow them to demonstrate their abilities. Being welcoming to your contributors
sets the tone for future contributors, and incites future  contributors to
also contribute to your project. To allow meaningful contributions,
it is crucial to make your project [FAIR](https://www.nature.com/articles/sdata201618)
(Findable, Accessible, Interoperable and Reusable). Define your project clearly,
by listing the aim of the project, areas of applications and area of improvements.
List all the resources such as your source-code, datasets, metadata,
documentation, list of tasks, and contribution guidelines.

### Respect your contributors!

It is a lot to consider, but remember that in the vast majority of cases,
people take time to contribute to your project because they find what you created
useful and want to improve it. These contributors may spend considerable amount of
their time (often voluntarily) to work on your project, so be respectful.
If your issue tracker is filled with ignored emails or comments, rude replies,
and uncalled bad behavior, your project will not be attractive for contributors.

> ## Discussion: What should others know before contributing to your project?
> #### Time: 10 min
> Have you ever contributed to a project? What did you need to know to
> contribute to that project? Based on your own experience, list the minimum
> required information someone needs to contribute to your project.
>
> > ## Outcome
> >
> > In this exercise, learners should realise the importance of providing appropriate
> > information to allow others to make contributions to the project, without
> > overwhelming or confusing them.
> >
> > Then you might suggest to include a minimum example document for contributing.
> > The contribution file should contain the bare minimum information:
> > - location: root-project/CONTRIBUTING.md
> > - cheer: Give a super nice welcome to contributors!
> > - introduction: Overview of the document
> > - how-to: Show one or two examples of contributions and time frame
> >
> > Further reading: 
> > - [https://rubygarage.org/blog/how-contribute-to-open-source-projects](https://rubygarage.org/blog/how-contribute-to-open-source-projects)
> {: .solution}
{: .discussion}

If you are not yet convinced that having your project open for contributions is
a great idea, we can go through some questions that a potential
contributor might ask.

1. Where can I contribute?
2. How can I contribute?
3. Who should I contact?
4. What are the communication channels?
5. What else should I know?
6. What's in it for me?

Although addressing all these questions is a very good idea, sometimes people just want a clear-cut guideline. So, first think about the minimal required information that you can provide to your contributors without overwhelming them.

> ## Challenge: Part I - Creating a Minimal Contributor’s Guideline
> #### Time: 10 minutes
> Hands on exercise to create a minimal contributor’s Guideline
> CONTRIBUTING.md
>
> > ## Solution
> >
> > A minimal CONTRIBUTING.md file must consist on the following information
> > - Acknowledgement/welcome to people who intend to contribute
> > - An example or two of how to contribute
> > - A main way of contact
> > - A short response to a contribution
> >
> {: .solution}
{: .challenge}

> ## Challenge: Part II - Review examples from other projects
> #### Time: 10 minutes
>
> Read two or three of the contributing guidelines examples listed below, and pick one element that you
> had not thought about, and that you think would be a useful addition to your project guidelines.
>
> - [Atom](https://github.com/atom/atom/blob/master/CONTRIBUTING.md)
> - short example [R for Data Science book](http://r4ds.had.co.nz/contribute.html)
> - [Galaxy Project](https://github.com/galaxyproject/galaxy/blob/dev/CONTRIBUTING.md)
> - [How to contribute to open source](https://opensource.guide/how-to-contribute/)
> - [pandas](https://pandas.pydata.org/pandas-docs/stable/contributing.html)
> - [GO](https://golang.org/doc/contribute.html)
> - [Mozilla Science working open](https://github.com/mozillascience/working-open-workshop/blob/gh-pages/handouts/contributing.md)
> - [Django advice for new contributors](https://docs.djangoproject.com/en/dev/internals/contributing/new-contributors/)
> - [Py4J - A Bridge between Python and Java](https://www.py4j.org/contributing.html)
> - [JuliaLang](https://github.com/JuliaLang/julia/blob/master/CONTRIBUTING.md)
> - [dplyr](https://github.com/tidyverse/dplyr/blob/master/.github/CONTRIBUTING.md)
> - [octobox](https://github.com/octobox/octobox#contribute)
> - [scipy](https://github.com/scipy/scipy/blob/master/CONTRIBUTING.rst)
> - [plotly](https://github.com/ropensci/plotly/blob/master/CONTRIBUTING.md)
> - [scrubr](https://github.com/ropensci/scrubr/blob/master/CONTRIBUTING.md)
> - [rOpenSci](https://github.com/ropensci/dev_guide/blob/master/maintenance_contributing.Rmd)
> - Ubuntu Contributing Guide: [short version](https://discourse.ubuntu.com/t/contribute/26) and [longer version](https://wiki.ubuntu.com/ContributeToUbuntu).
> - Short example [sf](https://github.com/r-spatial/sf#contributing)
> - [knitr](https://github.com/yihui/knitr/blob/master/.github/CONTRIBUTING.md)
> - [rmarkdown](https://github.com/rstudio/rmarkdown/blob/master/CONTRIBUTING.md)
{: .challenge}

### Support your contributors!

As your project grows and more people start to contribute, in addition to the
minimal `CONTRIBUTING` file you might need to provide support to your
contributors. Support encourages them to make future contributions and to remain active.
For example, it's important to identify what motivates people to contribute,
what resources do they need to work on your project (e.g.codes, data, metadata),
what are the right skills to work on a certain task, and if they lack any skill,
they have resources to help them develop those skills.

### Acknowledge your contributors!

As the project lead/author/owner, you should acknowledge all your contributors and reward their
contributions, for example, by mentioning them in your contributors list,
by offering them opportunities to become a mentor,
invite them as co-authors if their contribution is substantial and essential. 

How you acknowledge your contributors can be explained
in a simple paragraph, or covered in more details in the `CONTRIBUTING` file. If it is more extensive add links to a separate document, this will depend on the size of your project and team.

> ## Discussion: Supporting your contributors
> #### Time: 5 minutes
> Think about the different resources that contributors might need, in
> order to make a contribution. Also think at what stages these
> resources might be needed.
> Discuss in groups and list the resources.
>
> > ## Solution
> >
> > Here is a list of recommendations to provide support to your
> > contributors, but remember this is not an exhaustive list.
> > - Installation instructions
> > - Style guidelines
> > - FAQ’s
> > - Code review process
> > - Resources to develop skills required to contribute to the project
> > - Community calls / meetings
> > - Archive
> {: .solution}
{: .discussion}

### Promote your work

To get relevant contributions, it is also worth thinking
about reaching out to your audience (potential future contributors) by engaging
with your community by presenting your tools at conferences or workshops,
promoting it online and being active on the appropriate communication channels.

## Governance

Governance in an open source software project is a management framework for
dynamic decision making. A governance structure aims at the assignment of roles, timing and tasks related to the project. Ideally, this structure clearly defines
responsibilities, accountability and recognition. Roles are attributed by
managers while developing, testing, documenting and reviewing.

At the start of your project, when a few people are involved in its development, your governance
structure may be simple and roles may overlap. As your project grows, you as project manager/lead may need to
redistribute responsibilities.

A clearly defined governance structure not only allows your contributors to identify the correct
contact person, but also helps them to identify roles that they can fill in your project.

A properly managed project uses governance to make sure that there are no responsibilities
left behind, unassigned, and optimises for scalable development.

> ## Challenge
> #### Time: 10 min
>
> Assign levels of priority needed in the project design and governance
> (choose one level per line and justify your choice)
>
> |---|---|---|---|---|
> |Topic|High|Medium|Low|Justify your choice|
> |About the project|||||
> |Ownership|||||
> |Roles and Responsibilities|||||
> |License|||||
> |Funding|||||
> |Timeline|||||
> |Outreach||||||
>
> > ## Solution
> >
> > The priorities will be different and that's OK. Discussions among learners who chose different 
> > priorities will convince them of the need
> > for governance and transparency in open source projects. This will clarify the contributors' roles
> > and responsibilities within projects.
> {: .solution}
{: .challenge}

## Communication

Let's now talk about transparent communication processes. There are several options available
to establish transparent communication with everyone involved in an open source project.
However, the choice of communication channel depends on the team size, which also
influences the frequency of communications. From the start of your project, use open
and public communication channels for members of your project. Issue threads, mailing lists and other online
forums work well for open source projects, and scale well as your project grows. As your team
grows you may need to create additional and separated communication channels, so that you reach your
target audience on time, and with announcements that benefit a specific audience.

> ## Discussion: Develop communication strategies
> #### Time: 5 minutes
> Let's discuss what types of communication media do people prefer. Think about the team size,
> and what would be most convenient way for people to communicate and get updates.
>
> > ## Solution
> >
> > Here is a list of recommendations. However, the efficient solutions will
> > depend on the frequency of communication and the team size.
> > - Community calls/meetings
> > - Email list
> > - Slack
> > - Twitter
> > - GitHub issues
> > - Announcements (newsletters/updates)
> > - Archive
> {: .solution}
{: .discussion}

## Recommendations

The following checklist contains some points to be addressed in order to make 
contributions easier, clearer and more transparent

> ## A checklist of things that can be included in your Contributing guidelines
>
> 1. Where can I contribute?
> - User agreement
> - Fixing typo
> - Reporting and fixing bugs/errors
> - Contributing to documentation
> - Adding code/features
> - Testing
> - Writing papers
> - Promoting
> - Share ideas with the Community
> - Organise events
>
> 2. How can I contribute?
> - Technical requirements (software versions, space, etc)
> - Skill requirements (programming language)
> - Available resources
> - Is there a style guide to refer to?
> - What is allowed and not allowed
> - What happens with my contributions
> - Time frame that someone from the team responds to a contribution
> - What if the contribution is accepted/rejected
> - Citing your contributions (optional description of author, contributor, etc.)
>
> 3. Who should I contact?
> - Main contact
> - Owner
> - Developer
> - Maintainer
> - Helper
> - Tester
> - Admin
>
> 4. What are the communication channels?
> - Communication channels
> - Announcements (newsletters, updates)
> - Archive
>
> 5. What else should I know (links)?
> - License
> - Disclaimers
> - Policies
> - Code of conduct
> - Data protection
> - Main project page
> - Main documentation
> - Members/contributors page
> - Resources to develop skills required for working on the project
>
> 6. What's in it for me?
> - Develop new skills
> - Find people with similar interests
> - Find a mentor
> - Teach others
> - Learn how to work on open source projects
>
> 7. I don’t want to read all these, I only have a question!
> - One contact person
> - Minimal document
{: .solution}

## Nice testimonials examples of people contributing publicly

> ## Testimonial
>
> "For me this experience has been incredible! Thank you for putting all your
> effort into this project. Many people responded with overflowing enthusiasm
> to participate and collaborate in the different facets of this project.
> It was a pleasure to work with all of you." - H.S.
{: .testimonial}

> ## Tweet
>
> <blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">&quot;Now when I&#39;m writing a book I just make a lot of stupid mistakes in public. But it&#39;s fine b/c ppl are nice and they help me fix them.&quot; -<a href="https://twitter.com/hadleywickham?ref_src=twsrc%5Etfw">@hadleywickham</a> <a href="https://twitter.com/hashtag/bookdown?src=hash&amp;ref_src=twsrc%5Etfw">#bookdown</a> <a href="https://twitter.com/hashtag/rstats?src=hash&amp;ref_src=twsrc%5Etfw">#rstats</a> <a href="https://twitter.com/hashtag/tidyverse?src=hash&amp;ref_src=twsrc%5Etfw">#tidyverse</a> <a href="https://twitter.com/hashtag/jsm2018?src=hash&amp;ref_src=twsrc%5Etfw">#jsm2018</a> <a href="https://t.co/uYlTR4igRs">pic.twitter.com/uYlTR4igRs</a></p>&mdash; Joyce Robbins (@jtrnyc) <a href="https://twitter.com/jtrnyc/status/1024330878426595328?ref_src=twsrc%5Etfw">July 31, 2018</a></blockquote>
> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
{: .testimonial}

## Resources: Extra links

- The book
  "[Producing Open Source Software, How to Run a Successful Free Software Project](https://producingoss.com/)",
  by Karl Fogel provides a comprehensive overview of the different aspects of
  managing an open source software project, and includes advice and guidelines
  to set up your project and facilitate contributions.
- Mozilla ScienceLabs [short presentation on how to build the CONTRIBUTING.md file](https://docs.google.com/presentation/d/1YZA8rvD2Ix4F7y4ck44XYwTlQZ_YkM4higpuwy5swy8/edit#slide=id.gef398db8c_0_0)
- [How to Contribute?](https://opensource.guide/how-to-contribute/) from the
Open Source Guides
- [How to build welcoming communities?](https://opensource.guide/building-community/) from the Open Source Guides.
- [Contributing to Wikipedia](https://en.wikipedia.org/wiki/Wikipedia:Contributing_to_Wikipedia)
- https://github.com/marketplace/category/project-management
    -- Free for open source projects
    https://github.com/marketplace/zenhub
    https://github.com/marketplace/zube free up to 4 users
    https://github.com/marketplace/waffle
    https://github.com/marketplace/issue-sh free up to 5 users
    http://sciencetogether.online/tools/
- [OpenScienceMOOC](https://github.com/OpenScienceMOOC)
- [openproject] https://www.openproject.org/
- [Prefer to use other version control like GitLab](https://gitlab.com/)
- [opensource](https://opensource.com/)
- [Mozilla Science working open](http://mozillascience.github.io/working-open-workshop/)
- [Commision recommendation (EU) 2018 on access to and preservation of scientific information](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32018H0790) point 12
- [rubygarage](https://rubygarage.org/blog/how-contribute-to-open-source-projects)
- Shiny app that randomly picks an issue from an open source project to help with: <https://ropensci.shinyapps.io/contributr/>
- The rOpenSci R package [Collaboration Guide](https://ropensci.github.io/dev_guide/collaboration.html)
- The rOpenSci R package [Contributing Guide](https://ropensci.github.io/dev_guide/contributingguide.html)
