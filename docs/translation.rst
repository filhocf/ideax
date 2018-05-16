Translating Idea\ :sup:`X`
==========================

After installed your development environment and loaded your virtualenv, add the desired language, running the following command (using spanish "es" as example):

.. code::

    $ ./manage.py makemessages -l es

It will create a directory /locale/es/LC_MESSAGES/django.po. Translate this file with a text editor or a PO editor, like POEdit, or other localization software tool. Translated strings will be writted in msgstr fields.

After, add your language in settings.py file.

.. code::

    LANGUAGE_CODE = 'es'
    ...
    LANGUAGES = (
      ('en', u'English'),
      ('pt-br', u'Português'),
      ('es', u'Español')
    )
