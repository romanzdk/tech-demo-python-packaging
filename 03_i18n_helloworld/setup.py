import setuptools
# from setup.command.install import install

class Foo(setuptools.Command):
    def run(self):
        print('X' * 100)
        print('IN Foo.run()')

        with open('foo.txt', 'w') as handle:
            handle.write('bin drin')


setuptools.setup(
    cmdclass={
        'custom_command': Foo,
    }
)
