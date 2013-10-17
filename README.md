# flicker

Flicker adds some logging utilities that improve on Django's defaults.

# Developer setup

## Very first time

This setup assumes you have `virtualenv` installed on your system, have just cloned the git repo, and
are in the directory with this `README.md`.

    $ virtualenv ve --python=python2.7 --prompt="(flicker)"                             # Get a set of eggs just for this
    $ . ve/bin/activate                                                                 # Turn on the virtualenv
    $ python setup.py develop --always-unzip                                            # Fill the virtualenv with Python dependencies

Before you write any code, make sure you can run the tests and get them to pass 100%.

### Every time

When you come back to work after a day or more, you'll need to update your git checkout
and make sure you have any new dependencies or schema modifications:

    $ . ve/bin/activate                                               # Turn on the virtualenv (Every time!)
    $ python setup.py develop --always-unzip                          # Update the virtualenv with new Python dependencies

### Git Hooks

Optionally, if you would like all the post-pull stuff to happen automatically each time you do a git pull, you can install git hooks. From the project root, simply run:

    $ git-hooks/install-hooks

This will install (and keep up to date) some scripts in the .git directory that will automatically update your python packages, delete .pyc files, etc.

## Tests

The tests for this project are managed by `tox`, a Python package.
First, install tox via `easy_install`.

    $ easy_install tox # or use pip if you prefer

To run the tests: 

    $ tox

The first run will take a while as it builds a virtualenv and installs everything in it, subsequent ones will be much faster.
To rebuild the virtualenv later with updated dependencies:

    $ tox -r

You normally shouldn't need to recreate the tox virtualenv, since it updates itself on each run,
but it might be necessary in cases of version conflicts.
