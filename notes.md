# 4OSS lesson development kickoff CarpentryCon2018
when: June 1st 2018
where: Dublin, Ireland
Discussions during CarpentryCon 2018 workshop (originaly from the Etherpad)

Hashtag #4OSS

Participants:
* Mateusz Kuzak, [mateusz.kuzak@gmail.com](mailto:mateusz.kuzak@gmail.com); twitter: [@matkuzak](https://twitter.com/matkuzak), GitHub: [mkuzak](https://github.com/mkuzak)
* Paula Andrea Martinez, twitter: [@orchid00](https://twitter.com/orchid00), github: [orchid00](https://github.com/orchid00/)
* Fotis E. Psomopoulos, [fpsom@issel.ee.auth.gr](mailto:fpsom@issel.ee.auth.gr), [fopsom@gmail.com](mailto:fopsom@gmail.com), twitter: [@fopsom](https://twitter.com/fopsom), GitHub: [fpsom](https://github.com/fpsom)
* Jason Williams, williams@cshl.edu, twitter: [@JasonWilliamsNY](https://twitter.com/JasonWilliamsNY), Github: [JasonJWilliamsNY](https://github.com/JasonJWilliamsNY)
* François Michonneau, francois@carpentries.org, twitter: [@fmic_](https://twitter.com/fmic_), GitHub: [fmichonneau](https://github.com/fmichonneau)
* Ian van der Linde, ivdl@sun.ac.za, Github: [ianvdl](https://github.com/ianvdl)
* Thor Wikfeldt: kthw@kth.se, twitter: [@ktwikfeldt](https://twitter.com/ktwikfeldt), GitHub: [wikfeldt](https://github.com/wikfeldt)
* Allegra Via, allegra.via@gmail.com, twitter: [@elixir_ita](https://twitter.com/elixir_ita), GitHub: [allegravia](https://github.com/allegravia)
* Maneesha Sane, maneesha@carpentries.org; GitHub: [maneesha](https://github.com/maneesha), twitter: [maneeshasane](https://github.com/) 
* Gerard Capes, gerard.capes@manchester.ac.uk
* David Kane, dkane@wit.ie
* Scott Peterson, speterso@berkeley.edu
* David Perez-Suarez, d.perez-suarez@ucl.ac.uk
* Rhoda Aremu, 23925523@nwu.ac.za, ainarhoda@gmail; GitHub: [Tantoluwa](https://github.com/Tantoluwa)

## Agenda
1. Split into 4 teams:
* 1st recommendation "Make source code publicly accessible from day one"
* 2nd recommendation "Make software easy to discover by providing software metadata via a popular community registry"
* 3rd recommendation "Adopt a licence and comply with the licence of third-party dependencies"
* 4th recommendation "Define clear and transparent contribution, governance and communication processes"
    learning more about the 4OSS project / learning about lesson development

2. Readead the section for the recommendation of your choice from the original paper
https://f1000research.com/articles/6-876/v1

**Useful Links to project**
* lesson repository: https://github.com/SoftDev4Research/4OSS-lesson
* renderred lesson: https://softdev4research.github.io/4OSS-lesson/index.html
* summary website of the 4OSS paper    
   https://softdev4research.github.io/recommendations/
    
If you have a GitHub account, add content suggestions through issues:
    https://github.com/SoftDev4Research/4OSS-lesson/issues
    use issue labels per relative recommendation

If you don't have an account get help with getting one
or add commments below

**Other Relevant links**
* Open Source Guide https://opensource.guide
* Choose a license https://choosealicense.com
* Open Science Training Hanbook https://open-science-training-handbook.gitbooks.io/book/content/
* Biotools https://bio.tools
* EDAM Ontology http://edamontology.org/page
* Code is Science manifesto https://codeisscience.github.io/manifesto/manifesto.html
    
Learner profile:
       
Suggested order of Episodes

* 3rd recommendation "Adopt a licence and comply with the licence of third-party dependencies"
* 1st recommendation "Make source code publicly accessible from day one"
* 4th recommendation "Define clear and transparent contribution, governance and communication processes"
* 2nd recommendation "Make software easy to discover by providing software metadata via a popular community registry"

The idea is to go across all steps within the worskhop
- Put a single-line code in a repo
- Add license
- ...
- ...

We should have a concrete track / specific approach that can be applicable throughout the workshop. In each step we mention all the available options, but then we focus on the one particular approach/topic/platform/technology so that the exercises are specific.


## 1st recommendation "Make source code publicly accessible from day one"
lead: Mateusz

Suggestion: Licensing issues and institutional policies should be taught first in the workshop. Learners need to know if institutional policies, funders, may prohibit certian actions. Find this information before making code public. 

### Lesson objectives:
* Understand pros and cons of making source code public from day 1
* Make an informed decision whether OSS is appropriate for your software

### Discussion
* Write code for readability/re-usability (Where can you find style recomendations, what practices can you adopt  to make your code more readable) 
* Possible exercises : Reviwing style guides (PEP8?, parsing tools), Fixing some bad code, learning to write better functions and tests, learning how to comment well/write good documentation (Read the docs? GitHub pages?) - exercises could devide the room according to their abilities/interest/language/etc. What not to do: https://www.doc.ic.ac.uk/~susan/475/unmain.html
* Good coding practices in different languages
    * CodeRefinery material: http://cicero.xyz/v2/remark/github/bast/talk-complexity/master/talk.md/#1
* Know how to use a version control system
    * SWC git/Github lesson
* know the difference between version control and code hosting site (GitHub vs Git)
* Make a plan for incorporating feedback (code review, issue filing, etc.)
* Documentation is important!
    * CodeRefinery material, including exercises for Read the Docs and GitHub Pages: https://coderefinery.github.io/documentation/ 
* What nobody tells you about documentation: https://www.divio.com/en/blog/documentation/
* Special cases for reuse: Containers (singularity, docker, cloud)? - espcially useful for complex software deployments
    * binder/jupyter notebooks?

### Concepts:
* expose mistakes early, and get help in fixing them
* find collaborators
* Cover the Software Citation aspects (here or in licensing). Present Guidelines to doing so https://www.force11.org/software-citation-principles
* How are we going to deal with cases where a Research group is not willing to open their code from day 1.
* Could create confusion between version control (git) and the platform for making it publicly available (GitHub).
* What is version control?
* What is GitHub
* This lesson should cater (consider?) also for people who do not want / can have open code
* However, we should have a clear direction. We can decide what is should be about and then either convince people or make them understand whether the workshop is valid for them or not.
* Define what "source code" is, and what "Day 1" is.

### Learning Outcomes

## 2nd recommendation "Make software easy to discover by providing software metadata via a popular community registry"
lead: Fotis

### Learning Objectives 
* Stress out the importance of metadata
    * Discussion: what is your favorite/most used tool. Does it have metadata? Where is it accessible from?
* Clarify that the metadata captured may be different. Not standardized metadata can create problems (show the GEO "Age" issue)
* Be aware of the purpose of registries and aware of some popular resources:
* Platforms: CRAN/BioConductor (for R), PyPi, Conda etc? Focus on https://bio.tools/ as the "exercise" platform or maybe zenodo?
* Be aware of common standards/descriptions for software metadata (Bioinformatics, beyond?) and documentation needed for submission to registration
* EDAM Ontlology http://edamontology.org/page 
* How to raise visibility (traditional: publications JOSS https://joss.theoj.org/ , write a tutorial conferences, social media, etc.)
* Ways to promote software, give examples
* How to make a release (DOI/Package/etc)


(probably the last episode in the lesson)
* you've done all the work (license, public/open code, governance/policy) so now you put it out there.

### References/resources:
* https://zenodo.org/
* http://www.researchobject.org/
* https://figshare.com/
* https://www.codetriage.com/ (open discussion of issues in open source projects)
* https://codemeta.github.io/
* https://codeocean.com/
    
Create/Find a tool that can be used to verify/validate software adequate for submission to CRAN/PyPi etc..
* nothing is really required for submission to pypi, just some setup files and pypi config file

## 3rd recommendation "Adopt a licence and comply with the licence of third-party dependencies"
lead: Allegra

see: http://www.datacarpentry.org/rr-publication/

Before doing anything find out what is license and copyright policy in your institution

### Learning outcomes:
By the end of the episode, learners wlli be able to:
* Tell what is a copyright and what a licence does
* Stress out the importance of licencing a product/code
* Choose a licence for their code
* Add a LICENCE file to a repository
* Add the notice to the individual files

### Theory:
* What is a copyright
* What a licence does (waives parts of a copyright)
* Why you need a licence
* Explain the differences between concepts such as permissive, copyleft and proprietary
* Example licences explained in terms of the concepts discussed previously
* How can you change the licence applied to your repository? (N.B. mention that all previously published licences still apply to the older 
versions)

### Pitfalls:
* different licenses for different types of products
* Compatibility of dependencies
* Copyright ownership (IP ownership by university/institution/person) / team members / new contributors accepting the 
license (or transfer copyright: https://www.gnu.org/licenses/why-assign.en.html) / mention that copyright is shared between members 
* make sure the dependecy licenses and your software license are compatible, you can use the tool e.g. https://github.com/github/licensed
* you should use an existing licence. Do not write your own licence!
* Double licensing (comercialise to certain domains) / Other models of making money.

Exercises:
* Decide what's the most appropriate licence for your product
* choosealicence.com
* How to practically assign a licence to a project on GitHub:
    * How to add a LICENCE file to the repository (or COPYING as suggested by GPL)
    * How to add the notice to the individual files (suggested in GPL: https://www.gnu.org/licenses/gpl-howto.en.html / https://softwareengineering.stackexchange.com/questions/125836/do-you-have-to-include-a-license-notice-with-every-source-file )
     
### Instructor notes:
* Recommend to look up for Intelectual Property (IP) rules on the host institution/country/...
* Advices to talk with - IP officer, Research Services in the institution, Librarians (open access policy)

### References:
* CodeRefinery material: http://cicero.xyz/v2/remark/github/coderefinery/software-licensing/master/talk.md/#1
* https://choosealicense.com/
* http://www.thepublicdomain.org/enclosing-the-commons-of-the-mind/
* https://en.wikipedia.org/wiki/GNU_General_Public_License
    
## 4th recommendation "Define clear and transparent contribution, governance and communication processes"
lead: Paula

### Governance guidelines
* Define roles, define a minimun group of people to contribute to the project
* How can I contribute / How are new comers onboarded
    * Add a short part for first timers only
    * Be welcoming to contributors, have someone to contact
    * Include expectations and feedback time to respond to contributions
    * Invite people directly and encourge them to use their skills - feel on involvement
    * Be transparent about contributions - Be clear on what counts as a contribution to be listed as an author/contributor (and be explicit on potential commercial application of the product) 
    * Define timeframes, milestones, but be aware that people are contributing as volunteers, also add a regular timeframe for reviewers
    * have a list of todos (issues) so people can pick what to contribute with - Have open issues labeled for first-time contributors
    * Make step-by-step process on preferred way to contribute that includes times and expectations (e.g., open GitHub issue and submit a pull request that references it) - How to make a pull request
    * Build habit of involvement
    * Mentoring 
* Communication
    * Gratitute for the contributions    
    * Email/ issues/ members of a repo / slack / mailing list / video calls/minutes - focus on the problem that you are solving, long or short discussions, including the history
    * Have a space for discussions, when everyone is welcome
    * Project tracking (does time tracking fits here?)
------ from above maybe everything should be included in the documentation ----   
* Documentation - make a short outline or/and FAQs and (possibly) a larger version if needed 
    * Have a code of conduct 
    * Define scope of the project
    * Best practices (style guides), key concepts of the program goals 
    * Prototype (what should be included as a minimum)
     

### Resources - Examples
* https://opensource.guide/how-to-contribute/
* https://opensource.guide/building-community/
* https://ropensci.org/community/
* https://en.wikipedia.org/wiki/Wikipedia:Contributing_to_Wikipedia
* https://help.github.com/articles/about-project-boards/
* https://onboarding.ropensci.org/
* https://help.github.com/articles/about-project-boards/
* https://github.com/marketplace/category/project-management

Free for open source projects:
* https://github.com/marketplace/zenhub
* https://github.com/marketplace/zube free up to 4 users
* https://github.com/marketplace/waffle 
* https://github.com/marketplace/issue-sh free up to 5 users
* http://sciencetogether.online/tools/
* https://www.openproject.org/
* https://gitlab.com/
* https://opensource.com/
    
Code of conduct - examples
* https://www.contributor-covenant.org/
