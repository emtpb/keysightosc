*********
Changelog
*********

This project follows the guidelines of `Keep a changelog`_ and adheres to
`Semantic versioning`_.

.. _Keep a changelog: http://keepachangelog.com/
.. _Semantic versioning: https://semver.org/


`0.2.0`_ - 2026-11-04
=====================

Fixed
-----
* Minor documentation issues
* Prevent device detection from failing if there are resource names which do
  not match the previously assumed scheme of more than three parts divided by
  ``::``.

Changed
-------
* **Breaking:** Change init argument ``resource`` to only accept full visa
  resource names. Use the new keyword argument ``serial_number`` to initialize
  a generator by its serial number.
* Replace setup.py by pyproject.toml


`0.1.3`_ - 2025-10-30
=====================

Fixed
-----
* Missing read and write termination


`0.1.2`_ - 2024-11-13
=====================

Added
-----
* Support for DSOX1202A


`0.1.1`_ - 2024-09-24
=====================

Added
-----
* Support for DSOX2004A
* General support for 4-channel oscilloscopes


`0.1.0`_ - 2022-12-01
=====================

Added
-----
* First preview release.


.. _Unreleased: https://github.com/emtpb/keysightosc
.. _0.2.0: https://github.com/emtpb/keysightosc/releases/tag/0.2.0
.. _0.1.3: https://github.com/emtpb/keysightosc/releases/tag/0.1.3
.. _0.1.2: https://github.com/emtpb/keysightosc/releases/tag/0.1.2
.. _0.1.1: https://github.com/emtpb/keysightosc/releases/tag/0.1.1
.. _0.1.0: https://github.com/emtpb/keysightosc/releases/tag/0.1.0
