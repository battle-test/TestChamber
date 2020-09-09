from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(655, 500)
        MainWindow.setMinimumSize(QtCore.QSize(655, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/Wizard.ico"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QWidget#frmLogin,QWidget#frmPopup,QWidget#frmHostInfo,QWidget#frmLogout,QWidget#frmConfig,QWidget#frmData,QWidget#frmDefence,QWidget#frmHost,QWidget#frmMain,QWidget#frmPwd,QWidget#frmSelect,QWidget#frmMessageBox{\n"
"    border:1px solid #1B89CA;\n"
"    border-radius:1px;    \n"
"}\n"
"\n"
".QFrame{\n"
"    border:1px solid #5CACEE;\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QWidget#widget_title{\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #1B89CA, stop:1 #1077B5);\n"
"}\n"
"\n"
"QLabel#lab_Ico,QLabel#lab_Title{\n"
"    border-radius:0px;\n"
"    color: #F0F0F0;\n"
"    background-color:rgba(0,0,0,0);\n"
"    border-style:none;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: 1px solid #5CACEE;\n"
"    border-radius: 5px;\n"
"    padding: 2px;\n"
"    background: none;\n"
"    selection-background-color: #1B89CA;\n"
"}\n"
"\n"
"QLineEdit[echoMode=\"2\"] { \n"
"    lineedit-password-character: 9679; \n"
"}\n"
".QPushButton{\n"
"    border-style: none;\n"
"    border: 5px;\n"
"    color: #F0F0F0;\n"
"    padding: 5px;    \n"
"    min-height: 20px;\n"
"    border-radius:5px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #1B89CA, stop:1 #1077B5); \n"
"}\n"
"\n"
".QPushButton[focusPolicy=\"0\"] {\n"
"    border-style: none;\n"
"    border: 0px;\n"
"    color: #F0F0F0;\n"
"    padding: 0px;    \n"
"    min-height: 10px;\n"
"    border-radius:3px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #1B89CA, stop:1 #1077B5); \n"
"}\n"
"\n"
".QPushButton:hover{ \n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #5CACEE, stop:1 #4F94CD);\n"
"}\n"
"\n"
".QPushButton:pressed{ \n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #1B89CA, stop:1 #1077B5);\n"
"}\n"
"\n"
"QPushButton#btnMenu,QPushButton#btnMenu_Min,QPushButton#btnMenu_Max,QPushButton#btnMenu_Close{\n"
"    border-radius:0px;\n"
"    color: #F0F0F0;\n"
"    background-color:rgba(0,0,0,0);\n"
"    border-style:none;\n"
"}\n"
"\n"
"QPushButton#btnMenu:hover,QPushButton#btnMenu_Min:hover,QPushButton#btnMenu_Max:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(25, 134, 199, 0), stop:1 #5CACEE);\n"
"}\n"
"\n"
"QPushButton#btnMenu_Close:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(238, 0, 0, 128), stop:1 rgba(238, 44, 44, 255));\n"
"}\n"
"\n"
"QCheckBox {\n"
"    spacing: 2px; \n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QComboBox,QDateEdit{\n"
"    border-radius: 3px;\n"
"    padding: 1px 10px 1px 5px;\n"
"    border: 1px solid #5CACEE;\n"
"}\n"
"QComboBox::drop-down,QDateEdit::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px; \n"
"    border-left-width: 1px;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    border-left-color: #5CACEE;\n"
"}\n"
"QMenu {\n"
"    background-color:#F0F0F0;\n"
"    margin: 2px;\n"
"}\n"
"\n"
"QMenu::item {    \n"
"    padding: 2px 12px 2px 12px;\n"
"}\n"
"\n"
"QMenu::indicator {\n"
"    width: 13px;\n"
"    height: 13px;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    color: #FFFFFF;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #1B89CA, stop:1 #1077B5); \n"
"}\n"
"\n"
"QMenu::separator {\n"
"    height: 1px;\n"
"    background: #5CACEE;\n"
"}\n"
"\n"
"QProgressBar {\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    border: 1px solid #5CACEE;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    width: 5px; \n"
"    margin: 0.5px;\n"
"    background-color: #1B89CA;\n"
"}\n"
"QHeaderView::section {\n"
"    padding:3px;\n"
"    margin:0px;\n"
"    color:#F0F0F0;\n"
"    border: 1px solid #F0F0F0;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #5CACEE, stop:1 #4F94CD);\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border-top-left-radius:5px;\n"
"    border-top-right-radius:5px;\n"
"    border-bottom-left-radius:5px;\n"
"    border-bottom-right-radius:5px;\n"
"    color: #F0F0F0;\n"
"    min-width: 60px;\n"
"    min-height: 20px;\n"
"    padding: 3px 8px 3px 8px;\n"
"    margin:1px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #5CACEE, stop:1 #4F94CD); \n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #1B89CA, stop:1 #1077B5); \n"
"    \n"
"}\n"
"\n"
"QStatusBar::item {\n"
"     border: 1px solid #5CACEE;\n"
"     border-radius: 3px;\n"
"}")

        # Init mainFrame
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.verticalLayout_centralwidget = QtWidgets.QVBoxLayout(self.centralwidget)

        # init frame_openFile
        self.frame_openFile = QtWidgets.QFrame(self.centralwidget)
        # Init openFile
        self.frame_openFile_pushButton = QtWidgets.QPushButton(self.frame_openFile)
        self.frame_openFile_lineEdit = QtWidgets.QLineEdit(self.frame_openFile)
        self.frame_openFile_lineEdit.setReadOnly(True)
        # Init typeSepFieldField
        self.frame_openFile_comboBox_typeSepField = QtWidgets.QComboBox(self.frame_openFile)
        self.frame_openFile_comboBox_typeSepField.addItem("\\t")
        self.frame_openFile_comboBox_typeSepField.addItem(";")
        self.frame_openFile_label_typeSepField = QtWidgets.QLabel(self.frame_openFile)
        # Init typeEncoding
        self.frame_openFile_label_typeEncoding = QtWidgets.QLabel(self.frame_openFile)
        self.frame_openFile_comboBox_typeEncoding = QtWidgets.QComboBox(self.frame_openFile)
        self.frame_openFile_comboBox_typeEncoding.addItem("utf-8")
        self.frame_openFile_comboBox_typeEncoding.addItem("mbcs")
        # Init device
        self.frame_openFile_label_device = QtWidgets.QLabel(self.frame_openFile)
        self.frame_openFile_comboBox_device = QtWidgets.QComboBox(self.frame_openFile)
        self.frame_openFile_comboBox_device.addItem("МИТ")
        self.frame_openFile_comboBox_device.addItem("Rotronic")
        # Init typeDecimal
        self.frame_openFile_label_typeDecimal = QtWidgets.QLabel(self.frame_openFile)
        self.frame_openFile_comboBox_typeDecimal = QtWidgets.QComboBox(self.frame_openFile)
        self.frame_openFile_comboBox_typeDecimal.addItem(",")
        self.frame_openFile_comboBox_typeDecimal.addItem(".")
        # Init QtySensors
        self.frame_openFile_label_qtySensors = QtWidgets.QLabel(self.frame_openFile)
        self.frame_openFile_comboBox_qtySensors = QtWidgets.QComboBox(self.frame_openFile)
        self.frame_openFile_comboBox_qtySensors.addItem("9")
        self.frame_openFile_comboBox_qtySensors.addItem("15")
        # layout policy in frame_openFile
        spacer_item = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_centralwidget.addWidget(self.frame_openFile)
        self.gridLayout_frame_openFile = QtWidgets.QGridLayout(self.frame_openFile)
        self.gridLayout_frame_openFile.addWidget(self.frame_openFile_pushButton, 0, 0, 1, 1)
        self.gridLayout_frame_openFile.addWidget(self.frame_openFile_lineEdit, 0, 1, 1, 6)
        self.gridLayout_frame_openFile.addWidget(self.frame_openFile_label_typeSepField, 1, 2, 1, 1)
        self.gridLayout_frame_openFile.addWidget(self.frame_openFile_comboBox_typeSepField, 1, 3, 1, 1)
        self.gridLayout_frame_openFile.addWidget(self.frame_openFile_label_typeEncoding, 1, 4, 1, 1)
        self.gridLayout_frame_openFile.addWidget(self.frame_openFile_comboBox_typeEncoding, 1, 5, 1, 1)
        self.gridLayout_frame_openFile.addWidget(self.frame_openFile_label_device, 1, 0, 1, 1)
        self.gridLayout_frame_openFile.addWidget(self.frame_openFile_comboBox_device, 1, 1, 1, 1)
        self.gridLayout_frame_openFile.addWidget(self.frame_openFile_label_typeDecimal, 2, 2, 1, 1)
        self.gridLayout_frame_openFile.addWidget(self.frame_openFile_comboBox_typeDecimal, 2, 3, 1, 1)
        self.gridLayout_frame_openFile.addWidget(self.frame_openFile_label_qtySensors, 2, 4, 1, 1)
        self.gridLayout_frame_openFile.addWidget(self.frame_openFile_comboBox_qtySensors, 2, 5 ,1, 1)
        self.gridLayout_frame_openFile.addItem(spacer_item, 1, 6, 1, 1)

        # Init frame_temp
        self.frame_temp = QtWidgets.QFrame(self.centralwidget)
        spacer_item1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # Init temp in frame_temp
        self.frame_temp_label_textTemp = QtWidgets.QLabel(self.frame_temp)
        self.frame_temp_label_value1 = QtWidgets.QLabel(self.frame_temp)
        self.frame_temp_label_value2 = QtWidgets.QLabel(self.frame_temp)
        self.frame_temp_label_value3 = QtWidgets.QLabel(self.frame_temp)
        self.frame_temp_label_value4 = QtWidgets.QLabel(self.frame_temp)
        self.frame_temp_label_value5 = QtWidgets.QLabel(self.frame_temp)
        self.frame_temp_label_value6 = QtWidgets.QLabel(self.frame_temp)
        self.frame_temp_label_value7 = QtWidgets.QLabel(self.frame_temp)
        self.frame_temp_label_value8 = QtWidgets.QLabel(self.frame_temp)
        self.frame_temp_lineEdit_temp1 = QtWidgets.QLineEdit(self.frame_temp)
        self.frame_temp_lineEdit_temp2 = QtWidgets.QLineEdit(self.frame_temp)
        self.frame_temp_lineEdit_temp3 = QtWidgets.QLineEdit(self.frame_temp)
        self.frame_temp_lineEdit_temp4 = QtWidgets.QLineEdit(self.frame_temp)
        self.frame_temp_lineEdit_temp5 = QtWidgets.QLineEdit(self.frame_temp)
        self.frame_temp_lineEdit_temp6 = QtWidgets.QLineEdit(self.frame_temp)
        self.frame_temp_lineEdit_temp7 = QtWidgets.QLineEdit(self.frame_temp)
        self.frame_temp_lineEdit_temp8 = QtWidgets.QLineEdit(self.frame_temp)
        # Layout policy in frame_temp
        self.verticalLayout_centralwidget.addWidget(self.frame_temp)
        self.gridLayout_frame_temp = QtWidgets.QGridLayout(self.frame_temp)
        self.gridLayout_frame_temp.addWidget(self.frame_temp_label_value1, 0, 1, 1, 1)
        self.gridLayout_frame_temp.addWidget(self.frame_temp_label_value2, 0, 2, 1, 1)
        self.gridLayout_frame_temp.addWidget(self.frame_temp_label_value3, 0, 3, 1, 1)
        self.gridLayout_frame_temp.addWidget(self.frame_temp_label_value5, 0, 5, 1, 1)
        self.gridLayout_frame_temp.addWidget(self.frame_temp_label_value4, 0, 4, 1, 1)
        self.gridLayout_frame_temp.addWidget(self.frame_temp_label_value6, 0, 6, 1, 1)
        self.gridLayout_frame_temp.addWidget(self.frame_temp_label_value7, 0, 7, 1, 1)
        self.gridLayout_frame_temp.addWidget(self.frame_temp_label_value8, 0, 8, 1, 1)
        self.gridLayout_frame_temp.addWidget(self.frame_temp_label_textTemp, 1, 0, 1, 1)
        self.gridLayout_frame_temp.addWidget(self.frame_temp_lineEdit_temp1, 1, 1, 1, 1)
        self.gridLayout_frame_temp.addWidget(self.frame_temp_lineEdit_temp2, 1, 2, 1, 1)
        self.gridLayout_frame_temp.addWidget(self.frame_temp_lineEdit_temp3, 1, 3, 1, 1)
        self.gridLayout_frame_temp.addWidget(self.frame_temp_lineEdit_temp4, 1, 4, 1, 1)
        self.gridLayout_frame_temp.addWidget(self.frame_temp_lineEdit_temp5, 1, 5, 1, 1)
        self.gridLayout_frame_temp.addWidget(self.frame_temp_lineEdit_temp6, 1, 6, 1, 1)
        self.gridLayout_frame_temp.addWidget(self.frame_temp_lineEdit_temp7, 1, 7, 1, 1)
        self.gridLayout_frame_temp.addWidget(self.frame_temp_lineEdit_temp8, 1, 8, 1, 1)
        self.gridLayout_frame_temp.addItem(spacer_item1, 1, 9, 1, 1)

        # Init frame_hum
        self.frame_hum = QtWidgets.QFrame(self.centralwidget)
        self.frame_hum_label_humText = QtWidgets.QLabel(self.frame_hum)
        # Init hum and temp in frame_hum
        self.frame_hum_label_value1 = QtWidgets.QLabel(self.frame_hum)
        self.frame_hum_label_value2 = QtWidgets.QLabel(self.frame_hum)
        self.frame_hum_label_value3 = QtWidgets.QLabel(self.frame_hum)
        self.frame_hum_label_value4 = QtWidgets.QLabel(self.frame_hum)
        self.frame_hum_label_value5 = QtWidgets.QLabel(self.frame_hum)
        self.frame_hum_lineEdit_hum1 = QtWidgets.QLineEdit(self.frame_hum)
        self.frame_hum_lineEdit_hum2 = QtWidgets.QLineEdit(self.frame_hum)
        self.frame_hum_lineEdit_hum3 = QtWidgets.QLineEdit(self.frame_hum)
        self.frame_hum_lineEdit_hum4 = QtWidgets.QLineEdit(self.frame_hum)
        self.frame_hum_lineEdit_hum5 = QtWidgets.QLineEdit(self.frame_hum)
        self.frame_hum_label_valueText = QtWidgets.QLabel(self.frame_hum)
        self.frame_hum_lineEdit_temp1 = QtWidgets.QLineEdit(self.frame_hum)
        self.frame_hum_lineEdit_temp2 = QtWidgets.QLineEdit(self.frame_hum)
        self.frame_hum_lineEdit_temp5 = QtWidgets.QLineEdit(self.frame_hum)
        self.frame_hum_lineEdit_temp4 = QtWidgets.QLineEdit(self.frame_hum)
        self.frame_hum_lineEdit_temp3 = QtWidgets.QLineEdit(self.frame_hum)
        self.verticalLayout_centralwidget.addWidget(self.frame_hum)
        spacer_item2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_frame_hum = QtWidgets.QGridLayout(self.frame_hum)
        self.gridLayout_frame_hum.addWidget(self.frame_hum_label_value1, 0, 1, 1, 1)
        self.gridLayout_frame_hum.addWidget(self.frame_hum_label_value2, 0, 2, 1, 1)
        self.gridLayout_frame_hum.addWidget(self.frame_hum_label_value3, 0, 3, 1, 1)
        self.gridLayout_frame_hum.addWidget(self.frame_hum_label_value4, 0, 4, 1, 1)
        self.gridLayout_frame_hum.addWidget(self.frame_hum_label_value5, 0, 5, 1, 1)
        self.gridLayout_frame_hum.addWidget(self.frame_hum_label_humText, 1, 0, 1, 1)
        self.gridLayout_frame_hum.addWidget(self.frame_hum_lineEdit_hum1, 1, 1, 1, 1)
        self.gridLayout_frame_hum.addWidget(self.frame_hum_lineEdit_hum2, 1, 2, 1, 1)
        self.gridLayout_frame_hum.addWidget(self.frame_hum_lineEdit_hum3, 1, 3, 1, 1)
        self.gridLayout_frame_hum.addWidget(self.frame_hum_lineEdit_hum4, 1, 4, 1, 1)
        self.gridLayout_frame_hum.addWidget(self.frame_hum_lineEdit_hum5, 1, 5, 1, 1)
        self.gridLayout_frame_hum.addWidget(self.frame_hum_label_valueText, 2, 0, 1, 1)
        self.gridLayout_frame_hum.addWidget(self.frame_hum_lineEdit_temp1, 2, 1, 1, 1)
        self.gridLayout_frame_hum.addWidget(self.frame_hum_lineEdit_temp2, 2, 2, 1, 1)
        self.gridLayout_frame_hum.addWidget(self.frame_hum_lineEdit_temp3, 2, 3, 1, 1)
        self.gridLayout_frame_hum.addWidget(self.frame_hum_lineEdit_temp4, 2, 4, 1, 1)
        self.gridLayout_frame_hum.addWidget(self.frame_hum_lineEdit_temp5, 2, 5, 1, 1)
        self.gridLayout_frame_hum.addItem(spacer_item2, 0, 6, 1, 1)

        # Init frame_optionFile
        self.frame_optionFile = QtWidgets.QFrame(self.centralwidget)
        self.frame_optionFile_pushButton_modForm = QtWidgets.QPushButton(self.frame_optionFile)
        self.frame_optionFile_label_infoAboutForm = QtWidgets.QLabel(self.frame_optionFile)
        self.frame_optionFile_checkBox_deleteSheetTemp = QtWidgets.QCheckBox(self.frame_optionFile)
        self.frame_optionFile_checkBox_deleteSheetTemp.setChecked(True)
        self.frame_optionFile_checkBox_deleteSheetHum = QtWidgets.QCheckBox(self.frame_optionFile)
        self.frame_optionFile_checkBox_deleteSheetHum.setChecked(True)
        self.frame_optionFile_saveProtocol = QtWidgets.QPushButton(self.frame_optionFile)
        self.frame_optionFile_reset = QtWidgets.QPushButton(self.frame_optionFile)
        self.verticalLayout_centralwidget.addWidget(self.frame_optionFile)
        self.gridLayout_frame_saveFile = QtWidgets.QGridLayout(self.frame_optionFile)
        self.gridLayout_frame_saveFile.addWidget(self.frame_optionFile_pushButton_modForm, 1, 0, 1, 1)
        self.gridLayout_frame_saveFile.addWidget(self.frame_optionFile_checkBox_deleteSheetTemp, 1, 1, 1, 1)
        self.gridLayout_frame_saveFile.addWidget(self.frame_optionFile_label_infoAboutForm, 2, 0, 1, 1)
        self.gridLayout_frame_saveFile.addWidget(self.frame_optionFile_checkBox_deleteSheetHum, 2, 1, 1, 1)
        self.gridLayout_frame_saveFile.addWidget(self.frame_optionFile_saveProtocol, 3, 0, 1, 2)
        self.gridLayout_frame_saveFile.addWidget(self.frame_optionFile_reset, 4, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        # Init setTabOrder
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.frame_temp_lineEdit_temp1, self.frame_temp_lineEdit_temp2)
        MainWindow.setTabOrder(self.frame_temp_lineEdit_temp2, self.frame_temp_lineEdit_temp3)
        MainWindow.setTabOrder(self.frame_temp_lineEdit_temp3, self.frame_temp_lineEdit_temp4)
        MainWindow.setTabOrder(self.frame_temp_lineEdit_temp4, self.frame_temp_lineEdit_temp5)
        MainWindow.setTabOrder(self.frame_temp_lineEdit_temp5, self.frame_temp_lineEdit_temp6)
        MainWindow.setTabOrder(self.frame_temp_lineEdit_temp6, self.frame_temp_lineEdit_temp7)
        MainWindow.setTabOrder(self.frame_temp_lineEdit_temp7, self.frame_temp_lineEdit_temp8)
        MainWindow.setTabOrder(self.frame_temp_lineEdit_temp8, self.frame_hum_lineEdit_hum1)
        MainWindow.setTabOrder(self.frame_hum_lineEdit_hum1, self.frame_hum_lineEdit_hum2)
        MainWindow.setTabOrder(self.frame_hum_lineEdit_hum2, self.frame_hum_lineEdit_hum3)
        MainWindow.setTabOrder(self.frame_hum_lineEdit_hum3, self.frame_hum_lineEdit_hum4)
        MainWindow.setTabOrder(self.frame_hum_lineEdit_hum4, self.frame_hum_lineEdit_hum5)
        MainWindow.setTabOrder(self.frame_hum_lineEdit_hum5, self.frame_hum_lineEdit_temp1)
        MainWindow.setTabOrder(self.frame_hum_lineEdit_temp1, self.frame_hum_lineEdit_temp2)
        MainWindow.setTabOrder(self.frame_hum_lineEdit_temp2, self.frame_hum_lineEdit_temp3)
        MainWindow.setTabOrder(self.frame_hum_lineEdit_temp3, self.frame_hum_lineEdit_temp4)
        MainWindow.setTabOrder(self.frame_hum_lineEdit_temp4, self.frame_hum_lineEdit_temp5)


        # Init setText for everything objects
        MainWindow.setWindowTitle("Генератор протокола")
        self.frame_openFile_label_device.setText("Тип устройства:")
        self.frame_openFile_label_typeEncoding.setText("Кодировка:")
        self.frame_openFile_label_typeSepField.setText("Разделитель полей:")
        self.frame_openFile_label_typeDecimal.setText("Разделитель числа:")
        self.frame_openFile_label_qtySensors.setText("Количество датчиков:")
        self.frame_openFile_pushButton.setText("Результаты измерений")
        self.frame_temp_label_textTemp.setText("Температура:")
        self.frame_temp_label_value1.setText("№ 1")
        self.frame_temp_label_value2.setText("№ 2")
        self.frame_temp_label_value3.setText("№ 3")
        self.frame_temp_label_value4.setText("№ 4")
        self.frame_temp_label_value5.setText("№ 5")
        self.frame_temp_label_value6.setText("№ 6")
        self.frame_temp_label_value7.setText("№ 7")
        self.frame_temp_label_value8.setText("№ 8")
        self.frame_hum_label_humText.setText("Влажность:")
        self.frame_hum_label_valueText.setText("Температура:")
        self.frame_hum_label_value1.setText("№ 1")
        self.frame_hum_label_value2.setText("№ 2")
        self.frame_hum_label_value3.setText("№ 3")
        self.frame_hum_label_value4.setText("№ 4")
        self.frame_hum_label_value5.setText("№ 5")
        self.frame_optionFile_pushButton_modForm.setText("Модифицированная форма")
        self.frame_optionFile_checkBox_deleteSheetHum.setText("Удалить пустые листы с результатами измерений влажности-температура")
        self.frame_optionFile_checkBox_deleteSheetTemp.setText("Удалить пустые листы с результатами измерений температуры")
        self.frame_optionFile_label_infoAboutForm.setText(" Используеться стандартная форма")
        self.frame_optionFile_saveProtocol.setText("Сохранить протокол")
        self.frame_optionFile_reset.setText("Сброс атрибутов и значений")
        self.frame_temp_lineEdit_temp1.setText('-20')
        self.frame_temp_lineEdit_temp2.setText('10')
        self.frame_temp_lineEdit_temp3.setText('40')
        self.frame_temp_lineEdit_temp5.setText('70')
        self.frame_temp_lineEdit_temp4.setText('100')
