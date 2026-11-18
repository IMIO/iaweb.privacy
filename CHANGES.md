# Changelog

<!-- towncrier release notes start -->

## 2.0.0 (unreleased)


- Breaking: replace the `pkg_resources` namespace of `iaweb` with a PEP 420
  native namespace. Support Plone 6.1 only on Python 3.10 to 3.13, and Plone
  6.2 on Python 3.10 to 3.14. Use 1.0a2 for older Plone versions.
  [remdub]

- Import `INonInstallable` from `plone.base` instead of the alias Plone 6.2
  deprecates, and port the setup tests from `portal_quickinstaller` to
  `get_installer`.
  [remdub]

- Include the CMFCore permissions in `configure.zcml`, so the package also
  loads when it is included before Plone (`zcml_package_includes`).
  [remdub]

- Fix `rules/all.zcml`, which included a nonexistent `medial.zcml`.
  [remdub]

- Configure the package with plone.meta 2.12.0 (test matrix on Plone 6.2.3
  and 6.1), move its metadata to `pyproject.toml`, convert the documentation
  to Markdown and run the development environment on Plone 6.2.3 with uv
  instead of buildout. Drop the broken `update_locale` console script.
  [remdub]


## 1.0a2 (2022-01-19)


- SUP-21477: Change default cookies texts
  [laulaz]


## 1.0a1 (2021-12-13)


- Initial release.
  [mpeeters]
