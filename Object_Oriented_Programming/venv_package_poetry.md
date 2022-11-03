[# Python Virtual Environments

### Global environments

_By default, any Python interpreter installed runs in its own global environment. They aren't specific to a particular
project._
_Any packages that you install or uninstall affect the global environment and all programs that you run within it._
_Working in the global environment is an easy way to get started. If you install packages in that environment, though,
in time it will become crowded and make it difficult to properly test an application._

### Virtual environments

_To prevent such clutter, developers often create a virtual environment for a project. A virtual environment is a folder
that contains a copy (or symlink) of a specific interpreter._

_Any time you’re working on a Python project that uses external dependencies that you’re installing with pip, it’s best
to first create a virtual environment:_

```
windows:
    python -m venv venv
Linux:
    python3 -m venv venv 
```

+ If you’re using Python on Windows and you haven’t configured the PATH and PATHEXT variables, then you might need to
  provide the full path to your Python executable:

_Now we should activate it. Your project has its own virtual environment. Generally, before you start using it, you’ll
first activate the environment by executing a script that comes with the installation:_

```
windows:
    venv\Scripts\
Linux:
    source venv/bin/activate
```

_Install packages using the pip command:_

```
windows:
    python -m pip install <package-name>
Linux:
    python -m pip install <package-name>
```

_If you are done working in the virtual environment for the moment, you can deactivate it:_

```
windows:
    deactivate
Linux:
    deactivate
```

_The short answer is that Python isn’t great at dependency management. If you’re not specific, then pip will place all
the external packages that you install in a folder called site-packages/ in your base Python installation._

### Virtualenv

_The virtualenv tool is very similar to python -m venv. In fact, the venv module is based on virtualenv. However, using
virtualenv instead of python -m venv has several obvious advantages:_

+ virtualenv is generally faster than python -m venv
+ Tools like pip, setuptools and wheel are often more up to date and cached (hence the performance boost). In virtualenv
  terms, these are seed packages. And yes, you can add other seed packages.

```
pipx install virtualenv
```

### Poetry

_Poetry helps you declare, manage and install dependencies of Python projects, ensuring you have the right stack
everywhere._

#### Interaction with the Poetry virtual environment

_Poetry is for managing projects, so to create a new virtual environment, first create a project directory and enter
it:_

```
poetry new my_project
cd my_project
```

_To activate the virtual environment, do the following:_

```
poetry shell
```

#### Adding packages with Poetry

_Unlike the traditional approach, in Poetry we don't use pip install to install packages. Use poetry add instead_

```
poetry add arrow
```

### Pipenv

_Pipenv is a packaging tool for Python that solves some common problems associated with the typical workflow using pip,
virtualenv, and the good old requirements.txt._
_In addition to addressing some common issues, it consolidates and simplifies the development process to a single
command line tool._

_Installing:_

```
pip install pipenv
```

_Pipenv uses pip and virtualenv under the hood but simplifies their usage with a single command line interface._

_First, spawn a shell in a virtual environment to isolate the development of this app_

```
pipenv shell
```

_This will create a virtual environment if one doesn’t already exist. Pipenv creates all your virtual environments in a
default location._

_Now you can install the 3rd party package you need, flask. Oh, but you know that you need version 0.12.1 and not the
latest version, so go ahead and be specific_

```
pipenv install flask==0.12.1
```

_Okay, so let’s say you’ve got everything working in your local development environment and you’re ready to push it to
production. To do that, you need to lock your environment so you can ensure you have the same one in production:_

```
pipenv lock
```

### Conda

_If you need a large Python installation and all the tools, check out Anaconda. Miniconda provides the conda command
line tool and only the dependencies you need to get started._

# ++++++++++

# Package management

_Pip is the standard Python package manager, making it easy to download and install packages from the PyPI repository._

# ++++++++++

# Poetry

### How to set up poetry

_If you request a list of poetry settings immediately after installation, you will see the following:_

```
cache-dir = "/…/…/.cache/pypoetry"
virtualenvs.create = true
virtualenvs.in-project = null
virtualenvs.path = "{cache-dir}/virtualenvs"  # /home/astynax/.cache/pypoetry/virtualenvs
```

_Let's create a poetry project with the command poetry new NAME._

```
poetry new Name

Created package Name in Name

cd Name  # Переходим в созданную директорию
tree .

.
├── Name
│   └── __init__.py
├── myprojekt.toml
├── README.md
└── tests
    └── __init__.py
```

_The most important file in a poetry project is pyproject.toml. This is the project configuration file. It describes
what poetry needs to know in order to:_

+ manage project dependencies

+ run code for execution

+ launch development tools

+ build a distribution and publish it on PyPI

_By working with poetry, you are getting used to the fact that you will publish the project. Each package must have a
description and a proper structure, and a version is assigned to it. This should always be done, even if you are not
going to publish the project to the index._

