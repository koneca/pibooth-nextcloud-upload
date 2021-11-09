
====================
pibooth-nextcloud-upload
====================

|PythonVersions| |PypiPackage| |Downloads|

``pibooth-nextcloud-upload`` is a plugin for the `pibooth`_ application.

Its permits to upload the pictures to a Nextcloud`_ instance. It requires an
internet connection.

Install
-------

::

    $ pip3 install pibooth-nextcloud-upload

Configuration
-------------

Here below the new configuration options available in the `pibooth`_ configuration.
**The keys and their default values are automatically added to your configuration after first** `pibooth`_ **restart.**

.. code-block:: ini

    [NEXTCLOUD]

    # Directory where pictures are uploaded
    directory_name = Pibooth

    # user Credentials. ( 'user', 'password' )
    client_credentials =

    # Servername 'cloud.example.com'
    server_name =

.. note:: Edit the configuration by running the command ``pibooth --config``.

Grant secured access
--------------------

Access to a Nextcloud directory is granted by a **the credentials** that shall
be defined in the ``[NEXTCLOUD][client_credentials]``. With the directory name the path in the nextcloud instance can be choosen.
Please change the server_name to yours.

.. --- Links ------------------------------------------------------------------

.. _`pibooth`: https://pypi.org/project/pibooth

.. _`Nextcloud`: https://nextcloud.com

.. |PythonVersions| image:: https://img.shields.io/badge/python-3.6+-red.svg
   :target: https://www.python.org/downloads
   :alt: Python 3.6+

.. |PypiPackage| image:: https://badge.fury.io/py/pibooth-google-photo.svg
   :target: https://pypi.org/project/pibooth-google-photo
   :alt: PyPi package

.. |Downloads| image:: https://img.shields.io/pypi/dm/pibooth-nextcloud-upload?color=purple
   :target: https://pypi.org/project/pibooth-nextcloud-upload
   :alt: PyPi downloads
