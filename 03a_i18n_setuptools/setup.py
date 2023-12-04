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
    """This class overwrites the default build class.

    The original list of build commands is shadowed and the custom build
    command is injected as first entry. The commands from the original list
    are appended again.

    This approach comes from one of the setuptools maintainers:
    https://github.com/pypa/setuptools/discussions/3912
    """
    sub_commands = [
        ("handletranslation", None),
        *build.sub_commands
    ]


class HandleTranslation(build):
    """Compile po into mo files using msgfmt.
    """

    def run(self):
        print('|==-- Custom build step preparing translation files. --==|')

        # Check if "msgfmt" is available
        if not shutil.which('msgfmt'):
            raise OSError(
                'Executable "msgfmt" (from GNU gettext tools) is not '
                'available. Please install it via a package manager of '
                'your trust. In most cases "msgfmt" is part of "gettext".')

        # Location of the package
        pkg_path = Path.cwd() / 'src' / 'helloworldint'
        print(f'{pkg_path=}')

        # Collect all po files
        po_files = pkg_path.glob('po/*.po')

        for in_file in po_files:
            print(f'Processing {in_file.name=}')

            out_file = pkg_path / 'locales' / in_file.stem / 'LC_MESSAGES' \
                / 'helloworldint.mo'

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

        print('|==-- Custom build step completed. --==|')


setup(
    cmdclass={
        'build': CustomBuild,
        'handletranslation': HandleTranslation,
    }
)
