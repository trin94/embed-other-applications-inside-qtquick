import os
import platform
import sys

from PySide6.QtCore import QUrl, Slot, Qt
from PySide6.QtQml import QQmlApplicationEngine, QmlElement
from PySide6.QtQuick import QQuickWindow
from PySide6.QtWidgets import QApplication

QML_IMPORT_NAME = "pyobjects"
QML_IMPORT_MAJOR_VERSION = 1


@QmlElement
class MpvItem(QQuickWindow):

    def __init__(self):
        super().__init__()
        import mpv

        self._player = mpv.MPV(
            wid=f'{self.winId()}',
            # log_handler=print,
            loglevel='debug'
        )

    @Slot()
    def play(self):
        self._player.play('test1.mkv')

    @Slot()
    def terminate(self):
        self._player.terminate()


class MyApp(QApplication):

    def __init__(self):
        super().__init__()
        self._engine = QQmlApplicationEngine()

    def start_engine(self):
        self._engine.load(QUrl.fromLocalFile('qtquick.qml'))

    def verify(self):
        if not self._engine.rootObjects():
            sys.exit(-1)

    def run(self):
        sys.exit(self.exec())


def prepare_mpv():
    if platform.system() == 'Windows':
        os.environ["PATH"] = os.path.dirname(__file__) + os.pathsep + os.environ["PATH"]

    # This is necessary since PySide6 stomps over the locale settings needed by libmpv.
    # This needs to happen after importing PySide6 before creating the first mpv.MPV instance.
    import locale
    locale.setlocale(locale.LC_NUMERIC, 'C')


def main():
    prepare_mpv()

    app = MyApp()
    app.start_engine()
    app.verify()
    app.run()


if __name__ == '__main__':
    main()
