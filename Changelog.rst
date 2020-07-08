Changelog
=========

1.8.0
-----
- Removed Python 2.7 support.
- Added support for Python 3.8, Django 2.2 and 3.0

1.7.5
-----
- Support translated strings in settings (merwok).
- Set TinyMCE localization language when rendering the widget instead of the
  widget class initialization (allows to set TinyMCE language depending on
  the web page locale).

1.7.4
-----
- Upgraded TinyMCE to v.4.9.2

1.7.3
-----
- Upgraded TinyMCE to v.4.8.3

1.7.2
-----
- Upgraded TinyMCE to v.4.8.0.
- Various fixes (maqmigh, ojiii, rvanlaar).

1.7.1
-----
- Upgraded TinyMCE to v.4.7.11

1.7.0
-----
- Upgraded TinyMCE to v.4.7.4
- Fixed using TinyMCE in non-admin forms.
- Fixed compatibility with ``django-filebrowser-no-grapelli``.
  This broke compatibility with ``django-filebrowser``
  (based on grapelli) until the latter adds support for TinyMCE 4.

1.6.0
-----
- Upgraded TinyMCE to v.4.7.2.
- Added compatibility with Django 2.0 (thomwiggers).
- Fixed dropped widget attributes in Django => 1.11 (bentrm).
- Fixed missing Changelog in ``sdist`` .gz distribution.

1.5.2
-----
- Fixed rendering TinyMCE widgets with multiple inline formsets in Django admin
  (se-bastiaan).
- Fixed running Django management commands with ``ManifestStaticFilesStorage`` and
  ``DEBUG = False`` (hopefully).
- Upgraded TinyMCE to v.4.6.7.

1.5.1
-----
- Fixed running collectstatic command with ``ManifestStaticFilesStorage`` and
  ``DEBUG = False``.

1.5.0
-----
- **Security**: protected spellchecker REST endpoint from CRSF.
- Implemented correct handling of TinyMCE widgets inside inline formsets
  in Django admin interface.
- Upgraded TinyMCE to v.4.6.6.

1.4.2
-----
- Upgraded TinyMCE to v.4.6.4.
- Fixed the default editor config.

1.4.1
-----
- Upgraded TinyMCE to v.4.6.2.
- Added text format selector to the default editor configuration.

1.4.0
-----
- Upgraded TinyMCE to v.4.6.0.

1.3.2
-----
- Fixed compatibility with Django v.1.11.

1.3.1
-----
- Upgraded TinyMCE to v.4.5.5.
- Fixed language file configuration for languages with country codes (Gagaro).
- Rendering of the TinyMCE 4 is now tested with Selenium/PhantomJS.

1.3.0
-----
- Upgraded TinyMCE to v.4.5.1.

1.2.0
-----
- Upgraded TinyMCE to v.4.4.3
- Added ``TINYMCE_ADDITIONAL_JS_URLS`` configuration option.

1.1.0
-----
- Upgraded TinyMCE to v.4.4.1.
- Added Django 1.10 to compatibility matrix.

1.0.0
-----
- Initial PyPI release.
