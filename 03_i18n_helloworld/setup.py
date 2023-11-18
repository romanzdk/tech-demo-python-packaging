from setuptools import setup
from setuptools.command.build import build
from pathlib import Path
import subprocess
import shutil


"""Treat this code as workaround and hack.

It is far away from being an elegant pythonic solution. The author do not
know of a better one but would be happy if someone could provide one.
"""


class CustomBuild(build):
    sub_commands = [
        ("foo", None),
        *build.sub_commands
    ]


class Foo(build):
    """/locales/fr_FR/LC_MESSAGES/messages.mo
    msgfmt --output-file=../locales/de/LC_MESSAGES/helloworldint.mo de
    """
    def run(self):
        print('|==-- Custom build step preparing translation files. --==|')

        # Check if "msgfmt" is available
        if not shutil.which('msgfmt'):
            raise OSError(
                'Executable "msgfmt" (from GNU gettext toots) is not '
                'available. Please install it via a package manager of '
                'your trust. In most cases "msgfmt" is part of "gettext".')

        # Location of the package
        pkg_path = Path.cwd() / 'src' / 'helloworld-int'
        print(f'{pkg_path=}')

        # Collect all po files
        po_files = pkg_path.glob('po/*.po')

        for in_file in po_files:
            print(f'Processing {in_file.name=}')

            out_file = pkg_path / 'locales' / in_file.stem / 'LC_MESSAGES' \
                / 'helloworldint.mo'

            print(f'{out_file=}')
            # Create folder for output file
            out_file.parent.mkdir(parents=True)

            # Compile po-file to mo-file
            rc = subprocess.run(
                ['msgfmt', f'--output-file={out_file}', in_file],
                check=True,
                text=True,
                capture_output=True)

            if rc.stderr:
                raise RuntimeError(rc.stderr)
            print(f'{out_file.exists()=}')
            print(f'{rc=}')

        print('|==-- Custom build step completed. --==|')

setup(
    cmdclass={
        'build': CustomBuild,
        'foo': Foo,
    }
)
