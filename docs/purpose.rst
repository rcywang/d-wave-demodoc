Purpose
=======
About this doc: Go more into detail here.  



Why did I make this?
--------------------
* Job posting, interest in QC, documentation (link to my mini textbook), self-proclaimed LaTeX enthusiast (or put this in an About Me section under PERSONAL
* How (went and learned)?
* Wanted to learn confluence... time-sensitive job posting? work-in-progress?
* Mention technical/scientific writing skills here.


What does this doc contain?
---------------------------
general overview of contents? set expectations (mix and match)



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
* Research


Contact
"""""""

* Technical support
* Company address / contact
* Community contribution
