---
title: "Adopt a licence and comply with the licence of third-party dependencies"
teaching: 0
exercises: 0
questions:
- "What a licence does?"
- "What is an open source licence?"
- "What is the importance of your lincece for third-party dependencies?"
objectives:
- Tell what is a copyright and what a licence does
- tell why is important that a product/code has a licence
- tell what is the importance of third-party dependencies on your product/code
- Choose a licence for your code
- Add a LICENCE file to a repository
keypoints:
- "First key point."
---

## What is public domain, a copyright and what a licence does?

### What is a copyright?

* Copyright is a legal right over the creative expression of an idea or an intellectual work. It grants the creator of an original work exclusive rights to determine and decide whether, and under what conditions, this original work may be used by others. 
* Copyright is automatically attached to every novel expression of an idea, including a poem or a blog entry, for a certain amount of years, typically from 50 to 100 years after the idea creator dies (depending on the jurisdiction). That is, the law assumes that as the author of your code, you have a say in what others can do with it.
* In particular, the code that you write is copyrighted by default in the most restrictive way. This implies that nobody, except you, can use, modify, create derivative works and distibute your code.
* If you infringe on someone's copyright you may be in the situation of having to pay reasonable damages.
Fair use (*Comparison*, *criticism* and *quotation* with citation) is an exception to copyright infringements. For example, you can publish a study comparing the performance or the accuracy of several different programs, without infringing the copyright of the programs.

> ### NOTE: Copyright vs Patent vs Trademarks
>
> **Copyright** protects the creative expression of ideas, **patents** protect novel technological inventions, **trademarks** protect ownership.
{: .callout}

> ### Challenge
>
> For each one of the three scenarios below, answer yes or no to the question.
> 
> 1. **Scenario:** you receive a sticker and your friends want a copy.
> 
>    **Question:** can you make a copy of the sticker and sell the copy to your friends?
>
> 2. **Scenario:** you receive a script from your supervisor asking you to modify it to analyse a different type of input data.
>
>    **Question:** are you allowed to do change the script?
>
> 3. **Scenario:** you download a collection of photos from a shared photo website?
>
>    **Question:** are you allowed to use the photos that you downloaded for your machine learning algorithm?
{: .challenge}

### What a licence does 

A licence is an official permission to do, use, or own something. Basically, a licence waives parts of a copyright by defining terms and conditions for the usage of a product.   
A shorthand definition of licence is "a promise by the licensor not to sue licensees" if they comply with the licence terms and conditions.   

What an open source licence does?

