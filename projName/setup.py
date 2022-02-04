# setup.py

# This file and its subfolder create a custom Python package for use in the project.
# Your custom variables, configurations & functions are defined in the 'projName'
# subfolder. setup.py then stitches these together into a package that can be called.

# The custom package is a very useful tool for large projects, or projects where you
# are working with other developers. Not only does it centralise your management of
# custom code, but it creates a package that can potentially be deployed to our
# production environment and used by any BAR Python developer (like pandas).

# If you are working on a small project, you may find it simpler to replace
# everything in this folder with a single 'custom.py' script under 'notebooks/'.

from setuptools import setup, find_packages

setup(name="projName"
        ,version="0.1"
        ,description="Project Description"
        ,author="Stafflink#"
        ,author_email="youremail@health.nsw.gov.au")