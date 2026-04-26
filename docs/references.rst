References
==========

This page collects the canonical bibliography of the Extended Matrix
language: the foundation paper, the per-version flag papers, and the
extended literature in which EM has been applied, refined or compared
with other approaches.

.. note::

   For **citation guidance** — i.e. *which* of these papers you should
   cite when you write up a project that uses EM — see the
   `How to cite EM <https://www.extendedmatrix.org/cite/>`__ page on the
   project website. The cumulative rule (always cite the foundation
   paper, then add the flag paper of the version you used) is described
   there with ready-made BibTeX entries.

Foundation paper
----------------

.. admonition:: Always cite this paper
   :class: tip

   Demetrescu, E. (2015). *Archaeological stratigraphy as a formal
   language for virtual reconstruction. Theory and practice.*
   **Journal of Archaeological Science**, 57, 42–55.
   `DOI 10.1016/j.jas.2015.02.004 <https://doi.org/10.1016/j.jas.2015.02.004>`__.

   This is the **methodological foundation** of Extended Matrix. Every
   subsequent release builds on the formal language introduced here, so
   it must be cited in any academic work that uses EM, regardless of
   which specific version was actually used to author the project.

Flag papers per EM version
--------------------------

When you cite EM in a paper, *additionally* cite the flag paper of the
release you actually used (or the closest one in feature scope). The
list below grows as new releases are published.

EM 1.4 — Long-Term Support
~~~~~~~~~~~~~~~~~~~~~~~~~~

Demetrescu, E., Ferdani, D. (2021). *From Field Archaeology to Virtual
Reconstruction: A Five Steps Method Using the Extended Matrix.*
**Applied Sciences**, 11(11), 5206.
`DOI 10.3390/app11115206 <https://doi.org/10.3390/app11115206>`__.

EM 1.0–1.3
~~~~~~~~~~

Versions 1.0 to 1.3 are no longer separately downloadable, but the
features they introduced live on inside the latest EM core. When citing
projects authored under those versions, fall back to the foundation
paper (1.0) plus the closest available flag paper.

.. note::

   **Editors:** add the canonical flag paper for EM 1.1, 1.2 and 1.3
   here, with full citation and DOI, when the relevant references are
   confirmed.

EM 1.5 — Development
~~~~~~~~~~~~~~~~~~~~

The 1.5 development line does not yet have an associated flag paper.
Until then, citations of features that originate in 1.5 (TSU, Landscape
mode, CronoFilter, …) should fall back to the 1.0 foundation plus the
1.4 LTS flag paper, with a contextual note in the methods section
indicating that the development line was used.

Software citation
-----------------

Cite the software components only when you actually used them
(e.g., EM Tools for the Blender pipeline, Heriverse for the web
publication). Software citations complement — not replace — the
methodological citations above.

.. code-block:: bibtex

   @misc{demetrescu_extendedmatrix,
     title     = {Extended Matrix},
     author    = {Demetrescu, Emanuel},
     publisher = {Zenodo},
     doi       = {10.5281/zenodo.5957132},
     url       = {https://doi.org/10.5281/zenodo.5957132}
   }

Each component (EM Tools, Heriverse, 3DSC, s3dgraphy) has its own
Zenodo DOI on the
`Extended Matrix Zenodo community <https://zenodo.org/communities/extendedmatrix>`__.
Pick the version DOI that matches what you actually used.

Selected applications and case studies
--------------------------------------

A non-exhaustive selection of peer-reviewed work in which EM has been
applied, evaluated or extended. The corresponding case studies are
collected on the
`projects page <https://www.extendedmatrix.org/projects>`__ of the
project website.

* Berto S., Demetrescu E., Fanini B., Bonetto J., Salemi G. (2021).
  *Analysis and Validation of the 3D Reconstructive Process through
  the Extended Matrix Framework of the Temple of the Roman Forum of
  Nora (Sardinia, CA).* **Environmental Sciences Proceedings** 10, 1: 18.
  `DOI 10.3390/environsciproc2021010018 <https://doi.org/10.3390/environsciproc2021010018>`__.

* Daniele F., Demetrescu E., Cavalieri M., Pace G., Lenzi S. (2019).
  *3D Modelling and Visualization in Field Archaeology. From Survey to
  Interpretation of the Past Using Digital Technologies.*
  **Groma 4**.
  `DOI 10.12977/groma26 <http://dx.doi.org/10.12977/groma26>`__.

* Ferdani D., Fanini B., Piccioli M. C., Carboni F., Vigliarolo P. (2020).
  *3D reconstruction and validation of historical background for
  immersive VR applications and games: The case study of the Forum of
  Augustus in Rome.* **Journal of Cultural Heritage**.
  `DOI 10.1016/j.culher.2019.12.004 <http://dx.doi.org/10.1016/j.culher.2019.12.004>`__.

* Pietroni E., Menconero S., Botti C., Ghedini F. (2023).
  *e-Archeo: A Pilot National Project to Valorize Italian
  Archaeological Parks through Digital and Virtual Reality
  Technologies.* **Applied System Innovation** 6, 38.
  `DOI 10.3390/asi6020038 <https://doi.org/10.3390/asi6020038>`__.

.. note::

   **Editors:** this list is intentionally curated and partial. Open a
   PR to add a paper that uses EM as a method, applies one of the
   software components, or extends the formal language.
