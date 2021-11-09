
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


===========  ==================================================================
 |step1|     `enter the asked credentials`.

 |step2|     Enter a directory name (for instance **pibooth**) and click on.
===========  ==================================================================

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

.. --- Tuto -------------------------------------------------------------------

.. |step1| image:: https://github.com/pibooth/pibooth-google-photo/blob/master/docs/images/step1_shortcut_button.png?raw=true
   :width: 80 %
   :alt: step1_shortcut_button

.. |step2| image:: https://github.com/pibooth/pibooth-google-photo/blob/master/docs/images/step2_project_name.png?raw=true
   :width: 80 %
   :alt: step2_project_name

.. |step3| image:: https://github.com/pibooth/pibooth-google-photo/blob/master/docs/images/step3_display_name.png?raw=true
   :width: 80 %
   :alt: step3_display_name

.. |step4| image:: https://github.com/pibooth/pibooth-google-photo/blob/master/docs/images/step4_app_type.png?raw=true
   :width: 80 %
   :alt: step4_app_type

.. |step5| image:: https://github.com/pibooth/pibooth-google-photo/blob/master/docs/images/step5_download.png?raw=true
   :width: 80 %
   :alt: step5_download
