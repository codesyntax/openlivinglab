Use this django project template to easily setup a openlivinlab.com like site

USAGE
=====

You have to use pip to install this templates. Virtualenv is highly recomended.

.. code-block:: console

pip install -r https://raw.githubusercontent.com/codesyntax/openlivinglab/1.7.X/requirements.txt

Once installed crete a django project based on this template

.. code-block:: console

django-admin.py startproject -v2 --template=https://github.com/codesyntax/openlivinglab/archive/1.7.X.zip mysite

Run migrations

.. code-block:: consolo

python mysite/manage.py migrate

Run server

python mysite/manage.py runserver

** You have to chenge settings.DEBUG or settings.ALLOWED_HOSTS to run server correctly


