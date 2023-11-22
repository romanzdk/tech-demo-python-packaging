<sub>November 2023</sub>
> **NOTE**: The code in this repository and its documentation is still work in
> progress but will be completed soon.

# Python Packaging - A technical demonstration

The purpose of this repository is to illustrate the packaging of Python
projects. As examples this repository contain multiple projects in different
flavours.

The examples try to follow the current state of the art and official
recommendations (e.g. using a `pyproject.toml` and use _Development Mode_ via
`--editable` option). More details can be found in the sub folders.

## TOC

- [Overview](#overview)
- [Demo 01 - Simple terminal application](#demo-01-simple-terminal-application)
  - [About Python Packaging](#about-python-packaging)
  - [About the folder structure and the "src layout"](#about-the-folder-structure-and-the-src-layout)
  - [Development Mode / Editabel installs](#development-mode-editabel-installs)
- [Demo 02 - Simple GUI application](#demo-02-simple-gui-application)
- [Demo 03 - Internationalization (i18n) and localization (l10n) using GNU gettext](#demo-03-internationalization-i18n-and-localization-l10n-using-gnu-gettext)
  - [Demo 03 variant "setuptools"](#demo-03-variant-setuptools)
  - [Demo 03 variant "hatch"](#demo-03-variant-hatch)
- [Demo 04 - Start application "as root"](#demo-04-start-application-as-root)
- [Demo 05 - Multiple import packages](#demo-05-multiple-import-packages)
- [Eliminate redundant package information and centralize all meta data](#eliminate-redundant-package-information-and-centralize-all-meta-data)
- [Real world examples](#real-world-examples)
- [Further reading and official sources about Python Packaging](#further-reading-and-official-sources-about-python-packaging)

# Overview
Each of the sub folders is one example and could be treated as a repository of its own.

 - `01a_terminal_helloworld_setuptools` - Simplest packaging and installing demo just print "Hello World" on standard output (usually the terminal).
 - `01b_terminal_helloworld_hatch` - Similar to the previous example
   `01a_terminal_helloworld_setuptools` but using
   `hatch` as build backend.
 - `02_gui_helloworld` - Introduce the use of dependencies using a GUI to print "Hello World" in a window.
 - `03a_i18n_setuptools` - Using GNU gettext to introduce translation of strings.
 - `03b_i18n_hatch` - Similar to the previous example `03a_i18n_setuptools`
   but using `hatch` as build backend.
 - `04_user_and_as_root` - Run the application as regular user and "as root".
 - `05_two_import_packages` - Offer a command line and graphical interface to
   demonstrate two Import Packages in one Distripution package.

Please feel free to open issues.

# Demo 01 - Simple terminal application

The project in the sub-folder [`01_terminal_helloworld`](01_terminal_helloworld) starts as simpelst application possible just printing `Hello World` to the terminal.
The following concepts are illustrated:

 - Python Package configuration via `pyproject.toml` ([PEP 621](https://peps.python.org/pep-0621))
 - Elimination of redundancies in project meta data (e.g. version string, dependencies) through centralization into `pyproject.toml`.
 - Use of the ["src layout"](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/).
 - Use of `__init__.py` and `__main__.py`.
 - Installing the package in [Development Mode](https://setuptools.pypa.io/en/latest/userguide/development_mode.html) also known as _editable installation_ to avoid manipulation of `sys.path` and other `import` hacks.
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
often manipulated to fulfil the developers needs. Today is no need anymore
for risky and unstable hacks like this.

The solution is the [Development Mode](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/#working-in-development-mode)
also known as [editable install](https://pip-python3.readthedocs.io/en/latest/reference/pip_install.html#editable-installs)
([PEP660](https://peps.python.org/pep-0660/)).
The package in development is kind of *installed*. The Python interpreter see
the package as it was installed. But because of symlinks used in that special
mode the source files in the git repository are used. This also means that each
modification on the source has an immediate effect on the package available to
the system. To install a package in _Development Mode_ `pip`'s option `-e` or `--editable` is used.

[[terminal_helloworld.gif]]

# Demo 02 - Simple GUI application

The second demo extends the previous [Demo 01]((#demo-01-simple-terminal-appliation). The string `Hello World!` now is shon in a GUI window. The handling of dependencies in the Python Packaging process will be illustrated.

The GUI package [`PySimpleGUI`](https://www.pysimplegui.org) is used to create the window. The key difference to the previous demo is the use of the `dependencies` variable in the `pyproject.toml` file.

    [project]
    name = "helloworld-gui"

    # ...

    dependencies = [
	"PySimpleGUI",
    ]

    # ...

This results in installing depending packages in the back while installing the demo via `pip`.

[[gui_helloworld.gif]]

# Demo 03 - Internationalization (i18n) and localization (l10n) using GNU gettext

The third demo extends the previous [Demo 02](#demo-02-simple-gui-appliation). The [GNU gettext](https://www.gnu.org/software/gettext) localization framework is used to translate the string `Hello World!`. The translation itself is not the topic of this demo but the handling of the translational files is.

Two variants of this demo exists. One do use the usual `setuptools` as build-backend and the second do use [`hatch`](https://hatch.pypa.io). The latter is used because it offers a more elegant, pythonic and easier to understand solution.

## Demo 03 variant "setuptools"

> **NOTE**:
> Handle this example with care. It might not be the best solution nor it is
> pythonic. Feel free to open an Issue to provide an easier and better
> example.

A custom build step is used to compile the `po`-files using `msgfmt` into
`mo`-files. The `mo` files are included as `package-data` files while
installing.

There is a new folder `po` in the project containing two `po` and one `pot`
file. 

    03_i18n_setuptools
	|-- README.md
	|-- pyproject.toml
	|-- setup.py
	`-- src
		`-- helloworld-int
            |-- __init__.py
            |-- __main__.py
            `-- po
                |-- de.po
                |-- jp.po
                `-- messages.pot

The `pyproject.toml` do define `package-data`. While installing the
build-backend `setuptools` will look for a folder `locales` and its content
defined by the search pattern used here.

	[tool.setuptools.package-data]
	helloworldint = [
		'locales/*/LC_MESSAGES/*.mo',
	]

This folder do not exist yet. There is a custom build step defined via
`setup.py` file. This step will compile the `po` into `mo` files and place
them in the right place inside the projects source directory (not the install
directory!). See the `setup.py` for details.

## Demo 03 variant "hatch"

# Demo 04 - Start application "as root"
> **ATTENTION**:
> In its current state this technical demo do not work and need assistance.
> The issues are described in more details below.

> **WARNING**:
> This demo propagates to install it using `sudo -H`. This is prohibited
> because of [security reasons](https://askubuntu.com/a/802594/416969).
> The author is open for alternative solutions.

Install via `sudo --set-home python3 -m pip install .`.

# Demo 05 - Multiple import packages

# Eliminate redundant package information and centralize all meta data

# Real world examples
 - [Hyperorg](https://codeberg.org/buhtz/hyperorg) as a command line application.
 - [Buhtzology](https://codeberg.org/buhtz/buhtzology) as a Python library.

# Further reading and official sources about Python Packaging
 - [Python Packaging User Guide](https://packaging.python.org) especially in there
   - the [section about the project layout](https://packaging.python.org/en/latest/tutorials/packaging-projects/) using a `src` folder
   - and the discussion [src layout vs flat layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout)
   - and [the Packaing tutorial](https://packaging.python.org/en/latest/tutorials/packaging-projects).
 - [Configuring setuptools using `pyproject.toml`](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html)
 - [PEP 621 - Storing project metadata in `pyproject.tom`](https://peps.python.org/pep-0621)
 - [The basics of Python packaging in early 2023](https://drivendata.co/blog/python-packaging-2023)
 - [Python packages with pyproject.toml and nothing else](https://til.simonwillison.net/python/pyproject)
 - [Answer to "Is `sudo pip install` still a broken practice?" at AskUbuntu.com](https://askubuntu.com/a/802594/416969)
 
<sub>November 2023</sub>

