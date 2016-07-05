FAQ
===============

How do I get a devId and authKey?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you do not already have a developer ID and API key, you can obtain one by filling out `this form <https://fs12.formsite.com/HiRez/form48/secure_index.html>`_. Hi-Rez Studios usually responds within a few days.

Why am I getting a null dataset for a player that exists?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If a player has Hide My Profile enabled in-game, methods will return a null dataset.

When using methods such as :meth:`SmiteClient.get_match`, some player info is missing. Why?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If a player has Hide My Profile enabled in-game, some of their data will be unavailable for match history etc.

Does this library support older versions of Python?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No. smite-python only supports Python 3.5 or higher. However, if you are using Python 3.4, you can use `smython <https://github.com/RichardJTorres/smython>`_, though it may be outdated. It does not contain all possible API calls, and doesn't support the console endpoints.

Do all methods work with all endpoints?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No. PC is the only endpoint guaranteed to work with all methods.