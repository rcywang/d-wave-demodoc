.. _MLOO:

ML Review Paper
===============
As someone who is interested -- but by no means an expert -- in machine learning, I decided to enter the *Spectra Review Paper competition* on cutting-edge techniques in machine learning (ML). I was inspired by a paper [Wigley2016]_ on the use of ML **online optimization** in the production of Bose-Einstein Condensates (BECs), as my graduate research focus is on cold-atom experiments [#foot1]_. The benefit of entering the competition was two-fold:

    1. In researching the techniques and applications of ML in cold-atom experiments, I learned about various *online optimization* schemes that search for the optimal experimental settings in real-time (or *online*). Perhaps most importantly, I reviewed optimizers (e.g. Nelder-Mead) and optimization methods (e.g. Adam, AdaGrad, RMSProp, etc.) -- both of which are highly relevant for the efficient production of Bose-Einstein Condensates (BECs). In the context of cold-atom experiments, I compared various optimization strategies, using properties such as the convergence rate and the sample size/quality to judge performance.
    2. The two methods I reviewed in depth -- ML online optimization and **single-shot absorption imaging** [Ness2020]_ -- are quite different in their approach. The **Machine-Learning Online Optimization Package (M-LOOP)** is focused on the apparatus itself, using Bayesian optimization to search for the optimal experimental settings. In contrast, the goal of single-shot absorption imaging is to improve the signal-to-noise ratio (SNR) after the atomic cloud has been produced. Although this particular imaging sequence does not employ online optimization, the routine can easily be extended to a continuously updated model.


.. tip::

    The Read the Docs page for the Machine-Learning Online Optimization Package can be found `here <https://m-loop.readthedocs.io/en/stable/>`_.

.. Download my review paper: :download:`MLOO for Cold-atom Experiments <_static/PDFs/MLOOpaper_RachelWang.pdf>`


See :ref:`competition rules <about-competition>` below.


.. |link_MLOO|

.. .. |link_MLOO| raw:: html

..     <a href="https://spectra.pub/ml/online-optimisation-for-cold-atom-experiments"><h3>Machine-learning online optimization (MLOO) for cold-atom experiments</h3></a>


.. [#foot1] Specifically, I am interested in universality classes in non-equilibrium quantum many-body systems. Read more about my :ref:`research interests <research>`.

.. [Wigley2016] *Paul B Wigley, Patrick J Everitt, Anton van den Hengel, John W Bastian, Mahasen A Sooriyabandara, Gordon D McDonald, Kyle S Hardman, Ciaron D Quinlivan, P Manju, Carlos CN Kuhn, et al. Fast machine-learning online optimization of ultra-cold-atom experiments. Scientific reports, 6(1):1–6, 2016.*

.. [Ness2020] *Gal Ness, Anastasiya Vainbaum, Constantine Shkedrov, Yanay Florshaim, and Yoav Sagi. Single-exposure absorption imaging of ultracold atoms using deep learning. Physical Review Applied, 14(1):014011, 2020.*


|


.. _MLOOpdf:

Machine-learning online optimization (MLOO) for cold-atom experiments
*********************************************************************


    .. note::

      Ideally, documents would be embedded using `Adobe's PDF Embed API <https://www.adobe.io/apis/documentcloud/dcsdk/pdf-embed.html>`_. However, it requires a client ID to use and so this will have to do for the time being.

:pdfembed:`src:_static/PDFs/MLOOpaper_RachelWang.pdf#view=FitH&zoom=100, height:1000, width:100%, align:middle`




|



.. _about-competition:

About the Spectra Competition
*****************************


Mathpix is a tool for extracting text/equations from images and documents, making typing LaTeX documents faster and less tedious. The core technology of `Mathpix Snip <https://mathpix.com/>`_, the consumer app, is a publicly available API `MathpixOCR <https://mathpix.com/ocr>`_ for developers. Recently (March 2021), they announced the Spectra Review Paper Competition with the aim providing a platform, Spectra, presenting ML content to researchers/practitioners in HTML. 


.. _criteria:

Criteria
^^^^^^^^

Here is a brief summary of the competition criteria:

    * The review paper need not be novel/original research.
    * The goal of the paper is to summarize/explain state-of-the-art methods in a particular ML subfield.
    * The target audience are those occupied by ML research and development, who would benefit from a concise summary of novel approaches.
    * Papers must be submitted via PR to the `Spectra Github repo <https://github.com/Mathpix/spectra-review-paper-competition>`_ in Markdown.

Papers were judged with respect to:

    * Depth
    * Accuracy
    * Clarity of writing
    * Good coverage of the topic

add someting different