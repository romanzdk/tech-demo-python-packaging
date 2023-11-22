import sys
import os
import getpass
import shutil
from PyQt5.QtWidgets import QApplication
import rootusergui


def run_main_as_root_via_policykit():
    """Start this applicaton again in a new process with root privilegs using
    pkexec.

    STATUS: Currently this does not work for unknown reasons.
    """
    cmd = ['pkexec', #'--disable-internal-agent',
           # This two environment variables need to be set to make root
           # able to run GUI applications.
           'env',
           f'DISPLAY={os.environ["DISPLAY"]}',
           # f'XAUTHORITY={os.environ["XAUTHORITY"]}',
           # In most cases this is /usr/local/bin/bitgui which is not in PATH
           # of pkexec environments.
           shutil.which('usergui')
           ]

    print(f'Try to execute {cmd=}.')

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
