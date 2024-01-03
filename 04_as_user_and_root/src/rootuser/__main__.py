import sys
import os
import getpass
import shutil
from PyQt5.QtWidgets import QApplication
import rootusergui


def run_main_as_root_via_policykit():
    """Start this applicaton again in a new process with root privilegs using
    pkexec.
    """

    # Assuming the package is installed as user only it can not be found in
    # roots Pythons search path. The users Python search path is injected in
    # roots environment via $PYTHONPATH.
    user_sitepackages_path = __file__.rsplit('rootusergui')[0]
    python_path = os.environ.get('PYTHONPATH', '')
    python_path = f'{python_path}:{user_sitepackages_path}'

    cmd = ['pkexec',
           'env',
           f'DISPLAY={os.environ["DISPLAY"]}',
           f'XAUTHORITY={os.environ["XAUTHORITY"]}',
           f'PYTHONPATH={python_path}',
           # In most cases this is /usr/local/bin/bitgui which is not in PATH
           # of pkexec environments.
           shutil.which('usergui')
           ]

    print(f'FOO Try to execute {cmd=}.')

    # See https://github.com/python/cpython/issues/39569
    os.execvp(cmd[0], cmd)


def main():
    """The entry point for the application."""

    text = 'Hello World!\nRunning with PID "{}" as user "{}".' \
        .format(os.getpid(), getpass.getuser())

    print(text)

    app = QApplication(sys.argv)
    dlg = rootusergui.get_main_window(text)
    dlg.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
