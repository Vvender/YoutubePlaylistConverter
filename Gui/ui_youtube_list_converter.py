from PyQt5 import QtCore, QtGui, QtWidgets
import Gui.Icons.youtube_rc as youtube_rc


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(869, 716)
        self.frm_outer = QtWidgets.QFrame(Form)
        self.frm_outer.setGeometry(QtCore.QRect(140, 190, 482, 332))
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frm_outer.sizePolicy().hasHeightForWidth())
        self.frm_outer.setSizePolicy(sizePolicy)
        self.frm_outer.setMaximumSize(QtCore.QSize(800, 600))
        self.frm_outer.setStyleSheet("background-color:#2596be;\n"
                                     "border-radius:20px;\n"
                                     "")
        self.frm_outer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_outer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_outer.setObjectName("frm_outer")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frm_outer)
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frm_middle = QtWidgets.QFrame(self.frm_outer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frm_middle.sizePolicy().hasHeightForWidth())
        self.frm_middle.setSizePolicy(sizePolicy)
        self.frm_middle.setStyleSheet(
            "background-color:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:0.715909,stop:0 rgba(0,0,0,9), stop:0.375 rgba(0,0,0,50),stop:0.835227 rgba(0,0,0,75));\n"
            "border-radius:20px;\n"
            "")
        self.frm_middle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_middle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_middle.setObjectName("frm_middle")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frm_middle)
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frm_inside = QtWidgets.QFrame(self.frm_middle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frm_inside.sizePolicy().hasHeightForWidth())
        self.frm_inside.setSizePolicy(sizePolicy)
        self.frm_inside.setStyleSheet("/* FRAME STYLE */\n"
                                      "QFrame{\n"
                                      "    background-color: transparent;\n"
                                      "    border-radius: 15px;\n"
                                      "}\n"
                                      "\n"
                                      "/* BUTTON STYLE */\n"
                                      "QPushButton{\n"
                                      "    background-color: transparent;\n"
                                      "    color: #2596be;\n"
                                      "    border-radius: 5px;\n"
                                      "    padding: 8px 10px; /* Adjust the padding for the pop-up effect */\n"
                                      "    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2); /* Add a box shadow for the pop-up effect */\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover{\n"
                                      "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 150, 190, 200), stop:1 rgba(85, 98, 112, 226));\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed{\n"
                                      "    padding-left: 8px;\n"
                                      "    padding-top: 10px;\n"
                                      "    background-color: rgba(105, 118, 132, 200);\n"
                                      "    box-shadow: none; /* Remove the box shadow when pressed */\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "QStackedWidget{    \n"
                                      "    background-color: transparent;\n"
                                      "    border-radius:15px;\n"
                                      "}\n"
                                      "\n"
                                      "#lbl_file_location {\n"
                                      "    background-color: transparent;\n"
                                      "    color: #2586be;\n"
                                      "    border-radius: 15px;\n"
                                      "    border: 2px solid #2586be;\n"
                                      "}\n"
                                      "\n"
                                      "#lineEdit_url{\n"
                                      "    background-color: transparent;\n"
                                      "    color: #2586be;\n"
                                      "    border-radius: 15px;\n"
                                      "    border: 2px solid #2586be;\n"
                                      "}")
        self.frm_inside.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_inside.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_inside.setObjectName("frm_inside")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frm_inside)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 2)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frm_header = QtWidgets.QFrame(self.frm_inside)
        self.frm_header.setMinimumSize(QtCore.QSize(0, 50))
        self.frm_header.setStyleSheet("QFrame{\n"
                                      "background-color:#0b1e3b;\n"
                                      "border-radius:15px;\n"
                                      "}\n"
                                      "QPushButton{\n"
                                      "    background-color: transparent;\n"
                                      "    color:rgba(255, 255, 255, 210);\n"
                                      "    border-radius:5px;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
                                      "}\n"
                                      "QPushButton:pressed{\n"
                                      "    padding-left:5px;\n"
                                      "    padding-top:5px;\n"
                                      "    background-color:rgba(105, 118, 132, 200);\n"
                                      "}")
        self.frm_header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_header.setObjectName("frm_header")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frm_header)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frm_contact_info = QtWidgets.QFrame(self.frm_header)
        self.frm_contact_info.setStyleSheet("")
        self.frm_contact_info.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_contact_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_contact_info.setObjectName("frm_contact_info")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frm_contact_info)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_github = QtWidgets.QPushButton(self.frm_contact_info)
        self.btn_github.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_github.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/github.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_github.setIcon(icon)
        self.btn_github.setIconSize(QtCore.QSize(40, 40))
        self.btn_github.setObjectName("btn_github")
        self.horizontalLayout_3.addWidget(self.btn_github)
        self.btn_linkedin = QtWidgets.QPushButton(self.frm_contact_info)
        self.btn_linkedin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_linkedin.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icons/linkedin.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_linkedin.setIcon(icon1)
        self.btn_linkedin.setIconSize(QtCore.QSize(40, 40))
        self.btn_linkedin.setObjectName("btn_linkedin")
        self.horizontalLayout_3.addWidget(self.btn_linkedin)
        self.btn_cv = QtWidgets.QPushButton(self.frm_contact_info)
        self.btn_cv.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cv.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Icons/paperclip.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cv.setIcon(icon2)
        self.btn_cv.setIconSize(QtCore.QSize(40, 40))
        self.btn_cv.setObjectName("btn_cv")
        self.horizontalLayout_3.addWidget(self.btn_cv)
        self.btn_email = QtWidgets.QPushButton(self.frm_contact_info)
        self.btn_email.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_email.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Icons/mail.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_email.setIcon(icon3)
        self.btn_email.setIconSize(QtCore.QSize(40, 40))
        self.btn_email.setObjectName("btn_email")
        self.horizontalLayout_3.addWidget(self.btn_email)
        self.horizontalLayout.addWidget(self.frm_contact_info, 0, QtCore.Qt.AlignLeft)
        self.frm_top_right = QtWidgets.QFrame(self.frm_header)
        self.frm_top_right.setStyleSheet("")
        self.frm_top_right.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_top_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_top_right.setObjectName("frm_top_right")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frm_top_right)
        self.horizontalLayout_2.setContentsMargins(2, 0, 2, 0)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_minimize = QtWidgets.QPushButton(self.frm_top_right)
        self.btn_minimize.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_minimize.setStyleSheet("")
        self.btn_minimize.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Icons/chevron-down.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_minimize.setIcon(icon4)
        self.btn_minimize.setIconSize(QtCore.QSize(40, 40))
        self.btn_minimize.setObjectName("btn_minimize")
        self.horizontalLayout_2.addWidget(self.btn_minimize)
        self.btn_close = QtWidgets.QPushButton(self.frm_top_right)
        self.btn_close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_close.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Icons/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_close.setIcon(icon5)
        self.btn_close.setIconSize(QtCore.QSize(40, 40))
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout_2.addWidget(self.btn_close)
        self.horizontalLayout.addWidget(self.frm_top_right, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_4.addWidget(self.frm_header)
        self.pages = QtWidgets.QStackedWidget(self.frm_inside)
        self.pages.setStyleSheet("QPushButton#btn_download,\n"
                                 "QPushButton#btn_info_return {\n"
                                 "    background-color: #0b1e3b;\n"
                                 "    color: #2596be;\n"
                                 "    border-radius: 5px;\n"
                                 "    padding: 8px 10px;\n"
                                 "    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton#btn_download:hover,\n"
                                 "QPushButton#btn_info_return:hover {\n"
                                 "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(37, 150, 190, 200), stop:1 rgba(85, 98, 112, 226));\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton#btn_download:pressed,\n"
                                 "QPushButton#btn_info_return:pressed {\n"
                                 "    padding-left: 8px;\n"
                                 "    padding-top: 10px;\n"
                                 "    background-color: rgba(105, 118, 132, 200);\n"
                                 "    box-shadow: none;\n"
                                 "}\n"
                                 "\n"
                                 "QRadioButton#rb_360p,\n"
                                 "QRadioButton#rb_480p,\n"
                                 "QRadioButton#rb_720p,\n"
                                 "QRadioButton#rb_1080p,\n"
                                 "QRadioButton#rb_1440p,\n"
                                 "QRadioButton#rb_2160p {\n"
                                 "    background-color: transparent;\n"
                                 "    color: #2596be;\n"
                                 "}\n"
                                 "")
        self.pages.setObjectName("pages")
        self.page_download = QtWidgets.QWidget()
        self.page_download.setObjectName("page_download")
        self.lbl_file_location = QtWidgets.QLabel(self.page_download)
        self.lbl_file_location.setGeometry(QtCore.QRect(20, 100, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_file_location.setFont(font)
        self.lbl_file_location.setStyleSheet("")
        self.lbl_file_location.setWordWrap(False)
        self.lbl_file_location.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.lbl_file_location.setObjectName("lbl_file_location")
        self.btn_file_location = QtWidgets.QPushButton(self.page_download)
        self.btn_file_location.setGeometry(QtCore.QRect(385, 94, 50, 50))
        self.btn_file_location.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_file_location.setStyleSheet("")
        self.btn_file_location.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Icons/folder.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_file_location.setIcon(icon6)
        self.btn_file_location.setIconSize(QtCore.QSize(50, 50))
        self.btn_file_location.setObjectName("btn_file_location")
        self.btn_download = QtWidgets.QPushButton(self.page_download)
        self.btn_download.setGeometry(QtCore.QRect(230, 153, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_download.setFont(font)
        self.btn_download.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_download.setStyleSheet("")
        self.btn_download.setObjectName("btn_download")
        self.btn_url = QtWidgets.QPushButton(self.page_download)
        self.btn_url.setGeometry(QtCore.QRect(385, 34, 50, 50))
        self.btn_url.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_url.setStyleSheet("")
        self.btn_url.setText("")
        self.btn_url.setIcon(icon2)
        self.btn_url.setIconSize(QtCore.QSize(50, 50))
        self.btn_url.setObjectName("btn_url")
        self.lineEdit_url = QtWidgets.QLineEdit(self.page_download)
        self.lineEdit_url.setGeometry(QtCore.QRect(20, 40, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_url.setFont(font)
        self.lineEdit_url.setObjectName("lineEdit_url")
        self.frm_rb = QtWidgets.QFrame(self.page_download)
        self.frm_rb.setGeometry(QtCore.QRect(20, 150, 141, 71))
        self.frm_rb.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_rb.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_rb.setObjectName("frm_rb")
        self.formLayout = QtWidgets.QFormLayout(self.frm_rb)
        self.formLayout.setObjectName("formLayout")
        self.rb_360p = QtWidgets.QRadioButton(self.frm_rb)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.rb_360p.setFont(font)
        self.rb_360p.setChecked(True)
        self.rb_360p.setObjectName("rb_360p")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.rb_360p)
        self.rb_1080p = QtWidgets.QRadioButton(self.frm_rb)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.rb_1080p.setFont(font)
        self.rb_1080p.setObjectName("rb_1080p")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.rb_1080p)
        self.rb_480p = QtWidgets.QRadioButton(self.frm_rb)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.rb_480p.setFont(font)
        self.rb_480p.setObjectName("rb_480p")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.rb_480p)
        self.rb_1440p = QtWidgets.QRadioButton(self.frm_rb)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.rb_1440p.setFont(font)
        self.rb_1440p.setObjectName("rb_1440p")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.rb_1440p)
        self.rb_720p = QtWidgets.QRadioButton(self.frm_rb)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.rb_720p.setFont(font)
        self.rb_720p.setObjectName("rb_720p")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.rb_720p)
        self.rb_2160p = QtWidgets.QRadioButton(self.frm_rb)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.rb_2160p.setFont(font)
        self.rb_2160p.setObjectName("rb_2160p")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.rb_2160p)
        self.pages.addWidget(self.page_download)
        self.page_info = QtWidgets.QWidget()
        self.page_info.setObjectName("page_info")
        self.lbl_info_message = QtWidgets.QLabel(self.page_info)
        self.lbl_info_message.setGeometry(QtCore.QRect(92, 90, 261, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_info_message.setFont(font)
        self.lbl_info_message.setStyleSheet("background-color:transparent;\n"
                                            "color: #2586be;\n"
                                            "border-radius:15px;\n"
                                            "\n"
                                            "")
        self.lbl_info_message.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_info_message.setWordWrap(True)
        self.lbl_info_message.setObjectName("lbl_info_message")
        self.btn_info_return = QtWidgets.QPushButton(self.page_info)
        self.btn_info_return.setGeometry(QtCore.QRect(153, 170, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_info_return.setFont(font)
        self.btn_info_return.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_info_return.setStyleSheet("")
        self.btn_info_return.setObjectName("btn_info_return")
        self.lbl_icon_success = QtWidgets.QLabel(self.page_info)
        self.lbl_icon_success.setGeometry(QtCore.QRect(187, 10, 71, 71))
        self.lbl_icon_success.setText("")
        self.lbl_icon_success.setPixmap(QtGui.QPixmap(":/Icons/arrow-down-circle.svg"))
        self.lbl_icon_success.setScaledContents(True)
        self.lbl_icon_success.setObjectName("lbl_icon_success")
        self.pages.addWidget(self.page_info)
        self.verticalLayout_4.addWidget(self.pages)
        self.verticalLayout_2.addWidget(self.frm_inside)
        self.verticalLayout_3.addWidget(self.frm_middle)

        self.retranslateUi(Form)
        self.pages.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lbl_file_location.setText(_translate("Form", "Select File Location"))
        self.btn_download.setText(_translate("Form", "DOWNLOAD"))
        self.lineEdit_url.setPlaceholderText("Enter URL...")
        self.rb_360p.setText(_translate("Form", "360 P"))
        self.rb_1080p.setText(_translate("Form", "1080 P"))
        self.rb_480p.setText(_translate("Form", "480 P"))
        self.rb_1440p.setText(_translate("Form", "1440 P"))
        self.rb_720p.setText(_translate("Form", "720 P"))
        self.rb_2160p.setText(_translate("Form", "2160 P"))
        self.lbl_info_message.setText(
            _translate("Form", "Initializing Download"))
        self.btn_info_return.setText(_translate("Form", "RETURN"))
