About computer
-------------------------

computer is a Pluggable application for TurboGears2.

Installing
-------------------------------

computer can be installed both from pypi or from bitbucket::

    pip install computer

should just work for most of the users

Plugging computer
----------------------------

In your application *config/app_cfg.py* import **plug**::

    from tgext.pluggable import plug

Then at the *end of the file* call plug with computer::

    plug(base_config, 'computer')

You will be able to access the plugged application at
*http://localhost:8080/computer*.

Available Hooks
----------------------

computer makes available a some hooks which will be
called during some actions to alter the default
behavior of the appplications:

Exposed Partials
----------------------

computer exposes a bunch of partials which can be used
to render pieces of the blogging system anywhere in your
application:

Exposed Templates
--------------------

The templates used by registration and that can be replaced with
*tgext.pluggable.replace_template* are:

