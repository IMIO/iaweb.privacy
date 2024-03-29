# -*- coding: utf-8 -*-
"""Installer for the iaweb.privacy package."""

from setuptools import find_packages
from setuptools import setup


long_description = "\n\n".join(
    [
        open("README.rst").read(),
        open("CONTRIBUTORS.rst").read(),
        open("CHANGES.rst").read(),
    ]
)


setup(
    name="iaweb.privacy",
    version="1.0a3.dev0",
    description="Privacy rules for IMIO web projects",
    long_description=long_description,
    # Get more from https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="Python Plone",
    author="Martin Peeters",
    author_email="support@imio.be",
    url="https://pypi.python.org/pypi/iaweb.privacy",
    license="GPL version 2",
    packages=find_packages("src", exclude=["ez_setup"]),
    namespace_packages=["iaweb"],
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "Products.GenericSetup",
        "collective.privacy",
        "plone.api",
        "setuptools",
        "z3c.jbot",
    ],
    extras_require={
        "test": [
            "plone.app.robotframework",
            "plone.app.testing",
            "plone.testing",
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    [console_scripts]
    update_locale = iaweb.privacy.locales.update:update_locale
    """,
)