Authors of code tend to share it expecting that others will use, modify and share it. However, as the default is exclusive copyright, you need to explicitely state that you allow others to use, modify and share your code.   
The way to do it, is by assigning an open source licence to the code that you share with others, even if you are not publishing it but simply sharing it, e.g., by email.  
Notice that "if you do not assign an open source license to your project, everybody who contributes to it becomes an exclusive copyright holder of their work. That means 'nobody' can use, copy, distribute, or modify their contributions – includes yourself." [[ref]](https://opensource.guide/legal/)   

Also, you should be aware of whether other people's code, that you want to reuse or include in your project, has a licence and what type of licence it has. If you use, modify, or distribute a non licenced code, you are potentially liable to be sued by the code's owner.

How can you know which permissions you have from a licence? How can you know whether a project has an open source licence? See [https://choosealicense.com/](https://choosealicense.com/)

> ### Challenge
>
> Work in pairs. Ask learners to say wich permissions they have from a licence of a given software. Write permissions on sticky notes and stick them under each software name. Instructors should push learners to be more creative in terms of permissions. For example, can you sell the software? Can you sell support?
{: .challenge}

### Different licenses for different types of products (even data)


## Tell why is important that a product/code has a licence

* Why you need a licence
* Explain the differences between concepts such as [open](https://opensource.org/docs/osd) and proprietary

## Tell what is the importance of third-party dependencies on your product/code

Third-party dependencies are any library that you are using in your project that was wrote by someone else. For example, if your data analysis in R uses ggplot2 for the visualisation, ggplot2 would be a third-party dependence. Third-party dependencies have their own licenses that can be different from the license that you apply to your project but they should be compatible. The freedom provided by your license must not violate the restriction described in the license of the third-party depencency that you are using. For example:

The [GNU Affero General Public License](https://www.gnu.org/licenses/agpl-3.0.en.html) (AGPL) license says

> if you modify the Program, your modified version must prominently offer all users interacting with it remotely through a computer network (if your version supports such interaction) an opportunity to receive the Corresponding Source of your version by providing access to the Corresponding Source from a network server at no charge, through some standard or customary means of facilitating copying of software.

Therefore, if one of third-party libraries that you are using on your web app is licensed under this license, you should be aware that you will need to provide a copy of this AGPL third-party library that you are using.

Most of the open source licenses can be divided into two big groups: copyleft (or share-alike) and permissive. Copyleft licenses includes a clause that guarantees continued open access to a software and its source code in derivative works. The [GNU General Public License](https://www.gnu.org/licenses/gpl-3.0.en.html) is the most famous copyleft license and it says

> To protect your rights, we need to prevent others from denying you these rights or asking you to surrender the rights. Therefore, you have certain responsibilities if you distribute copies of the software, or if you modify it: responsibilities to respect the freedom of others.
>
> For example, if you distribute copies of such a program, whether gratis or for a fee, you must pass on to the recipients the same freedoms that you received. You must make sure that they, too, receive or can get the source code. And you must show them these terms so they know their rights.

Permissive licenses, as opposed to copyleft licenses, does not enforce that derivative works are licensed under the same terms or compatible terms of the original work. Famous examples of permissive licenses are the [MIT](https://opensource.org/licenses/MIT) and [BSD](https://opensource.org/licenses/BSD).

![Diagram](http://journals.plos.org/ploscompbiol/article/figure/image?size=large&download=&id=10.1371/journal.pcbi.1002598.g002)

> ### Challenge 1
>
> Work in pairs. Pick one item from the list below. Discuss with your partner what would be the implications to your project if one of the third-party libraries that you are considering to use, has the fragment mentioned in the selected item as part of their license.
> 
> 1. "Linking this library statically or dynamically with other modules is making a combined work based on this library. Thus, the terms and conditions of the GNU General Public License cover the whole combination."
>
>    Source: GNU Classpath's License
> 2. "The license granted hereunder will terminate, automatically and without notice, if you (or any of your subsidiaries, corporate affiliates or agents) initiate directly or indirectly, or take a direct financial interest in, any Patent Assertion: (...)"
>
>    Source: [React's License at 10 April 2015](https://github.com/facebook/react/blob/b8ba8c83f318b84e42933f6928f231dc0918f864/PATENTS).
> 3. "(...) each Contributor hereby grants to You a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable (except as stated in this section) patent license to make, have made, use, offer to sell, sell, import, and otherwise transfer the Work, where such license applies only to those patent claims licensable by such Contributor that are necessarily infringed by their Contribution(s) alone or by combination of their Contribution(s) with the Work to which such Contribution(s) was submitted."
>
>    Source: [Apace 2.0 License](https://opensource.org/licenses/Apache-2.0)
>
> > ### Solution to Challenge 1
> >
> > 1. If you distributed your project as a binary to your end user, your project must be licensed under the GNU General Public License because the binary make use (is linked) to the third-party library.
> > 2. In the future, you might not be able to use your software until you replace the third-party dependence or acquire a new license.
> > 3. You and your project is protected against patents owned by the contributor related with their contribution. If the third-party dependency does not have similar clause, you are a potential victim of a "[patent troll](https://en.wikipedia.org/wiki/Patent_troll)".
> {: .solution}
{: .challenge}

> ### Note: GPL vs LGPL vs AGPL
>
> The [Free Software Foundation](https://www.fsf.org/) publishes a family of licenses know as GNU General Public Licenses composed of (1) The GNU General Public License, (2) The GNU Lesser General Public License (GPL) and (3) The GNU Affero General Public License that are now at their third version. The GNU General Public License is a strong copyleft license that includes protection clauses for patents. The GNU Lesser General Public License is a version of GPL that has a clause stating that a binary form of the library can be distributed with one software without enforcing the copyleft clause on your code.  The GNU Affero General Public License is a version of GPL that has a clause stating that even if the software is being used over a network, the source code of it must be available to their users. Generally speaking, for-profit organisations will only use the GNU Lesser General Public License software.
{: .callout}

## Choose a licence for my code

In most countries, the use of one's original work such as a software by others is protected by law. Because of that, it is important that creators choose an appropriate licence when sharing their code by email or in platforms such as GitHub, GitLab, Bitbucket. The definition of original work is not trivial, but as a rule of thumb most code that are dozens of lines long would probably fit as original work. If your code is too small, a dozen of characters, it can not classify as original work in which case it is not protected by any law.

If you are the creator of an original work, you can decide the licence for it, but you should be careful of some common pitfalls:

* you are contributing to an existent project, in this case your contribution should be licence compatible with the project that you are contributing to;
* Giving away your copyright as part of your employment contract. This is very common and if this is the case you must seek permission of your employer to use a open source licence;
* the terms and conditions of the grant funding the project, this is getting more common since funding agencies are requiring research outputs to be open access in which case you must choose a compatible licence.

Since these are only three examples of issues that can arise, we recommend you to talk with the Intellectual Property (IP) office at your institution.

Once added, a licence and all future versions of the software, will be under that licence. Most projects never need to change licenses, but occasionally circumstances change. When changing a project’s license, there is one fundamental thing to consider: **all** project's existing copyright holders should give their agreement in writing and signed. This is complicated because, without a previous copyright transfer agreement, the list of copyright holders can have thousands of names. We recommand to have a look at the [guide from GitHub on this question](https://opensource.guide/legal/#what-if-i-want-to-change-the-license-of-my-project) for more details.

> ### Note: Dual License
>
> Some software that have comercial potential adopt a dual license model. They have a version of the code under the GNU General Public License that is freely available to everyone, but they also offer a proprietary version of the code in exchange of some cash. If you decide to adopt this business model, you must be very careful to correctly collect copyright transfer from all contributors to you.
{: .callout}

In principle, you can create your own bespoke licence, it's your right. However, we strongly discourage it, unless you have appropriate legal background. You are helping the users to understand the licence over your code or data by adopting an existing, widely described licence which better suits with your creation. So, users do not have to analyze the legal details of the licence to understand it.

* Example licences explained in terms of the concepts discussed previously
https://choosealicense.com/

## Add a LICENCE file to a repository

By including an open source license in your repository, it makes easier for other people to contribute. Most of the projects places their license information in a file named `LICENSE` (`LICENSE.txt` or `LICENSE.md` or `LICENSE.rst` or `COPYING`, `COPYING.txt`, `COPYING.md`, `COPYING.rst` are also used) in the root of the repository.

> ## Challenge 
> 
> Add the previously selected license to your GitHub repository
> 
> > ## Solution
> > 
> > Via the GitHub interface for an already existing repository
> > 1. On GitHub, navigate to the main page of the repository.
> > 2. Click on `Create new file` button above the file list
> > 3. Type `LICENSE` or `LICENSE.md` (with all caps) in the file name field
> > 4. Click on `Choose a license template` on the right
> > 5. Click on the selected license
> > 6. Check that the license terms correspond to the one
> > 7. Click on `Review and submit` button
> > 8. Commit the file
> > 
> > Locally: 
> > 1. Navigate to the root of the repository
> > 2. Open your favorite text editor with a new file
> > 3. Go to https://choosealicense.com
> > 4. Select your license by opening it page
> > 5. Click on `Copy license text to clipboard`
> > 6. Paste the content in the text editor
> > 8. Save the file as `LICENSE.md`
> > 9. Commit the added file
> > 
> > 
> > Via the GitHub interface for a new repository
> > 1. Start creation of a new repository
> > 2. Click on `Add a license`
> > 3. Select the chosen license
> {:.solution}
{:.challenge}

> ## Notes: Other places for license
> 
> Some projects also include the license in every individual file. This approach is appropriate when the project is a collection of small scripts that work independently.
> 
> Also, some projects have a short paragraph naming the license they use the README file with, for example, a note saying "This project is licensed under the terms of the MIT license.". 
{: .callout}
