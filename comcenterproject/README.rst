About project
-------------------------

project is a Pluggable application for TurboGears2.

Installing
-------------------------------

project can be installed both from pypi or from bitbucket::

    pip install project

should just work for most of the users

Plugging project
----------------------------

In your application *config/app_cfg.py* import **plug**::

    from tgext.pluggable import plug

Then at the *end of the file* call plug with project::

    plug(base_config, 'project')

You will be able to access the plugged application at
*http://localhost:8080/project*.

Available Hooks
----------------------

project makes available a some hooks which will be
called during some actions to alter the default
behavior of the appplications:

Exposed Partials
----------------------

project exposes a bunch of partials which can be used
to render pieces of the blogging system anywhere in your
application:

Exposed Templates
--------------------

The templates used by registration and that can be replaced with
*tgext.pluggable.replace_template* are:

