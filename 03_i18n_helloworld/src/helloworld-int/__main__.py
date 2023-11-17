"""
    This file is run when you "execute" a package.
    e.g. via "python -m package".
"""
import pathlib
import gettext
import helloworldint


def main():
    """The entry point for the application."""

    localedir = pathlib.Path(helloworldint.__file__).parent / 'locales'

    # Initiate Class-based API of GNU gettext.
    # It installs the ``_()`` in the ``builtins`` namespace and eliminates
    # the need to ``import gettext`` and declare ``_()`` in each module.
    translation = gettext.translation(
        domain='messages',
        localedir=localedir,
        fallback=True
    )
    rc = translation.install()

    print(f'{rc=}')
    print(f'{translation=}')

    print(_('Hello World!'))
    # Open the GUI window
    helloworldint.open_main_window()


if __name__ == '__main__':
    main()
