# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:/GIT/nodes/PyFlow/CodeEditor_ui.ui'
#
# Created: Sun Mar 11 18:19:06 2018
#      by: pyside2-uic 2.0.0 running on PySide2 5.6.0~a1
#
# WARNING! All changes made in this file will be lost!

from Qt import QtCompat, QtCore, QtGui, QtWidgets

class Ui_CodeEditorWidget(object):
    def setupUi(self, CodeEditorWidget):
        CodeEditorWidget.setObjectName("CodeEditorWidget")
        CodeEditorWidget.resize(889, 512)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/resources/py.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CodeEditorWidget.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(CodeEditorWidget)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.leLabel = QtWidgets.QLineEdit(CodeEditorWidget)
        self.leLabel.setObjectName("leLabel")
        self.verticalLayout.addWidget(self.leLabel)
        self.tabWidget = QtWidgets.QTabWidget(CodeEditorWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabPins = QtWidgets.QWidget()
        self.tabPins.setObjectName("tabPins")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tabPins)
        self.gridLayout_3.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pbAddInput = QtWidgets.QPushButton(self.tabPins)
        self.pbAddInput.setObjectName("pbAddInput")
        self.gridLayout_2.addWidget(self.pbAddInput, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 3, 1, 1)
        self.pbAddOutput = QtWidgets.QPushButton(self.tabPins)
        self.pbAddOutput.setObjectName("pbAddOutput")
        self.gridLayout_2.addWidget(self.pbAddOutput, 0, 4, 1, 1)
        self.pbKillSelectedItems = QtWidgets.QPushButton(self.tabPins)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/resources/delete_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbKillSelectedItems.setIcon(icon1)
        self.pbKillSelectedItems.setObjectName("pbKillSelectedItems")
        self.gridLayout_2.addWidget(self.pbKillSelectedItems, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.tabPins)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 436, 392))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_5.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.lwInputs = QtWidgets.QListWidget(self.scrollAreaWidgetContents)
        self.lwInputs.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.lwInputs.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.lwInputs.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.lwInputs.setUniformItemSizes(False)
        self.lwInputs.setSelectionRectVisible(True)
        self.lwInputs.setObjectName("lwInputs")
        self.gridLayout_5.addWidget(self.lwInputs, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.addWidget(self.scrollArea)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.tabPins)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 435, 392))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_4.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lwOutputs = QtWidgets.QListWidget(self.scrollAreaWidgetContents_2)
        self.lwOutputs.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.lwOutputs.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.lwOutputs.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.lwOutputs.setSelectionRectVisible(True)
        self.lwOutputs.setObjectName("lwOutputs")
        self.gridLayout_4.addWidget(self.lwOutputs, 0, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_3.addWidget(self.scrollArea_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tabPins, "")
        self.tabCode = QtWidgets.QWidget()
        self.tabCode.setObjectName("tabCode")
        self.gridLayout = QtWidgets.QGridLayout(self.tabCode)
        self.gridLayout.setContentsMargins(1, 1, 1, 1)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget.addTab(self.tabCode, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pbReset = QtWidgets.QPushButton(CodeEditorWidget)
        self.pbReset.setObjectName("pbReset")
        self.horizontalLayout_4.addWidget(self.pbReset)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.pbSave = QtWidgets.QPushButton(CodeEditorWidget)
        self.pbSave.setMaximumSize(QtCore.QSize(45, 16777215))
        self.pbSave.setObjectName("pbSave")
        self.horizontalLayout_4.addWidget(self.pbSave)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.sbFontSize = QtWidgets.QSpinBox(CodeEditorWidget)
        self.sbFontSize.setProperty("value", 10)
        self.sbFontSize.setObjectName("sbFontSize")
        self.horizontalLayout_2.addWidget(self.sbFontSize)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(CodeEditorWidget)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(CodeEditorWidget)

    def retranslateUi(self, CodeEditorWidget):
        CodeEditorWidget.setWindowTitle(QtCompat.translate("CodeEditorWidget", "Python node editor", None, -1))
        self.leLabel.setText(QtCompat.translate("CodeEditorWidget", "PythonNode", None, -1))
        self.leLabel.setPlaceholderText(QtCompat.translate("CodeEditorWidget", "Node label...", None, -1))
        self.pbAddInput.setText(QtCompat.translate("CodeEditorWidget", "add input", None, -1))
        self.pbAddOutput.setText(QtCompat.translate("CodeEditorWidget", "add output", None, -1))
        self.pbKillSelectedItems.setText(QtCompat.translate("CodeEditorWidget", "kill selected pins", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPins), QtCompat.translate("CodeEditorWidget", "Pins", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCode), QtCompat.translate("CodeEditorWidget", "Code", None, -1))
        self.pbReset.setText(QtCompat.translate("CodeEditorWidget", "reset", None, -1))
        self.pbSave.setText(QtCompat.translate("CodeEditorWidget", "save", None, -1))

from .. import nodes_res_rc
if __name__ == '__main__':
    from Qt.QtWidgets import QApplication,QStyleFactory
    import sys



    app = QApplication(sys.argv)

    app.setStyle(QStyleFactory.create("plastique"))
    wm = QtWidgets.QDialog()
    w = Ui_CodeEditorWidget()
    w.setupUi(wm)
    wm.show()

    sys.exit(app.exec_())