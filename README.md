# Python Packaing - A technical demonstration

The purpose of this repository is to illustrate the packaging of Python
projects. As examples this repository contain multiple projects in different
flavours.

The examples try to follow the current state of the art and official
recommendations (e.g. using a `pyproject.toml` and use _Development Mode_ via
`--editable` option). More details can be found in the sub folders.

## TOC

- [Overview](#overview)
- [Demo 01 - Simple terminal appliation](#demo-01---simple-terminal-appliation)
  - [About Python Packaging](#about-python-packaging)
  - [About the folder structure and the "src layout"](#about-the-folder-structure-and-the-src-layout)
  - [Development Mode / Editabel installs](#development-mode--editabel-installs)
- [Demo 02 - Simple GUI application](#demo-02---simple-gui-application)
- [Demo 03 - Internationalization (i18n) and localization (l10n) using GNU gettext](#demo-03---internationalization-i18n-and-localization-l10n-using-gnu-gettext)
- [Demo 04 - Start application "as root"](#demo-04---start-application-as-root)
- [Demo 05 - Multiple import packages](#demo-05---multiple-import-packages)
- [Eliminate redundant package informaton and centralize all meta data](#eliminate-redundant-package-informaton-and-centralize-all-meta-data)
- [Real world examples](#real-world-examples)
- [Further reading and official sources about Python Packaging](#further-reading-and-official-sources-about-python-packaging)

# Overview
Each one of the sub folders is one example can could be treated as a
respository of its own.

 - `01_terminal_helloworld` - Simplest packaging and installing demo just print "Hello World" on standard output (usually the terminal).
 - `02_gui_helloworld` - Introduce the use of dependencies using a GUI to print "Hello World" in a window.
 - `03_i18n_helloworld` - Using GNU gettext to introduce translation of strings.
 - `04_user_and_as_root` - Run the application as regular user and "as root".
 - `05_two_import_packages` - Offer a command line and graphical interface to demonstrate two Import Packages in one Distripution package.

Please feel free to open issues.

# Demo 01 - Simple terminal appliation

The project in the sub-folder [`01_terminal_helloworld`](01_terminal_helloworld) starts as simpelst application possible just printing `Hello World` to the terminal.
The following concepts are illustrated:

 - Python Package configuration via `pyproject.toml`.
 - Elimination of redundancies in project meta data (e.g. version string, dependencies) through centralization.
 - Use the ["src layout"](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/) combined with [Development Mode](https://setuptools.pypa.io/en/latest/userguide/development_mode.html) also known as _editable installation_ to avoid manipulation of `sys.path` and other `import` hacks.
 - Use of `__init__.py` and `__main__.py`.
 - Installing the package in _Developer Mode_ (aka "as editable").
 - Run tests and the application itself.

Please see the comments in the files themself for detailed explanations.

## About Python Packaging

How to tie up a Python package is easy but the topic itself is not. The latter is because since Python was born in 1991 and while it's ongoing evolution multiple packaging systems has been created. Keep this in mind when looking around for alternative documentation and tutorials and look on their dates because they might be outdated.

## About the folder structure and the "src layout"

This is the so called [src layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/).

    01_terminal_helloworld
    ├── LICENSE
    ├── pyproject.toml
    ├── README.md
    ├── src
    │   └── helloworld-cli
    │       ├── __init__.py
    │       └── __main__.py
    └── tests
	└── test_dummy.py

The difference between _Distribution Packages_ and _Import Packages_ and the consequences in naming them are described in a later demo.

## Development Mode / Editabel installs

While developing and testing a python project (not recommended!) constructs like this are often used.

    # Don't do this at home!!!
    import unittest
    import sys

    sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

    import mypackage
	
The environment variable [`PYTHONPATH` and
`sys.path`](https://docs.python.org/3/library/sys.html#sys.path) do define
where the python interpreter looks for new modules. That variable was and is
often manipulated to fullfill the developers needs. Today is no need anymore
for risky and unstable hacks like this.

The solution is the [Development Mode](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/#working-in-development-mode)
also known as [editable install](https://pip-python3.readthedocs.io/en/latest/reference/pip_install.html#editable-installs)
([PEP660](https://peps.python.org/pep-0660/)).
The package in development is kind of *installed*. The Python interpreter see
the package as it was installed. But because of symlinks used in that special
mode the source files in the git repository are used. This also means that each
modification on the source has an immediate effect on the package avilable to
the system. To install a package in _Development Mode_ `pip`'s option `-e` or `--editable` is used.

[[01_terminal_helloworld.gif]]

# Demo 02 - Simple GUI application

[[02_gui_helloworld.gif]]

# Demo 03 - Internationalization (i18n) and localization (l10n) using GNU gettext

# Demo 04 - Start application "as root"

# Demo 05 - Multiple import packages

# Eliminate redundant package informaton and centralize all meta data

# Real world examples
 - [Hyperorg](https://codeberg.org/buhtz/hyperorg) as a command line application.
 - [Buhtzology](https://codeberg.org/buhtz/buhtzology) as a Python library.

# Further reading and official sources about Python Packaging
 - [Python Packaging User Guide](https://packaging.python.org) especially its [section about the project layout](https://packaging.python.org/en/latest/tutorials/packaging-projects/) using a `src` folder and the discussion [src layout vs flat layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout).
 - [Configuring setuptools using `pyproject.toml`](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html)
 - [PEP 621 - Storing project metadata in `pyproject.tom`](https://peps.python.org/pep-0621)
 - 
 
<sub>November 2023</sub>

