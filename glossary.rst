.. _glossary:

Glossary Terms
==============

----

.. The following terms will appear in this documentation:

GitHub
    Github is a web-based Git repository hosting service. It is built for collaboration, providing features such as access control, bug tracking, version control, feature requests, task management, and more.


Sphinx 
    Sphinx is a tool for making intelligent and well-formatted documents, written by George Brandl and licensed under the BSD license. It was originally created for Python documnetation, and has facilities for the documentation of software projects in a range of languages. Some features include: output formats, extensive cross-references, hierarchical structure, automatic indices, code handling, extensions, and contributed extensions. Sphinx uses reST as its markup language.


reST 
    reStructuredText (reST) is an easy-to-read plaintext markup syntax and parser system. It is useful for in-line program documentation (e.g. Python docstrings), for quickly creating simple web pages, and for standalone documents. It is designed specifically for extensibility for application domains. It is a revision and reinterpretation of the `StructuredText <https://en.wikipedia.org/wiki/Structured_text>`_ and `Setext <https://docutils.sourceforge.io/mirror/setext.html>`_ lightweight markup systems.


Hybrid solver
    Quantum-classical hybrid solvers implement state-of-the-art classical algorithms together with intelligent allocation of the QPU to parts of the problem where it benefits most.


Quantum processing unit (QPU)
    Quantum computational element within a D-Wave system. Quantum annealing processors naturally return low-energy solutions; some applications require the real minimum energy (optimization problems) and others require good low-energy samples (probabilistic sampling problems). For a technical description, visit `Technical Description of the QPU <https://docs.dwavesys.com/docs/latest/doc_qpu.html>`_.
    


Quantum machine instruction (QMI)
    Set of information that is sent to the QPU, including the Ising model or QUBO parameters and annealing-cycle parameters.

Quantum annealing (QA)
    Quantum annealing is a metaheuristic for finding the global minimum of a given objective function over a given set of candidate solutions (candidate states), by a process using quantum fluctuations. For an in-depth description, visit `What is Quantum Annealing? <https://docs.dwavesys.com/docs/latest/c_gs_2.html>`_

Annealing cycle
    Physical process of starting with the QMI (prepared for the D-Wave system) and yielding a single sample to the QMI. Typically executed multiple times in a single QMI.

Sample, result, read, or solution
    Terms for the result yielded by an annealing cycle; ‘sample’ is preferred to connote the nondeterministic behavior of the QPU.


Rachel Wang 
    A quick learner, physicist/astrophysicist, and self-proclaimed LaTeX enthusiast.