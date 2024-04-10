#!/usr/bin/env python3
import os
import platform
import sys

from PySide6.QtCore import *
from PySide6.QtGui import QAction
from PySide6.QtWidgets import *


class MyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.menu_bar = QMenuBar(self)
        self.menu_entry = self.menu_bar.addMenu('Actions')
        self.action1 = QAction('Action 1')
        self.menu_entry.addAction(self.action1)
        self.action2 = QAction('Action 2')
        self.menu_entry.addAction(self.action2)
        self.action3 = QAction('Action 3')
        self.menu_entry.addAction(self.action3)

        self.setMenuBar(self.menu_bar)

        self.container = QWidget(self)
        self.container.setMinimumWidth(640)
        self.container.setMinimumHeight(480)
        self.setCentralWidget(self.container)
        self.container.setAttribute(Qt.WA_DontCreateNativeAncestors)
        self.container.setAttribute(Qt.WA_NativeWindow)

        import mpv

        player = mpv.MPV(
            wid=str(int(self.container.winId())),
            # log_handler=print,
            loglevel='debug'
        )
        player.play('test1.mkv')


def prepare_mpv():
    if platform.system() == 'Windows':
        os.environ["PATH"] = os.path.dirname(__file__) + os.pathsep + os.environ["PATH"]

    # This is necessary since PySide6 stomps over the locale settings needed by libmpv.
    # This needs to happen after importing PySide6 before creating the first mpv.MPV instance.
    import locale
    locale.setlocale(locale.LC_NUMERIC, 'C')


def main():
    prepare_mpv()

    app = QApplication()
    win = MyMainWindow()
    win.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
