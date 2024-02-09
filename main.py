import sys
from ExceptionHandler.exception_handler import CustomExceptionHandler
from PyQt5.QtWidgets import QApplication, QWidget
from EventHandler.utility_event import UtilityEventHandler
from Gui.ui_youtube_list_converter import Ui_Form
from Downloader.downloader import *


class MainWindow:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.ui_window = QWidget()
        self.ui = Ui_Form()  # change
        self.ui.setupUi(self.ui_window)
        self.ui_window.show()

        # Create an instance of EventHandler and pass the app and ui objects
        self.event_handler = UtilityEventHandler(self.app, self.ui)


        # Main Button Events
        self.ui.btn_github.clicked.connect(self.event_handler.utility_event_handler)
        self.ui.btn_linkedin.clicked.connect(self.event_handler.utility_event_handler)
        self.ui.btn_cv.clicked.connect(self.event_handler.utility_event_handler)
        self.ui.btn_email.clicked.connect(self.event_handler.utility_event_handler)
        self.ui.btn_info_return.clicked.connect(self.event_handler.utility_event_handler)
        self.ui.btn_minimize.clicked.connect(self.ui_window.showMinimized)
        self.ui.btn_close.clicked.connect(self.app.quit)
        self.ui.btn_info_return.clicked.connect(self.event_handler.utility_event_handler)

        # File Location Button Event
        self.ui.btn_file_location.clicked.connect(lambda: select_location(self))

        # Download Button Event
        self.ui.btn_download.clicked.connect(lambda: download_playlist(self))


if __name__ == "__main__":
    main_app = MainWindow()
    sys.exit(main_app.app.exec_())
