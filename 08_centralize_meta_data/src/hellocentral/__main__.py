"""
    This file is run when you "execute" a package.
    e.g. via "python -m package".
"""
import hellocentralpkg


def main():
    """The entry point for the application."""
    print('Hello World!')

    print(f'Application: {hellocentralpkg.__name__} ({hellocentralpkg.__version__})')
    print(f'License: {hellocentralpkg.__license__}')
    print(f'Author: {hellocentralpkg.__author__}')
    print(f'Maintainer: {hellocentralpkg.__maintainer__}')
    print(f'Website: {hellocentralpkg.__website__}')


if __name__ == '__main__':
    main()
