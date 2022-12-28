#!/usr/bin/env python3

import os
import platform
import sys

from PySide6.QtCore import QUrl
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtWidgets import QApplication

from c_storage import STORAGE


class MyApp(QApplication):

    def __init__(self):
        super().__init__()
        self._engine = QQmlApplicationEngine()

    def start_engine(self):
        self._engine.load(QUrl.fromLocalFile('a_app.qml'))

    def verify(self):
        if not self._engine.rootObjects():
            sys.exit(-1)

    def store_qml_window_reference(self):
        STORAGE.QML_WINDOW = self._engine.rootObjects()[0]

    def run(self):
        sys.exit(self.exec())


def prepare_mpv():
    if platform.system() == 'Windows':
        os.environ["PATH"] = os.path.dirname(__file__) + os.pathsep + os.environ["PATH"]

    import locale
    locale.setlocale(locale.LC_NUMERIC, 'C')


def import_custom_qml_component():
    # noinspection PyUnresolvedReferences
    import b_container


def main():
    prepare_mpv()
    import_custom_qml_component()

    app = MyApp()
    app.start_engine()
    app.store_qml_window_reference()
    app.verify()
    app.run()


if __name__ == '__main__':
    main()
