---
title: "Make software easy to discover by providing software metadata via a popular community registry"
teaching: 90
exercises: 45
questions:
- "Why are metadata important in research software?"
- "What are good metadata?"
- "Which are the most commonly used platforms for registering research software data."
objectives:
- "Understand the importance of metadata"
- "Understand why metadata are necessary for software discoverability"
- "Have a clear concept of what good metadata entail"
- "Use one of the existing platforms to upload metadata"
keypoints:
- "Metadata is for finding software and documentation for understanding software."
- "Metadata is essential in making research software findable."
- "Good (i.e. standardised) metadata ensures that the software is easily discoverable and reusable."
- "Different platforms use different levels of granularity in metadata."
- "[bio.tools](https://bio.tools/) is a good example of a software metadata registry in life sciences."
---

## What is metadata?

You are already using metadata, but you might not be fully aware of it.

**Definition**

Metadata (for data) can be defined as:
- ["A set of data that describes and gives information about other data"](https://en.oxforddictionaries.com/definition/metadata)
- ["Meta is a prefix that in most information technology usages means 'an underlying definition or description'"](https://whatis.techtarget.com/definition/metadata)

For some more information and examples, [follow this link](https://web.archive.org/web/20160306145239/http://www.theguardian.com/technology/interactive/2013/jun/12/what-is-metadata-nsa-surveillance#meta=0000000).

For the software case, we have defined metadata as "_a set of data that describes and gives information about software with the purpose of make it findable/discoverable_".


> ## Exercise: Think about metadata
> #### Time 5 minutes
>
> Let's think about why metadata is useful to describe a publication. We have for instance a title and authors. What other metadata can you think of? Why would you say those are metadata?
>
> By the end of this exercise, you should be able to better understand the difference between data and metadata.
>
> > ## Solution
> >
> > Some other common metadata for publications are starting page, ending page, journal where it was published, volume and item.
> >
> > They are considered metadata because they give you information about the publication but they are not the publication.
> >
> {: .solution}
{: .discussion}

## Documentation vs metadata
**Definition**
From Wikipedia, ["Software documentation is written text or illustration that accompanies computer software or is embedded in the source code. It either explains how it operates or how to use it, and may mean different things to people in different roles."](https://en.wikipedia.org/wiki/Software_documentation)

All software documentation can be divided into two main categories ([ref](https://www.altexsoft.com/blog/business/software-documentation-types-and-best-practices/)), _Product_ documentation and _Process_ documentation, with the former further broken down to _System_ and _User_ documentation. However, in the majority of cases in research software, documentation refers to _User documentation_, i.e. information in the form of manuals that are mainly prepared for end-users of the product and system administrators. As such, (user) documentation includes tutorials, user guides, troubleshooting manuals, installation, and reference manuals.

Opposed to the documentation, metadata helps describe the software in a standardized way, so it can be findable/discoverable, by both machines and humans.

> ## Software metadata vs documentation
>
> Metadata is for finding software while documentation is for understanding it.
>
{: .callout}


> ## Exercise: Highlighting the importance of metadata
> #### Time 20 minutes
>
> **Part 1**
> Split into Groups of 3-4; each group decides on "keywords" / placeholders for describing a movie (do **not** include the title!). Such keywords might include attributes such as _Director_, _Year_, _Actor(s)_, _Genre_, _Duration_, _Setting_, etc. As soon the placeholders are defined, every person in the group thinks of a movie and tries to describe it based on specific keywords.
> Do people identify the movie? If you put the keywords in Google, does it give you back the correct movie?
>
> **Part 2**
> Do the same thing but for a research tool (it can be of the same scientific discipline as the people comprising the group, or a general purpose tool).
>
> By the end of this exercise, you should be able to internalize what metadata are and what **good** metadata are.
>
> > ## Solution
> >
> > TODO
> >
> {: .solution}
{: .discussion}


## What are the existing commonly used standards descriptions for software metadata

**Definition**
A standard can be defined as:
- A structure agreed and adopted by a community
- A pattern or model used or accepted as normal or average
- A standard may be represented by an *ontology*, or a *controlled vocabulary*, etc.

A standard can be defined as "a structure agreed and adopted by a community" or as "a pattern or model used and accepted as normal or average". Standards may be represented by an Ontology, or a Controlled Vocabulary, etc.

> ## Ontology definition
>
> "In computer science and information science, an ontology encompasses a representation, formal naming, and definition of the categories, properties, and relations between the concepts, data, and entities that substantiate one, many, or all domains." - Wikipedia (https://en.wikipedia.org/wiki/Ontology_(information_science)
>
{: .callout}

**Controlled vocabularies** provide a way to organize knowledge for subsequent retrieval. It is usually a carefully selected list of words and phrases, which are used to tag units of information (document or work) so that they may be more easily retrieved by a search. The fundamental difference between an **ontology** and a **controlled vocabulary** is the level of abstraction and relationships among concept. A formal ontology is a controlled vocabulary expressed in an ontology representation language. ([ref](https://semwebtec.wordpress.com/2010/11/23/contolled-vocabulary-vs-ontology/))

Examples
- The [Gene Ontology](https://http://www.geneontology.org/) (GO) is the framework for the model of biology. The GO defines concepts/classes used to describe gene function, and relationships between these concepts. It classifies functions along three aspects: molecular function, cellular component and biological process
-  The [Climate and Forecast (CF) metadata](https://http://cfconventions.org/) are designed to promote the processing and sharing of files created with the NetCDF API. The CF conventions are increasingly gaining acceptance and have been adopted by a number of projects and groups as a primary standard. The conventions define metadata that provide a definitive description of what the data in each variable represents, and the spatial and temporal properties of the data.
- The [myGrid Ontology](https://http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.118.4077&rep=rep1&type=pdf) is designed to support web service discovery and composition in the bioinformatics domain. myGrid supports in silico experiments in the life sciences, enabling the design and enactment of workflows as well as providing components to assist service discovery, data and metadata management. The myGrid ontology is one component in a larger semantic discovery framework for the identification of the highly distributed and heterogeneous bioinformatics services in the public domain.  
- The [Sequence Ontology (SO)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1175956/) is a structured controlled vocabulary for genomic annotation. SO provides a common set of terms and definitions that will facilitate the exchange, analysis and management of genomic data.
- The [Darwin Core](https://http://rs.tdwg.org/dwc/) standard is body of standards. It includes a glossary of terms (in other contexts these might be called properties, elements, fields, columns, attributes, or concepts) intended to facilitate the sharing of information about biological diversity by providing reference definitions, examples, and commentaries.

## Standards for software metadata

- What is a good standard?
- How can I make sure that I am using a good standard?
- How to choose a standard?

The process in choosing a "good standard" is to see what is being (extensively) accepted in the scientific community. It should ideally be well known and highlighted by the existence of a certain number of citations.

Example of standards:
- [The Dublin Core Metadata Initiative](http://dublincore.org/)), or "DCMI"
It is an open organization supporting innovation in metadata design and best practices across the metadata ecology
- [CodeMeta](https://codemeta.github.io/)
Includes tools for preparing metadata in JSON format
- [Schema.org](https://schema.org/SoftwareApplication)
To describe software applications
- [SoftwareX Code metadata](https://www.journals.elsevier.com/softwarex)
To publish software with its respective metadata
- [EDAM Ontology](http://edamontology.org/page)
EDAM is a comprehensive ontology of well-established, familiar concepts that are prevalent within bioinformatics and computational biology, including types of data and data identifiers, data formats, operations and topics)
- [BioSchema.org](http://bioschemas.org/specifications/Tool/specification/)
Bioschemas is a community project built upon [schema.org](schema.org). It provides customisations, a.k.a. profiles, on top of schemas.org types and properties. Profiles include examples together with guidelines regarding cardinality, marginality and reuse of well-known vocabularies in Life Sciences.

The following table shows examples of metadata you would find on a software package in the SoftwareX journal. It gives a short description and a possible value.

|Description|Value|
|----|-----|
|Current code version| v 0.1.0|
|Permanent link to code/repository used for this code version | http://github.com/tool/code|
| Legal Code License | MIT |
| Code versioning system used | git |
| Software code languages, tools, and services used|  r, Java |
| Compilation requirements, operating environments & dependencies | 64-bit operating system & R environment version 3.2.3 and up (64-bit) & R packages: httr, rJava, xml2, data.table, foreach, doParallel, parallel |
| If available Link to developer documentation/manual | https://github.com/tool/documentation/ |
| Support email for questions | aperson@gmail.com |


> ## Exercise: Using a standard for creating metadata
> #### Time 10 minutes
>
> Ask the participants to go to the https://schema.org/SoftwareApplication and try to map the "metadata" they prepared for the previous movie/Software exercise. How many have you mapped? What are the top x metadata entries that you have missed and you think are necessary? What are your unmapped "metadata" that do not have a respective entry in schema - is there a closely related entry, or a composite one?
>
> > ## Solution
> >
> > Todo
> >
> {: .solution}
{: .challenge}


> Callout:
> This is a very complex way of adding metadata. Almost all of the time, you are better served by using an existing platform that is based on the standards that you have selected.
{: .callout}


## Existing platforms and tools for software metadata

The [schema.org](https://schema.org/SoftwareApplication) is the raw form of the possible metadata fields. It is very detailed but it is not readily useful for writing down the metadata of your software. Bioschemas has made an effort to narrow down and customise schema.org. types relevant for Life Sciences, one of them is the SoftwareApplication type. More information is available on [this link](http://bioschemas.org/specifications/Tool/specification/).


Adding metadata describing your software is commonly done via available platforms, that internally use those standards. The following list indicates some of the most prevalent ones:

1. [bio.tools](https://bio.tools)
This is a portal to bioinformatics resources worldwide, aimed to help bioinformaticians and scientists find, understand, compare and select resources, as well as use and connect them in workflows.

As a platform, it makes use of the [EDAM ontology](http://EDAMontology.org), and therefore provides a standardized vocabulary for providing metadata. Moreover, it includes aspects such as `language` and `platform`. However, it does not support filters by `language` nor does it assign a doi to the software (which is to be expected, as it serves as a registry and not a repository).

2. [OMICTools](https://omictools.com/)
This is a **commercial** service providing a registry of tools relevant in life sciences, containing sufficient metadata for connecting different tools in a single pipeline. However, it is not an open registry, i.e. the authors need to contact the development team in order for a tool to be included.

3. [Astrophysics Source Code Library](http://ascl.net/)
The Astrophysics Source Code Library (ASCL) is a free online registry for source codes of interest to astronomers and astrophysicists and lists codes that have been used in research that has appeared in, or been submitted to, peer-reviewed publications. It is fairly simple compared to other registries, but it focused on a particular domain (astrophysics).

4. [BioCatalogue](http://www.biocatalogue.org)
The BioCatalogue is a curated catalogue of Life Science Web Services. The BioCatalogue was launched in June 2009 at the Intelligent Systems for Molecular Biology Conference. The project is a collaboration between the myGrid project at the University of Manchester led by Carole Goble and the European Bioinformatics Institute led by Rodrigo Lopez. It is funded by the Biotechnology and Biological Sciences Research Council. It contains only web services. The BioCatalogue is based on an open source Ruby on Rails codebase.

5. [Metadata tools from the US Federal Geographic Data Committee](https://wiki.osgeo.org/wiki/Metadata_software)
This is a complete list of tools for capturing software metadata in the Geographic Data domain.

6. [Zenodo](https://zenodo.org/)
Zenodo is a research data repository. It was created by OpenAIRE and CERN to provide a place for researchers to deposit datasets. It launched in 2013, allowing researchers in any subject area to upload files up to 50 GB.
Zenodo has integration with GitHub to make code hosted in GitHub citable.
Zenodo is a general-purpose open access repository.


> ## Exercise: Using a registry, e.g., bio.tools
> #### Time 10 minutes
>
> Connect to the test instance of [bio.tools](https://dev.bio.tools/) and create a new entry on a software tool / github repo that you own or any of your favourite tools. You could find useful having a look to their [documentation on adding a tool](http://biotools.readthedocs.io/en/latest/user_guide.html#add-content).
>
> ![bio.tools main page](https://raw.githubusercontent.com/SoftDev4Research/4OSS-lesson/gh-pages/fig/bio-tools-main-ui.png)
>
> Once you are done, ask any of your colleagues what their tool is about. Use the search box to find it.
>
> > ## Solution
> >
> > We have a tool to visualize protein sequence annotations developed in JavaScript and hosted in GitHub. A publication indexed in PubMed is already available.
> >
> > These are the fields you would fill up to describe the tool we described:
> >
> > TODO: list of fields and so on.
> >
> > If you go to the search box and look for "protein visualisation", you will see an entry like:
> > TODO : add image
> >
> > That's it! You have published your tool in the development version or bio.tools. You are ready to go live and published your tool for real! Remember bio.tools focuses on life sciences.
> {: .solution}
{: .challenge}

## Wrap up
By adding good enough metadata to our research software, we are directly supporting its findability, thus increasing the overall visibility of the software. This is tied to the **findable** aspect of the FAIR principles mentioned in the introductory episode of this lesson.
