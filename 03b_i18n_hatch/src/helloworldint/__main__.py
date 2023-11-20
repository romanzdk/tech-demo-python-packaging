"""
    This file is run when you "execute" a package.
    e.g. via "python -m package".
"""
import os
import pathlib
import gettext
import helloworldint


def main():
    """The entry point for the application."""

    # First try Pythons site-packages as location of translation files
    localedir = pathlib.Path(helloworldint.__file__).parent / 'locales'

    # Not found
    if not localedir.exists():

        # Try systems locale data dirs (e.g. /usr/share/locales)
        for data_dir in os.environ['XDG_DATA_DIRS'].split(':'):
            localedir = pathlib.Path(data_dir) / 'locales'

            if localedir.exists():
                # found
                break

        else:
            # nothing found
            localedir = None

    # Initiate Class-based API of GNU gettext.
    # It installs the ``_()`` in the ``builtins`` namespace and eliminates
    # the need to ``import gettext`` and declare ``_()`` in each module.
    translation = gettext.translation(
        domain=helloworldint.__name__,
        localedir=localedir,
        fallback=True
    )
    rc = translation.install()

    print(_('Hello World!'))

    # Open the GUI window
    helloworldint.open_main_window()


if __name__ == '__main__':
    main()
