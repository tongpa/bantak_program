About datacenter
-------------------------

datacenter is a Pluggable application for TurboGears2.

Installing
-------------------------------

datacenter can be installed both from pypi or from bitbucket::

    pip install datacenter

should just work for most of the users

Plugging datacenter
----------------------------

In your application *config/app_cfg.py* import **plug**::

    from tgext.pluggable import plug

Then at the *end of the file* call plug with datacenter::

    plug(base_config, 'datacenter')

You will be able to access the plugged application at
*http://localhost:8080/datacenter*.

Available Hooks
----------------------

datacenter makes available a some hooks which will be
called during some actions to alter the default
behavior of the appplications:

Exposed Partials
----------------------

datacenter exposes a bunch of partials which can be used
to render pieces of the blogging system anywhere in your
application:

Exposed Templates
--------------------

The templates used by registration and that can be replaced with
*tgext.pluggable.replace_template* are:

