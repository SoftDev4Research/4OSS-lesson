---
title: "Make software easy to discover by providing software metadata via a popular community registry"
teaching: 90
exercises: 0
questions:
- "Why are metadata important in research software?"
- "What are good metadata?"
- "Which are the most commonly used platforms for registering research softwaetadata."
objectives:
- "Understand the importance of metadata."
- "Understand why meta-data are necessary for software discoverability."
- "Have a clear concept of what good metadata entail."
- "Use one of the existing platforms to upload metadata."
keypoints:
- "Metadata is for finding software and documentation for understanding software."
- "Metadata is essential in making research software findable."
- "Good (i.e. standardised) metadata ensures that the software is easily discoverable and reusable."
- "Different platforms use different levels of granularity in metadata."
- "[bio.tools](https://bio.tools/) is a good example of a software metadata registry in Life Sciences."
---

## What is metadata?

You are already using meta-data, but you might not be fully aware of it.

**Definition**
Metadata (for data) can be defined as [“a set of data that describes and gives information about other data”](https://en.wikipedia.org/wiki/Metadata) or [“Meta is a prefix that in most information technology usages means 'an underlying definition or description'”](https://whatis.techtarget.com/definition/metadata). For some more information and examples, just [follow this link](https://web.archive.org/web/20160306145239/http://www.theguardian.com/technology/interactive/2013/jun/12/what-is-metadata-nsa-surveillance#meta=0000000). 

For the software case, we have defined metadata as “a set of data that describes and gives information about software with the purpose of make it findable/discoverable”

> ## Exercise: Thinking of metadata
> #### Time 5 minutes
>
> Let's think about metadata useful to describe a publication. We have for instance title and authors. What other metadata can you think about? Why would you say those are metadata?
> 
> By the end of this exercise, you should be able to better understand the difference between data and metadata.
>
> > ## Solution
> >
> > Some other common metadata for publications are starting page, ending page, journal where it was published, voumen and item. 
> > 
> > They are considered metadata because they give you information about the publication but they are not the publication. 
> > 
> {: .solution}
{: .discussion}

## Documentation vs Metadata
**Definition**
From Wikipedia, [“Software documentation is written text or illustration that accompanies computer software or is embedded in the source code. It either explains how it operates or how to use it, and may mean different things to people in different roles.”](https://en.wikipedia.org/wiki/Software_documentation)

That is, metadata helps describe the software in a standardised way, so it can be findable/discoverable, by both machines and humans.

> ## Software metadata vs documentation
>
> Metadata is for finding software while documentation is for understanding it
>
{: .callout}


## What are the existing / commonly used standards / descriptions for software metadata (Fatma)

**Definition**
A standard can be defined as:
- A structure agreed and adopted by a community
- A pattern or model used or accepted as normal or average
- A standard may be represented by an Ontology, or a Controlled Vocabulary, etc

For capturing good meta-data, it is better to use an existing standard

> ## Ontology definition 
>
> “In computer science and information science, an ontology encompasses a representation, formal naming, and definition of the categories, properties, and relations between the concepts, data, and entities that substantiate one, many, or all domains.” - Wikipedia (https://en.wikipedia.org/wiki/Ontology_(information_science)
>
{: .callout}


Examples
- The [Gene Ontology](https://http://www.geneontology.org/) is the framework for the model of biology. The GO defines concepts/classes used to describe gene function, and relationships between these concepts. It classifies functions along three aspects:molecular function, cellular component and biological process
-  The [CF (Climate and Forecast) metadata](https://http://cfconventions.org/) are designed to promote the processing and sharing of files created with the NetCDF API. The CF conventions are increasingly gaining acceptance and have been adopted by a number of projects and groups as a primary standard. The conventions define metadata that provide a definitive description of what the data in each variable represents, and the spatial and temporal properties of the data.
- The [myGrid ontology](https://http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.118.4077&rep=rep1&type=pdf) is designed to support web service discovery and composition in the bioinformatics domain. myGrid supports in silico experiments in the life sciences, enabling the design and enactment of workflows as well as providing components to assist service discovery, data and metadata management. The myGrid ontology is one component in a larger semantic discovery framework for the identification of the highly distributed and heterogeneous bioinformatics services in the public domain.  
- The [Sequence Ontology (SO)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1175956/) is a structured controlled vocabulary for genomic annotation. SO provides a common set of terms and definitions that will facilitate the exchange, analysis and management of genomic data. 
- The [Darwin Core](https://http://rs.tdwg.org/dwc/) standard is body of standards. It includes a glossary of terms (in other contexts these might be called properties, elements, fields, columns, attributes, or concepts) intended to facilitate the sharing of information about biological diversity by providing reference definitions, examples, and commentaries. 


**About good standards**

- What is a good standard? 
- How can I make sure that I am using a good standard? 
- How to choose a standard?

The process in choosing a "good standard" is to see what is being (extensively) used by the community. It should ideally be well known and highlighted by the existence of a certain number of citations.



Examples in Life Sciences:
- [EDAM Ontology](http://edamontology.org/page)
EDAM is a comprehensive ontology of well-established, familiar concepts that are prevalent within bioinformatics and computational biology, including types of data and data identifiers, data formats, operations and topics)
- [BioSchema.org](http://bioschemas.org/specifications/Tool/specification/)
Bioschemas is a community project built upon [schema.org](schema.org). It provides customisations, a.k.a. profiles, on top of schemas.org types and properties. Profiles include examples together with guidelines regarding cardinality, marginality and reuse of well-known vocabularies in Life Sciences.

General Examples
- [CodeMeta](https://codemeta.github.io/)
Includes tools for preparing meta-data in JSON format
- [Schema.org](https://schema.org/SoftwareApplication)
To describe software applications 
- [SoftwareX Code meta-data](https://www.journals.elsevier.com/softwarex)

|Code|metadata|
|----|-----|
|Current code version| v 0.1|
|Permanent link to code/repository used for this code version | http://github.com/tool/code|
| Legal Code License | MIT |
| Code versioning system used | git |
| Software code languages, tools, and services used|  r, Java |
| Compilation requirements, operating environments & dependencies | 64-bit operating system & R environment version 3.2.3 and up (64-bit) & R packages: httr, rJava, xml2, data.table, foreach, doParallel, parallel |
| If available Link to developer documentation/manual | https://github.com/tool/documentation/ |
| Support email for questions | aperson@gmail.com |



> ## Exercise: Using a registry, e.g., bio.tools
>
> Ask the participants to go to the http://bioschemas.org/specifications/Tool/specification/ and try to map the “metadata” they prepared for the previous movie/Software exercise, focusing only on software this time. How many have you mapped? What are the top x metadata entries that you have missed and you think are necessary? What are your unmapped “metadata” that do not have a respective entry in schema - is there a closely related entry, or a composite one? 
> 
> > ## Solution
> >
> > Todo
> > 
> {: .solution}
{: .challenge}


> Callout:
> This is a very complex way of adding meta-data. Almost all of the time, you are better served by using an existing platform that is based on the standards you’ve selected.
{: .callout}



## What are the existing meta-data platforms and tools that can be used (Radka)

The [schema.org](https://schema.org/SoftwareApplication) is the raw form of the possible meta-data fields. It is very detailed but it is not readily useful for writing down the meta-data of your software. Bioschemas has made an effort to narrow down and customise schema.org. types relevant for Life Sciences, one of them is the SoftwareApplication type. More information is available on [this link](http://bioschemas.org/specifications/Tool/specification/).

Adding metadata describing your software is commonly done via available platforms, that internally use those standards. The following list indicates some of the most prevelant ones:

1. [bio.tools](https://bio.tools)
This is a portal to bioinformatics resources worldwide, aimed to help bioinformaticians and scientists find, understand, compare and select resources, as well as use and connect them in workflows.
As a platform, it makes use of the [EDAM ontology](http://EDAMontology.org), and therefore provides a standardised vocabulary for providing meta-data. Moreover, it includes aspects such as `language` and `platform`. However, it does not support filters by `language` nor does it assign a doi to the software (which is to be expected, as it serves as a registry and not a repository).

2. [OMICTools](https://omictools.com/)
This is a fairly big registry of tools relevant in Life Sciences, containing sufficient metadata for connecting different tools in a single pipeline. However, it is not an open registry, i.e. the authors need to contact the development team in order for a tool to be included.

3. [Astrophysics Source Code Library](http://ascl.net/)
The Astrophysics Source Code Library (ASCL) is a free online registry for source codes of interest to astronomers and astrophysicists and lists codes that have been used in research that has appeared in, or been submitted to, peer-reviewed publications. It is fairly simple compared to other registries, but it focused on a particular domain (astrophysics).

4. [BioCatalogue](http://www.biocatalogue.org)
The BioCatalogue is a curated catalogue of Life Science Web Services. The BioCatalogue was launched in June 2009 at the Intelligent Systems for Molecular Biology Conference. The project is a collaboration between the myGrid project at the University of Manchester led by Carole Goble and the European Bioinformatics Institute led by Rodrigo Lopez. It is funded by the Biotechnology and Biological Sciences Research Council. It contains only web  services. The BioCatalogue is based on an open source Ruby on Rails codebase 

5. [Metadata tools from the US Federal Geographic Data Committee](https://wiki.osgeo.org/wiki/Metadata_software)
This is a complete list of tools for capturing software metadata in the Geographic Data domain.

6. [Zenodo](https://zenodo.org/)
Zenodo is a research data repository. It was created by OpenAIRE and CERN to provide a place for researchers to deposit datasets. It launched in 2013, allowing researchers in any subject area to upload files up to 50 GB.
Zenodo has integration with GitHub to make code hosted in GitHub citable.
Zenodo is a general-purpose open access repository.

> ## Exercise: Using a registry, e.g., bio.tools
>
> Connect to the test instance of [bio.tools](link to test instance) and create a new entry on a software tool / github repo that you own or any of your favourite tools. You could find useful having a look to their [documentation on adding a tool](http://biotools.readthedocs.io/en/latest/user_guide.html#add-content). 
> 
> TODO: bio.tools image
>
> Once you are done, as any of your colleagues what their tool is about. Use the search box to find it.
> 
> > ## Solution
> >
> > We have a tool to visualise protein sequence annotations developed in JavaScript and hosted in GitHub. A publication indexed in PubMed is already available.
> > 
> > These are the fields you would fill up to describe the tool we just described:
> > 
> > TODO: list of fields and so on.
> >
> > If you go to the search box and look for "protein visualisation", you will see an entry like:
> > TODO : add image
> > 
> > That's it! You have published your tool in the development version or bio.tools. You are ready to go live and published yout tool for real! Just remember bio.tools focuses on Life Sciences.
> {: .solution}
{: .challenge}

## Wrap up
We are increasing visibility, because we are supporting findability by adding the correct/good meta-data -> Connect this with FAIR principles.


**Instructor Notes / Setup**
- [Local Installation of Zenodo](https://github.com/zenodo/zenodo/blob/master/INSTALL.rst)
It may be interesting to have a local installation of zenodo to play around. The instructions using Docker are available on the link above.
 
- [Bio-Linux](http://environmentalomics.org/bio-linux-software-list/)
It is a final OS containing tools that have been already published, connected meta-data, etc
