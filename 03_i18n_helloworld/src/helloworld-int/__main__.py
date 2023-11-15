"""
    This file is run when you "execute" a package.
    e.g. via "python -m package".
"""
import gettext
import helloworldint


def main():
    """The entry point for the application."""

    # Initiate Class-based API of GNU gettext.
    # It installs the ``_()`` in the ``builtins`` namespace and eliminates
    # the need to ``import gettext`` and declare ``_()`` in each module.
    translation = gettext.translation(
        domain='helloworldint',
        # localedir=_GETTEXT_LOCALE_DIR,
        fallback=True
    )
    translation.install()

    # Open the GUI window
    helloworldint.open_main_window()


if __name__ == '__main__':
    main()
