Purpose
=======
This demo documentation is intended for my application to the `Technical Writer / Editor position <https://jobs.lever.co/dwavesys/063f504f-9402-4953-9429-cf14452e1436>`_ at D-Wave Systems. It is not meant for any other purpose.


Why did I make this?
--------------------

Last week (April 29, 2021), I found the job posting for the Technical Writer position. I decided to apply as the job description fits my interests in many ways, a few examples of which are listed below:

* I enjoy technical writing and often write documents on topics in physics that interest me. An example of this is my :ref:`QDG`... which is currently at 42 pages.
* I love to learn. I study physics in my spare time, writing technical documents and textbooks on each concept for future reference. I have many examples of such documents that I can share upon request.
* I am interested in quantum simulations (see my page on :ref:`neutralatomsim`), especially in quantum research. In particular, I was particularly intrigued by the transverse field Ising model (TFIM) after reading D-Wave's `Phase transitions in a programmable quantum spin glass simulator <https://science.sciencemag.org/content/361/6398/162>`_  paper.
* I have experience in Python, Markdown, **reStructuredText and Sphinx (this doc!)**, Jupyter Notebooks, Git; I am familiar with HTML and CSS. In particular, I am a self-proclaimed LaTeX enthusiast.

After visiting the `Ocean documentation <https://docs.ocean.dwavesys.com/en/stable/>`_, my enthusiasm for technical writing and typesetting motivated me to create my own demo documentation using Sphinx (in my spare time over the last week)... and I had fun doing so!



What does this doc contain?
---------------------------

As this documentation is both a demo for my documentation style and ability, and a resource to learn more about me (my :ref:`research`, :ref:`writing samples <quick-links>`, etc.), the content of this doc is a fusion of the two. Below I highlight and outline some of the most important sections of this doc:

* :ref:`methodology` -- an outline of how I structure my documentation and the reasoning for each of my choices/methods.
* :ref:`install` -- a partial sample of an Installation page, intended to show my structure and formatting.
* :ref:`quick-links` -- additional writing samples including an :ref:`MLOO`, with a brief description of the purpose for each document to provide context.
* :ref:`research` -- a thorough overview of how my research interests and experience align with the work done at D-Wave.





.. _methodology:

My Documentation Methodology
----------------------------

The following sections outline **my approach to writing (consumer-facing) technical documentation**. It is meant to give an idea as to what my documentation style looks like.


Good Documentation Practises
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Documentation is intended to give a comprehensive review of the project/software. When it comes to writing technical documents, especially those which are external-facing, there are a few things to keep in mind:

    Intended audience
        Documentation intended for public release should be clear, all-inclusive, and easily accessible. It is generally assumed the audience has little to no experience with the software.

    Durability
        As the project is updated, documentation must be current and easy to maintain. Versions and changes should be recorded in a :ref:`changelog`. Known bugs and fixes should be included as well.

    Participatory
        Working closely with software, hardware, support, and marketing teams to create documentation means documentation should be integrated into the standard workflow of developers. It should be intuitive such that additions and edits are easily incorporated by other authors.

    Content 
        Content should be ordered to cover prerequisite concepts first and sources should be stored as close as possible to the code which they document. The documentation should be cumulative, complete, and beautiful.
    
    Accessibility
        Navigating the documentation should be intuitive and must have a search feature for quick reference.
    
    Language
        Technical terms and acronyms should be defined (in-line or in a :ref:`Glossary <glossary>`). Documentation should be explicit with relevant examples or links to external resources for further reading.
    
    Style
        In general, the content should be skimmable, single-sourced, exemplary, consistent, and up-to-date. For readability, it is often helpful to adopt a documentation style guide. Many programming languages and frameworks provide coding standards, conventions, or best practises to improve code readability and uniformity. It makes collaboration and maintenance easier.


Content: What to Include?
^^^^^^^^^^^^^^^^^^^^^^^^^

Though it is tempting to include *everything* in documentation, including too much extraneous information can be overwhelming, clutter the document body, and dissuade users (especially newcomers) from using the documentation. To differentiate between relevant vs. irrelevant information, I abide by the following rules:

* **Keep it straightforward/minimal** -- often times users need not understand everything, they just want something that works.
* **Support best practises** -- focus on what has been proven functional and avoid including practises that break conventions.
* **Is 'X' content necessary?** -- if not, don't include it. If it may be semi-relevant, users can be redirected to the right communication channel.
* **Does 'X' enrich the content/product? Does it have value?** -- documentation should be treated as part of the product, so content should be tailored accordingly.





Basic Structure
^^^^^^^^^^^^^^^

For technical documentation, there are a few 'must-have' sections. Additionally, the hierarchical structure of the overall documentation is crucial, especially for intuitive navigation; users must be able to locate information quickly.

We can use the `Ocean Software <https://docs.dwavesys.com/docs/latest/index.html>`_ as an example. The major headlines that draw the user's attention should be items like:



Installation
""""""""""""

* Download (walkthrough, GitHub repo)
* Tutorials (set up, getting started, where to find more information)
* Software prerequisites / requirements
* Code examples


Examples
""""""""

* Code-in-action (for various cases)
* Common issues (FAQ) and fixes


Applications
""""""""""""

* Commercial
  * Optimization (e.g. social network analysis, traffic flow, web advertising, etc.)
  * Constraint satisfaction (e.g. portfolio optimization, scheduling, circuit fault detection, etc.)
* Research (link to papers on `arXiv <arXiv.org>`_)


Contact
"""""""

* Technical support
* Company address / contact
* Community forum
