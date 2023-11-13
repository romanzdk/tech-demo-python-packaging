# Python Packaing - A technical demonstration

The purpose of this repository is to illustrate the packaging of Python
projects. As examples this repository contain multiple projects in different
flavours.

The examples try to follow the current state of the art and official
recommendations (e.g. using a `pyproject.toml` and use _Development Mode_ via
`--editable` option). More details can be found in the sub folders.

# Overview
Each one of the sub folders is one example can could be treated as a
respository of its own.

 - `01_terminal_helloworld` - Simplest packaging and installing demo just print "Hello World" on standard output (usually the terminal).
 - `02_gui_helloworld` - Introduce the use of dependencies using a GUI to print "Hello World" in a window.
 - `03_i18n_helloworld` - Using GNU gettext to introduce translation of strings.
 - `04_user_and_as_root` - Run the application as regular user and "as root".
 - `05_two_import_packages` - Offer a command line and graphical interface to demonstrate two Import Packages in one Distripution package.

# Demo 01 - Simple terminal appliation
 - Install
 - Run
 - Tests
 
# Demo 02 - Simple GUI application

# Demo 03 - Internationalization (i18n) and localization (l10n) using GNU gettext

# Demo 04 - Start application "as root"

# Demo 05 - Multiple import packages

# Additional informations
As real world examples see the following projects:
 - [Hyperorg](https://codeberg.org/buhtz/hyperorg) as a command line application.
 - [Buhtzology](https://codeberg.org/buhtz/buhtzology) as a Python library.

Further reading and official sources about Python Packaging:
 - [Python Packaging User Guide](https://packaging.python.org) especially its [section about the project layout](https://packaging.python.org/en/latest/tutorials/packaging-projects/) using a `src` folder and the discussion [src layout vs flat layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout).
 - [Configuring setuptools using `pyproject.toml`](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html)
 - [PEP 621 - Storing project metadata in `pyproject.tom`](https://peps.python.org/pep-0621)
 - 
 
<sub>November 2023</sub>
