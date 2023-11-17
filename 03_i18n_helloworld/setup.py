import sys
from setuptools import setup
from setuptools.command.build import build
from pathlib import Path


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
        print('X' * 100)
        print(f'{self.build_lib=}')
        print('Z' * 100)

        print(f'{Path.cwd()=}')
        print(f'{self.build_base=}')
        print(f'{self.build_lib=}')
        p = Path.cwd() / self.build_base
        print(f'{p=}')
        print(f'{p.exists()=}')
        print(list(p.glob('*')))
        print(f'{sys.argv=}')


setup(
    cmdclass={
        'build': CustomBuild,
        'foo': Foo,
    }
)
