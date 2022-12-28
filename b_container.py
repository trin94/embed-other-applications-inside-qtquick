from PySide6.QtCore import Slot, QTimer, Qt
from PySide6.QtQml import QmlElement
from PySide6.QtWidgets import QWidget

from c_storage import STORAGE

QML_IMPORT_NAME = "pyobjects"
QML_IMPORT_MAJOR_VERSION = 1


@QmlElement
class MyEmbedder(QWidget):

    def __init__(self):
        super().__init__()
        self._widget = None
        self._initial_x = 0
        self._initial_y = 0
        self._initial_width = 0
        self._initial_height = 0

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    @Slot()
    def schedule_init(self):
        timer = QTimer()
        timer.singleShot(100, self._init)

    def _init(self):
        self.setGeometry(self._initial_x, self._initial_y, self._initial_width, self._initial_height)
        self.winId()
        self.windowHandle().setParent(STORAGE.QML_WINDOW)
        self.show()

        import mpv

        player = mpv.MPV(
            wid=str(int(self.winId())),
            # log_handler=print,
            loglevel='debug'
        )
        player.play('test1.mkv')

    @Slot(int, int, int, int)
    def set_geometry(self, x: int, y: int, width: int, height: int):
        if self.isVisible():
            self.setGeometry(x, y, width, height)
        else:
            self._initial_x = x
            self._initial_y = y
            self._initial_width = width
            self._initial_height = height
