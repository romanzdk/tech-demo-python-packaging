<sub>December 2023</sub>
> **NOTE**: The code in this repository and its documentation is still work in
> progress but will be completed soon.

# Python Packaging - A technical demonstration

The purpose of this repository is to illustrate the packaging of Python
projects. It contains multiple projects in different flavours illustrating
several use cases.

The examples try to follow the current state of the art and official
recommendations (e.g. `pyproject.toml`, "src layout" and _Development Mode_
via `--editable` option). More details can be found in the sub folders.

Please feel free to open issues to ask questions, request support, report
problems or suggest alternative solutions.

## TOC

- [Overview of the demos](#overview-of-the-demos)
- [Potential problems and their solutions](#potential-problems-and-their-solutions)
   - [Missing PEP 660 (pyproject.toml) support](#missing-pep-660-pyproject-toml-support)
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
- [Demo 06 - Test coverage](#demo-06-test-coverage)
- [Demo 07 - Coverage reports combined](#demo-07-coverage-reports-combined)
- [Demo 08 - Centralize project meta data to eliminate redundancies or how to get the version string into your application?](#demo-08-centralize-project-meta-data-to-eliminate-redundancies-or-how-to-get-the-version-string-into-your-application)
- [Real world examples](#real-world-examples)
- [Further reading and official sources about Python Packaging](#further-reading-and-official-sources-about-python-packaging)

# Overview of the demos

Each sub folders is one example. They could be treated as a project folder or
a repository.

 - `01a_terminal_helloworld_setuptools` - Minimal packaging and installing demo just print "Hello World".
 - `01b_terminal_helloworld_hatch` - Minimal packaging and installing demo using `hatch` as alternative build backend.
 - `02_gui_helloworld` - Introduce the use of dependencies using a GUI to print "Hello World" in a window.
 - `03a_i18n_setuptools` - Using GNU gettext to introduce translation of strings.
 - `03b_i18n_hatch` - Handle GNU gettext translation using `hatch` as alternative build backend.
 - `04_user_and_as_root` - Executable as regular user and administrator ("as root").
 - `05_two_import_packages` - Demonstrate two Import Packages in one Distribution Package and other naming issues.
 - `06_test_coverage` - Measure and report test coverage.
 - `07_multi_coverage` - Combine test coverage measurement of two Distribution Packages into one report.
 - `08_centralize_meta_data` - Specify project meta data exclusively in ony file.

# Potential problems and their solutions
## Missing PEP 660 (pyproject.toml) support
The following error message can occur when installing one of the demos.

      Checking if build backend supports build_editable ... done
    ERROR: Project file:///XYZ has a 'pyproject.toml' and its build backend
    is missing the 'build_editable' hook. Since it does not have a 'setup.py'
    nor a 'setup.cfg', it cannot be installed in editable mode.
    Consider using a build backend that supports PEP 660.
    
The reason is a `setuptools` package older then version `61.0.0`. Upgrade
`setuptools` (or `pip`) with the package manager of your choice; e.g. `python3
-m pip install --upgrade setuptools`.

# Demo 01 - Simple terminal application

This minimal demo just printing `Hello World` to the terminal to illustrate
basic concepts of modern Python packaging and build-systems. The demo comes in
two variants differing by the used build-backends `setuptools` and
`hatch`. The following concepts are covered by this demo:

 - Python Package configuration via `pyproject.toml` ([PEP 621](https://peps.python.org/pep-0621))
 - Use of the ["src layout"](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/).
 - Installing the package in [Development Mode](https://setuptools.pypa.io/en/latest/userguide/development_mode.html) also known as _editable installation_ to avoid manipulation of `sys.path` and other `import` hacks.
 - Run tests and the application itself.
 - Use of `__init__.py` and `__main__.py`.

The comments in the files contain more detailed explanations.

## About Python Packaging

How to tie up a Python package is easy but the topic itself is not. The latter
is because since Python was born in 1991 and while it's
[ongoing evolution multiple packaging systems](https://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/history.html)
has been created. Keep this in mind when looking around for alternative
documentation and tutorials and look on their dates because they might be
outdated.

## About the folder structure and the "src layout"

This is an example of the so called "src layout" (see discussion:
[src-layout vs. flat-layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/)).
The package-folder `helloworldcli` is separated in a sub-folder named `src`.
If you have no good reason against it do it that way.

    01_terminal_helloworld
    ├── LICENSE
    ├── pyproject.toml
    ├── README.md
    ├── src
    │   └── helloworldcli
    │       ├── __init__.py
    │       └── __main__.py
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
`sys.path`](https://docs.python.org/3/library/sys.html#sys.path) does define
where the Python interpreter looks for new modules. That variable was and is
often manipulated to fulfil the developers needs. But today there is no need
anymore for risky and unstable hacks like this. Never touch `sys.path`.

The solution is the [Development Mode](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/#working-in-development-mode)
also known as [editable install](https://pip-python3.readthedocs.io/en/latest/reference/pip_install.html#editable-installs)
([PEP660](https://peps.python.org/pep-0660/)).
The package in development is kind of *installed*. The Python interpreter see
the package as it was installed. But because of symlinks used in that special
mode the source files in the git repository are used. This also means that each
modification on the source has an immediate effect on the package available to
the system. To install a package in _Development Mode_ `pip`'s option `-e` or `--editable` is used.

## Demo 01 variant "setuptools"

All package related information including how to build it is located in only one file named `pyproject.toml`.

    [build-system]
    requires = ["setuptools >= 61.0.0"]
    build-backend = "setuptools.build_meta"

    # ...

    [project]
    name = "helloworld-cli"
    version = "0.0.1"

    [project.scripts]
    helloworldterminal = "helloworldcli.__main__:main"

    [tool.setuptools.package-dir]
    helloworldcli = 'src/helloworldcli'

The first three lines specifying the `[build-system]`. In this demo it is the
widely used `setuptools`. Its version is restricted to 61 or higher because the
support for `pyproject.toml` was introduced with that version in March 2022.
The section `[tools.setuptools.package-dir]` does
point to the location of the package files. And `helloworldterminal` in
section `[project.scripts]` does name the executable of that package.

[[terminal_helloworld.gif]]

Again the necessary commands to install and run:

    git clone https://codeberg.org/buhtz/tech-demo-python-packaging.git
    cd tec*/01a*
    python3 -m pip install --editable .
    helloworldterminal

And the full output:

    $ git clone https://codeberg.org/buhtz/tech-demo-python-packaging.git
    Cloning into 'tech-demo-python-packaging'...
    remote: Enumerating objects: 363, done.
    remote: Counting objects: 100% (363/363), done.
    remote: Compressing objects: 100% (331/331), done.
    remote: Total 363 (delta 158), reused 0 (delta 0), pack-reused 0
    Receiving objects: 100% (363/363), 7.08 MiB | 1.81 MiB/s, done.
    Resolving deltas: 100% (158/158), done.

    $ cd tec*/01a*
    $ python3 -m pip install --editable .
    Defaulting to user installation because normal site-packages is not writeable
    Obtaining file:///home/user/tech-demo-python-packaging/01a_terminal_helloworld_setuptools
    Installing build dependencies ... done
    Checking if build backend supports build_editable ... done
    Getting requirements to build editable ... done
    Installing backend dependencies ... done
    Preparing editable metadata (pyproject.toml) ... done
    Building wheels for collected packages: helloworld-cli
    Building editable for helloworld-cli (pyproject.toml) ... done
    Created wheel for helloworld-cli: filename=helloworld_cli-0.0.1-0.editable-py3-none-any.whl size=26798 sha256=aed4d9190a07f5d993ec4d8001f13a8b71cfa3c1276b962e660e15f67369fc9a
    Stored in directory: /tmp/pip-ephem-wheel-cache-vgxzidv7/wheels/20/1c/e6/5c3d25d5ae15a2af7acd3677ea8149a76282633e96798cd784
    Successfully built helloworld-cli
    DEPRECATION: gpg 1.14.0-unknown has a non-standard version number. pip 24.0 will enforce this behaviour change. A possible replacement is to upgrade to a newer version of gpg or contact the author to suggest that they release a version with a conforming version number. Discussion can be found at https://github.com/pypa/pip/issues/12063
    Installing collected packages: helloworld-cli
    Successfully installed helloworld-cli-0.0.1

    $ helloworldterminal
    Hello World!

    $ whereis helloworldterminal
    helloworldterminal: /home/user/.local/bin/helloworldterminal

    $ pytest -v
    ===================================== test session starts =====================================
    platform linux -- Python 3.9.2, pytest-7.4.2, pluggy-1.3.0 -- /usr/bin/python3
    cachedir: .pytest_cache
    hypothesis profile 'default' -> database=DirectoryBasedExampleDatabase(PosixPath('/home/user/tech-demo-python-packaging/01a_terminal_helloworld_setuptools/.hypothesis/examples'))
    rootdir: /home/user/tech-demo-python-packaging/01a_terminal_helloworld_setuptools
    plugins: hypothesis-6.92.2, pyfakefs-5.2.4, anyio-4.2.0
    collected 2 items                                                                             

    tests/test_dummy.py::DummyTest::test_dummy PASSED                                       [ 50%]
    tests/test_dummy.py::DummyTest::test_import PASSED                                      [100%]


    ====================================== 2 passed in 2.13s ======================================

    $ python3 -m pip uninstall helloworld-cli
    Found existing installation: helloworld-cli 0.0.1
    Uninstalling helloworld-cli-0.0.1:
    Would remove:
        /home/user/.local/bin/helloworldterminal
        /home/user/.local/lib/python3.9/site-packages/__editable__.helloworld_cli-0.0.1.pth
        /home/user/.local/lib/python3.9/site-packages/__editable___helloworld_cli_0_0_1_finder.py
        /home/user/.local/lib/python3.9/site-packages/helloworld_cli-0.0.1.dist-info/*
    Proceed (Y/n)? Y
    Successfully uninstalled helloworld-cli-0.0.1


## Demo 01 variant "hatch"

A lot of alternative build-systems exists and can be used. The differences
and use cases can not be covered here. Using [`hatch`](https://hatch.pypa.io)
just illustrates how to setup an alternative build-backend in the
`pyproject.toml`. The usage of `pip` does not change.

    [build-system]
    requires = ['hatchling']
    build-backend = 'hatchling.build'

    # ...

    [tool.hatch.build.targets.wheel]
    packages = ['src/helloworldcli']


# Demo 02 - Simple GUI application

That demo illustrates the handling of dependencies. It displays the string
`Hello World!` in a GUI window.  The GUI package
[`PySimpleGUI`](https://www.pysimplegui.org) is the dependency and used to
create the window. The key difference to the previous demo is the use of the
`dependencies` variable in the `pyproject.toml` file.

    [project]
    name = "helloworld-gui"

    # ...

    dependencies = [
        "PySimpleGUI",
    ]

    # ...

With this modification `pip` does install depending packages in the back.

[[gui_helloworld.gif]]

# Demo 03 - Internationalization (i18n) and localization (l10n) using GNU gettext

The [GNU gettext](https://www.gnu.org/software/gettext) localization framework is used to offer a translated version of the string `Hello World!`. The translation itself is not the topic of this demo but the handling of the translation files is in the context of Python Packing. Two variants of this demo exists differing by the used build-backends (`setuptools` and `hatch`). The latter is used because it offers a more elegant, pythonic and easier to understand solution.

Independent from the used build-backend the general approach is to use a _custom build step_. That step is executed before the package is installed into the system. That step use `msgfmt` in an external system call (using `subprocess.run()`) to compile the `po` files into `mo` files and create them in the appropriated folder structure.
After the custom build step the projects source folder will look like this:

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

The files in the `po` folder are from the original source. The files in the
`locales` folder are generate via the custom build step.

## Demo 03 variant "setuptools"

> **NOTE**:
> Handle this example with care. It might not be the best solution nor it is
> pythonic. Feel free to open an Issue to provide an easier and better
> example.

The `mo` files (generated by the custom build step) are included as
`package-data` files while installing. The `pyproject.toml` does define
`package-data`. The build-backend `setuptools` will look for a folder
`locales` and its content defined by the search pattern used here.

    [tool.setuptools.package-data]
    helloworldint = [
        'locales/*/LC_MESSAGES/*.mo',
    ]

The custom build step is implemented in the `setup.py` file. See that file for
more details and further references.

[[gui_i18n.gif]]

## Demo 03 variant "hatch"

Using `hatch` as build-backend the `pyproject.toml` file is modified:

    [tool.hatch.build]
    exclude = ['src/helloworldint/po']
    artifacts = ['src/helloworldint/locales/*/LC_MESSAGES/*.mo']

The folder `po` is excluded because this files are used by the custom build
step but useless for the installation. The `artifacts` variable takes care
that the `mo` files generated by the custom build step are included in the
installation. The file `hatch_build.py` is used by default to implement custom
build steps.

# Demo 04 - Start application "as root"

> **ATTENTION**:
> This technical demo might have security implications. The authors
> recommendation is to use this approach only in development context but not
> for regular users. The latter should install an application using the 
> package manager of their own Linux distributions (e.g. apt, pacman, etc).

In the screencast below I do install usually as a user via `python3 -m pip
install .` On some systems it might help to install with admin rights via
`sudo --set-home python3 -m pip install .`. Otherwise the "run as root" entry
point scripts won't find the Python sources files. But I am not sure about it
and I also don't think that this is the reason for the main problem.

[[gui_as_root.gif]]

# Demo 05 - Multiple import packages

The two terms
[Distribution Package](https://packaging.python.org/en/latest/glossary/#term-Distribution-Package)
and [Import Package](https://packaging.python.org/en/latest/glossary/#term-Import-Package)
and other naming issues are illustrated in this demo. A Distribution Package
is the entity or the name you do use when installing "a package" via `pip`
(e.g. from PyPI). In this example it is `howareyouworld`. An Import Package is
the name you do use in Python code when using the `import` statement. In most
Python Projects you will find similar names for this two concepts. But
technically they are different
(see [Distribution package vs. import package](https://packaging.python.org/en/latest/discussions/distribution-package-vs-import-package)).
In this example there are two Import Packages
named `helloworldpkg` and `howareyoupkg`.

Additionally this example does install two start scripts (entry points) named
`helloworldcli` and `howareyoucli`. And as last the name of the package
folders (inside `/src`) are `helloworld` and `howareyou`. The key fact to
notice is that all these elements have different names.

See the `pyproject.toml` to see how these names are defined:


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

The package `howareyoupkg` does depend on `helloworldpkg`.
See the file `src/howareyou/__main__.py` for details.

# Demo 06 - Test coverage

The usage and configuration of [`coverage`](https://coverage.readthedocs.io)
to calculate a **strict** _test coverage_ for a project using `pyproject.toml`
and the "src layout" is illustrated. The _test coverage_ is defined as "How
much productive code is executed by the code in the test suite?".

The default behavior of `coverage` has its shortcomings and would lead into
invalid measurements. This demo does take the following into account:

- External Python libraries (third party and Python standard libs) should not
  included in the calculation.
- Python files that are not loaded by the test suite should be included into
  the calculation as uncovered code.

Install the package:

    $ git clone https://codeberg.org/buhtz/tech-demo-python-packaging.git
    $ cd tec*/06*
    $ python3 -m pip install .
    $ bananacli
    Hello World! Eat a banana.

Run `coverage` and create the report:

    $ coverage run
    $ coverage report

The output should look like this:

```
Name                                                                Stmts   Miss  Cover   Missing
-------------------------------------------------------------------------------------------------
/home/user/.local/lib/python3.11/site-packages/banana/__init__.py       8      0   100%
/home/user/.local/lib/python3.11/site-packages/banana/__main__.py       4      4     0%   1-6
/home/user/.local/lib/python3.11/site-packages/banana/foo.py            2      2     0%   1-2
-------------------------------------------------------------------------------------------------
TOTAL                                                                  14      6    57%
```

There where no arguments or switches used on command line because the
configuration reside in the `pyproject.toml` file:

    [tool.coverage.run]
    command_line = "--module pytest --verbose"
    source = ["banana"]

    [tool.coverage.report]
    show_missing = true

The `command_line` value is used by `coverage` to execute the test suite. The
`source` is just the name of the Import Package. The file `foo.py` is part of
the report even if it was never loaded by the test suite.

# Demo 07 - Coverage reports combined

As an extension to the previous demo the coverage of two separate Distribution
Packages is measured and combined.

Install both packages (`fruit` and `vegetable`) as usual. The `coverage run`
need to be done on each package separate. The resulting data files
(`.coverage`) then combined and reported at once:

```
Name                                                                 Stmts   Miss  Cover
----------------------------------------------------------------------------------------
/home/user/.local/lib/python3.11/site-packages/cherry/__init__.py        8      1    88%
/home/user/.local/lib/python3.11/site-packages/cherry/__main__.py        4      4     0%
/home/user/.local/lib/python3.11/site-packages/cherry/foo.py             2      2     0%
/home/user/.local/lib/python3.11/site-packages/pumpkin/__init__.py       8      6    25%
/home/user/.local/lib/python3.11/site-packages/pumpkin/__main__.py       4      4     0%
/home/user/.local/lib/python3.11/site-packages/pumpkin/bar.py            2      0   100%
----------------------------------------------------------------------------------------
TOTAL                                                                   28     17    39%
```

See the file `do_combined_coverage.sh` for detailed steps:

    #!/usr/bin/env sh

    # Run and report coverage on both distribution packages separate
    cd fruit
    coverage run
    coverage report
    cd ../vegetable
    coverage run
    coverage report
    cd ..

    # Combine the coverage data into one file
    coverage combine --keep fruit/.coverage vegetable/.coverage

    # Report
    coverage report


# Demo 08 - Centralize project meta data to eliminate redundancies or how to get the version string into your application?

It is usual and often recommended to locate an applications or package meta
data in module variables like this:

	>>> import hellocentralpkg
	>>> hellocentralpkg.__version__
	'0.0.1'

Some projects have hard coded version strings in several code locations and
documentation files. They use shell scripts or some tools to modify that
version strings before each release. This is a workaround not a solution.

One possible solution is the [`importlib.metadata`](https://docs.python.org/3/library/importlib.metadata.html)
module. It gives a
python application the opportunity to access all its meta data
that was specified in `pyproject.toml`. 
A helper function is offered in this demo.
The function `_package_metadata_as_dict()` get the meta data and store it as a
well accessible `dict` in the module variable `helloworldpkg.meta`.

The file `__main__.py` does produce this output with meta data retrieved from
`pyproject.toml`:

    $ hellocentralcli
    Hello World!
    Application: hellocentralpkg in hellocentralapp (0.0.1)
    License: GNU GENERAL PUBLIC LICENSE
    Version 3, 29 June 2007
    See License file "LICENSE".
    Author: Christian Buhtz <c.buhtz@posteo.jp>
    Maintainer: Christian Buhtz <c.buhtz@posteo.jp>
    Website: https://codeberg.org/buhtz/tech-demo-python-packaging

Be aware that [PEP621](https://peps.python.org/pep-0621/) about
`pyproject.toml` does offer
[*Dynamic Meta Data*](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html#dynamic-metadata).
The intention is good but a current shortcoming is that this feature is
restricted to a small bunch of variables and not suited for all fields that
are used in a `pyproject.toml`. The second shortcoming is that it is against
the original intention of `pyproject.toml` to specify projects meta data. It
is the humble opinion of the author of that repo that meta data shouldn't be
specified anywhere else then the `pyproject.toml` because it ease up things
and reduce maintainers burden.

# Real world examples
 - [Hyperorg](https://codeberg.org/buhtz/hyperorg) as a command line application.
 - [Buhtzology](https://codeberg.org/buhtz/buhtzology) as a Python library.

# Further reading and official sources about Python Packaging
 - [Python Packaging User Guide](https://packaging.python.org) especially in there
   - the [section about the project layout](https://packaging.python.org/en/latest/tutorials/packaging-projects/) using a `src` folder
   - and the discussion about [src layout vs flat layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout)
   - and [the Packaing tutorial](https://packaging.python.org/en/latest/tutorials/packaging-projects)
   - and [Distribution package vs. import package](https://packaging.python.org/en/latest/discussions/distribution-package-vs-import-package).
 - [Configuring setuptools using `pyproject.toml`](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html)
 - [PEP 621 - Storing project metadata in `pyproject.tom`](https://peps.python.org/pep-0621)
 - [PEP 517 – A build-system independent format for source trees](https://peps.python.org/pep-0517)
 - [The basics of Python packaging in early 2023](https://drivendata.co/blog/python-packaging-2023)
 - [Python packages with pyproject.toml and nothing else](https://til.simonwillison.net/python/pyproject)
 - [Answer to "Is `sudo pip install` still a broken practice?" at AskUbuntu.com](https://askubuntu.com/a/802594/416969)
 
<sub>December 2023</sub>

