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

2) copy the DATABASES dictionary from 'settings.py' into 'settings_local.py' e.g.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',# Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

3) In 'settings_local.py', override the following two variables:
    DATABASES['default']['ENGINE'] = "django.db.backends.sqlite3"
    DATABASES['default']['NAME'] = '<absolute path to your SQLite3 db>'

If you are not using SQLite3, please consult the Django documentation for
details of other supported databases.

4) In 'settings_local.py' overide the TEMPLATE_DIRS variable with the 
absolute path to the applications template directory:
    TEMPLATE_DIRS = ('<absolute path to this app>/manager/templates',)

5) run 'python ./manage.py syncdb' to create and populate your Django database
