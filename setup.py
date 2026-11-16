# -*- coding: utf-8 -*-
"""Installer for the iaweb.privacy package."""

from setuptools import setup


long_description = "\n\n".join(
    [
        open("README.md").read(),
        open("CONTRIBUTORS.md").read(),
        open("CHANGES.md").read(),
    ]
)


setup(
    name="iaweb.privacy",
    version="2.0.0.dev0",
    description="Privacy rules for IMIO web projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # Get more from https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 6.1",
        "Framework :: Plone :: 6.2",
        "Framework :: Plone :: Addon",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="Python Plone",
    author="Martin Peeters",
    author_email="support@imio.be",
    url="https://pypi.python.org/pypi/iaweb.privacy",
    license="GPL version 2",
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.10",
    install_requires=[
        "Products.GenericSetup",
        "collective.privacy",
        "plone.api",
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
