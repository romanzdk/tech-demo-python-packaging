from setuptools import Command, setup
from setuptools.command.build import build


class CustomBuild(build):
    sub_commands = [
        ("foo", None),
        *build.sub_commands
    ]


class Foo(build):
    def run(self):
        print('X' * 100)
        print(f'{self.build_lib=}')
        print('Z' * 100)

        with open('./src/helloworld-int/foo.txt', 'w') as handle:
            handle.write('bin drin')

setup(
    cmdclass={
        'build': CustomBuild,
        'foo': Foo,
    }
)
