<sub>December 2023</sub>
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
  - [Demo 01 variant "setuptools"](#demo-01-variant-setuptools)
  - [Demo 01 variant "hatch"](#demo-01-variant-hatch)
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
 - `05_two_import_packages` - Demonstrate two Import Packages in one Distripution package and other naming issues.

Please feel free to open issues.

# Demo 01 - Simple terminal application

This demo starts as simpelst application possible just printing `Hello World` to the terminal to illustrate basic concepts of modern Python packaging and build-systems. The demo comes in two variants differing by the used build-backends `setuptools` and `hatch`. These concepts are covered by this demo:

 - Python Package configuration via `pyproject.toml` ([PEP 621](https://peps.python.org/pep-0621))
 - Use of the ["src layout"](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/).
 - Installing the package in [Development Mode](https://setuptools.pypa.io/en/latest/userguide/development_mode.html) also known as _editable installation_ to avoid manipulation of `sys.path` and other `import` hacks.
 - Run tests and the application itself.
 - Use of `__init__.py` and `__main__.py`.

The comments in the files do contain more detailed explanations.

## About Python Packaging

How to tie up a Python package is easy but the topic itself is not. The latter is because since Python was born in 1991 and while it's [ongoing evolution multiple packaging systems](https://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/history.html) has been created. Keep this in mind when looking around for alternative documentation and tutorials and look on their dates because they might be outdated.

## About the folder structure and the "src layout"

This is an example of the so called [src layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/). The package-folder `helloworld-cli` is separated in a sub-folder named `src`. If you have no good reason agsinst it do it that way.

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

## Development Mode / Editabel installs

While developing and testing a Python project (not recommended!) constructs like this are often used.

    # Don't do this at home!!!
    import unittest
    import sys

    sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

    import mypackage
	
The environment variable [`PYTHONPATH` and
`sys.path`](https://docs.python.org/3/library/sys.html#sys.path) do define
where the python interpreter looks for new modules. That variable was and is
often manipulated to fulfil the developers needs. Today is no need anymore
for risky and unstable hacks like this. Never touch `sys.path`.

The solution is the [Development Mode](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/#working-in-development-mode)
also known as [editable install](https://pip-python3.readthedocs.io/en/latest/reference/pip_install.html#editable-installs)
([PEP660](https://peps.python.org/pep-0660/)).
The package in development is kind of *installed*. The Python interpreter see
the package as it was installed. But because of symlinks used in that special
mode the source files in the git repository are used. This also means that each
modification on the source has an immediate effect on the package available to
the system. To install a package in _Development Mode_ `pip`'s option `-e` or `--editable` is used.

## Demo 01 variant "setuptools"

All package related information including how to build it is located only one file named `pyproject.toml`.

    [build-system]
    requires = ["setuptools"]
    build-backend = "setuptools.build_meta"

    # ...

    [project]
    name = "helloworld-cli"
    version = "0.0.1"

    [project.scripts]
    helloworldterminal = "helloworldcli.__main__:main"

    [tool.setuptools.package-dir]
    helloworldcli = 'src/helloworldcli'

The first three lines specifing the `[build-system]`. In this demo it is the often used `setuptools`. The section `[tools.setuptools.package-dir]` do point to the location of the package files. And `helloworldterminal` in section `[project.scripts]` do name the executable of that package.

[[terminal_helloworld.gif]]

## Demo 01 variant "hatch"

A lot of alterntive build-systems do exists and can be used. The differences and use cases can not be covered here. Using [`hatch`](https://hatch.pypa.io) just ilustrates how to setup a build-backend in the `pyproject.toml`.

    [build-system]
    requires = ['hatchling']
    build-backend = 'hatchling.build'

    # ...

    [tool.hatch.build.targets.wheel]
    packages = ['src/helloworldcli']

The usage of `pip` do not change.

# Demo 02 - Simple GUI application

That demo illustrates the handling of dependencies in the Python Packaging process with displaying the string `Hello World!` in a GUI window. 
The GUI package [`PySimpleGUI`](https://www.pysimplegui.org) is the dependency and used to create the window. The key difference to the previous demo is the use of the `dependencies` variable in the `pyproject.toml` file.

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

This demo use the [GNU gettext](https://www.gnu.org/software/gettext) localization framework to offer a translated version of the string `Hello World!`. The translation itself is not the topic of this demo but the handling of the translational files is.

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
	├── README.md
	├── pyproject.toml
	├── setup.py
	└── src
            └── helloworldint
                ├── __init__.py
                ├── __main__.py
                └── po
                    ├── de.po
                    ├── jp.po
                    └── messages.pot

The `pyproject.toml` do define `package-data`. While installing the
build-backend `setuptools` will look for a folder `locales` and its content
defined by the search pattern used here.

	[tool.setuptools.package-data]
	helloworldint = [
		'locales/*/LC_MESSAGES/*.mo',
	]

Independed from the used build-backendn (`setuptools` or `hatch` in this example) the general approach here is to use a _custom build step_. That step is executed before the package is installed into the system. That step use `msgfmt` in an external system call (using `subprocess.run()`) to compile the `po` files into `mo` files and create them in the appropriated folder structure. The projects source folder will look like this:

    03_i18n_setuptools
	├── ...
        └── src
            └── helloworldint
                ├── __init__.py
                ├── __main__.py
                ├── locales
                │   ├── de
                │   │   └── LC_MESSAGES
                │   │       └── helloworldint.mo
                │   └── jp
                │       └── LC_MESSAGES
                │           └── helloworldint.mo
                └── po
                    ├── de.po
                    ├── jp.po
                    └── messages.pot

The custom build step is implemented in the `setup.py` file. See that file for more details and further references.

[[gui_i18n.gif]]

## Demo 03 variant "hatch"

Please see the previous variant using `setuptools` to get an idea about the approach using a custom-build step. Using `hatch` as build-backend the `pyproject.toml` file is modified:

    [tool.hatch.build]
    exclude = ['src/helloworldint/po']
    artifacts = ['src/helloworldint/locales/*/LC_MESSAGES/*.mo']

The folder `po` is excluded because this files are useless for the installation. The `artifacts` variable takes care that the `mo` files generated by the custom build step are included in the installation. The file `hatch_build.py` is used by default to implement custom build steps. See comments in the `pyproject.toml` file to see how to use different names.

# Demo 04 - Start application "as root"

> **WARNING**:
> This demo propagates to install it using `sudo -H`. This is prohibited
> because of [security reasons](https://askubuntu.com/a/802594/416969).
> The author is open for alternative solutions.

> **ATTENTION**:
> In its current state this technical demo do not work and need assistance.
> The issues are described in more details below.

This is the error message

```
Running with PID "6923" as user "root".
Authorization required, but no authorization protocol specified

qt.qpa.xcb: could not connect to display :10.0
qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.
This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.

Available platform plugins are: eglfs, linuxfb, minimal, minimalegl, offscreen, vnc, wayland-egl, wayland, wayland-xcomposite-egl, wayland-xcomposite-glx, xcb.
```

In the screencast below I do install usually as a user via `python3 -m pip install .` On some systems it might help to install with admin rights via `sudo --set-home python3 -m pip install .`. Otherwise the "run as root" entry point scripts won't find the Python sources files. But I am not sure about it and I also don't think that this is the reason for the main problem.

[[gui_as_root.gif]]

# Demo 05 - Multiple import packages
In this demo the two terms [Distribution Package](https://packaging.python.org/en/latest/glossary/#term-Distribution-Package) and [Import Package](https://packaging.python.org/en/latest/glossary/#term-Import-Package) are explained. A Distribution Package is the entity or the name you do use when installing "a package" via `pip` (e.g. from PyPI). In this example it is `howareyouworld`. An Import Package is the name you do use in Python code when using the `import` statement. In this example there are two Import Packages named `helloworldpkg` and `howareyoupkg`. Additionally this example do installs two start scripts (entry points) named `helloworldcli` and `howareyoucli`. And as last the name of the package folders (inside `/src`) are `helloworld` and `howareyou`. The key fact is that all these elements having different names. In most projects the names will be the same and not different.

See the `pyproject.toml` to see how these names are definied:


    # Distribution Package
    [project]
    name = "howareyouworld"

    # Import Packages pointing to their package folders
    [tool.setuptools.package-dir]
    helloworldpkg = 'src/helloworld'
    howareyoupkg = 'src/howareyou'

    # The executable scripts (entry points)
    [project.scripts]
    helloworldcli = "helloworldpkg.__main__:main"
    howareyoucli = "howareyoupkg.__main__:main"

After installation using `pip` (see previous demos) the code can be used in several ways:

    $ python3 -m pip install .
    ...
    Successfully installed howareyouworld-0.0.1

    $ helloworldcli
    Hello World!

    $ howareyoucli
    Hello World!
    How are you?                                                                                     

    $ python3
    >>> import helloworldpkg
    >>> import howareyoupkg

The package `howareyoupkg` do depend on `helloworldpkg`. See the file `src/howareyou/__main__.py` for details.

# Demo 06 - Reporting test coverage
tests/test_fruits.py::TestJustTrue::test_true PASSED                             [ 25%]
tests/test_fruits.py::TestTrueOrFalse::test_error PASSED                         [ 50%]
tests/test_fruits.py::TestTrueOrFalse::test_false PASSED                         [ 75%]
tests/test_fruits.py::TestTrueOrFalse::test_true PASSED                          [100%]

Name                                                           Stmts   Miss  Cover
----------------------------------------------------------------------------------
/usr/local/lib/python3.9/dist-packages/iniconfig/__init__.py     122     99    19%
/usr/local/lib/python3.9/dist-packages/tomli/__init__.py           4      0   100%
/usr/local/lib/python3.9/dist-packages/tomli/_parser.py          458    193    58%
/usr/local/lib/python3.9/dist-packages/tomli/_re.py               35     20    43%
/usr/local/lib/python3.9/dist-packages/tomli/_types.py             4      0   100%
src/fruits/__init__.py                                             8      0   100%
tests/__init__.py                                                  0      0   100%
tests/test_fruits.py                                              12      0   100%
----------------------------------------------------------------------------------
TOTAL                                                            643    312    51%

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
 - [PEP 517 – A build-system independent format for source trees](https://peps.python.org/pep-0517)
 - [The basics of Python packaging in early 2023](https://drivendata.co/blog/python-packaging-2023)
 - [Python packages with pyproject.toml and nothing else](https://til.simonwillison.net/python/pyproject)
 - [Answer to "Is `sudo pip install` still a broken practice?" at AskUbuntu.com](https://askubuntu.com/a/802594/416969)
 
<sub>December 2023</sub>

