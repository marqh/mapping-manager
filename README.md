mapping-manager
===============

PLEASE NOTE: This is pre-alpha software and is in a continuous state of flux. Please do not rely on it for anything.

Things you need to do before running the application:

Application Dependencies
------------------------

This application depends on metOcean-mapping.  

1) The Python modules in metOcean-mapping need to be installed (see setup.py)

2) metOcean-mapping's fuseki server needs to be running, providing a SPARQL endpoint


Application SetUp
-----------------

1) create a python file called 'settings_local.py', which will be imported in to
the Django startup 'settings.py' file upon launch.

2) In 'settings_local.py' overide the TEMPLATE_DIRS variable with the 
absolute path to the applications template directory:
    TEMPLATE_DIRS = ('<absolute path to this app>/manager/templates',)

3) Ensure that the fusekiQuery and metocean modules from the metOcean-mapping project are available.
