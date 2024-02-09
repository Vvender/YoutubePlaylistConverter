import webbrowser
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
from ExceptionHandler.exception_handler import CustomExceptionHandler


class UtilityEventHandler:
    def __init__(self, app, ui):
        self.app = app
        self.ui = ui

    def utility_event_handler(self):
        try:
            sender = self.app.sender()
            # Check if the sender is the GitHub button
            if sender == self.ui.btn_github:
                # Open the GitHub URL
                QDesktopServices.openUrl(QUrl('https://github.com/Vvender'))
            # Check if the sender is the LinkedIn button
            elif sender == self.ui.btn_linkedin:
                # Open the LinkedIn URL
                QDesktopServices.openUrl(QUrl('https://www.linkedin.com/in/ozan-çatak-06a35a162/'))
            # Check if the sender is the email button
            elif sender == self.ui.btn_email:
                # Open the default email client with the specified email address
                webbrowser.open('mailto:ozancatak@hotmail.com')
            # Check if the sender is the CV button
            elif sender == self.ui.btn_cv:
                # Open the CV URL
                QDesktopServices.openUrl(QUrl('https://amethyst-nancee-79.tiiny.site'))
            elif sender == self.ui.btn_info_return:
                self.ui.pages.setCurrentIndex(0)
            # Check if the sender is a menu button and call page_changer with the corresponding index
        except Exception as e:
            CustomExceptionHandler("Utility Event", e)
