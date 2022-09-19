# coding=utf-8

"""
Script was created by Ben Somosi.
Reach me at here for more information!
Linkedin: https://www.linkedin.com/in/bensomosi/
"""

import os
from datetime import datetime

# Python UI package imports
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

# Maya API package imports
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
import maya.cmds as cmds
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin


# Basic settings
WIDTH, HEIGHT = 400, 150
VERSION = "001"
INTRODUCTION = "<br><strong>Floood Paint r-"+ VERSION + "</strong><br><br>Select the paint map you want to smooth and floood it!<br><br>Visit my Github page for proper documentation!"
WELCOME_LINK = "https://github.com/BenceSomosi/CFX---Nucleus-Manager"


# Core of the script.
class FlooodPaintMainWindow(MayaQWidgetDockableMixin, QWidget):
    def __init__(self):
        super(FlooodPaintMainWindow, self).__init__()

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.resize(WIDTH, HEIGHT)
        self.setWindowTitle("Floood Paint r-" + str(VERSION) + "")

        self.WELCOME_LABEL = QLabel(INTRODUCTION)
        self.WELCOME_LABEL.setAlignment(Qt.AlignCenter)

        linkTemplate = '<a style="color:white;" href={0}>{1}</a>'

        self.WELCOME_LINK_LABEL = HyperlinkLabel(self)
        self.WELCOME_LINK_LABEL.setText(linkTemplate.format(WELCOME_LINK, WELCOME_LINK))

        self.LABEL_floodValue = QLabel("Amount of flooding: ")

        self.floodAmount = QLineEdit()
        self.floodAmount.setAlignment(Qt.AlignCenter)
        self.floodAmount.setText("10")
        self.onlyInt = QIntValidator()
        self.floodAmount.setValidator(self.onlyInt)

        self.floodButton = QPushButton("Flood it!")
        self.floodButton.setIconSize(QSize(20, 20))
        self.floodButton.setMinimumHeight(30)
        self.floodButton.setIcon(QIcon(":/paintBlendshape.png"))
        self.floodButton.setStyleSheet('''QPushButton { background-color: rgb(146, 172, 198); color: "black";} QToolTip { background-color: 'black'; color: 'white'; border-style:none; font-size: 12px; padding: 5px;}''')
        self.floodButton.clicked.connect(self.floodFunction)

        # Set up the layout. (self.layout)
        self.layout.addWidget(self.WELCOME_LABEL, 0, 0, 1, 20)
        self.layout.addWidget(self.WELCOME_LINK_LABEL, 1, 0, 1, 20)
        self.layout.addWidget(QLabel(""), 2, 0, 1, 20)
        self.layout.addWidget(self.LABEL_floodValue , 3,  0, 1, 1)
        self.layout.addWidget(self.floodAmount , 3,  1, 1, 18)
        self.layout.addWidget(self.floodButton , 4,  0, 1, 20)

    def floodFunction(self):
        floodVAL = int(self.floodAmount.text())

        if floodVAL > 20:
            confirm = cmds.confirmDialog(title='Confirm', message='Flood amount is BIGGER than 20.<br>Are you sure?', button=['Yes', 'No'], defaultButton='Yes',
                               cancelButton='No', dismissString='No')

            if confirm == "Yes":
                for i in range(floodVAL):
                    mel.eval('artAttrCtx -e -clear `currentCtx`;')
        else:
            for i in range(floodVAL):
                mel.eval('artAttrCtx -e -clear `currentCtx`;')

    def run(self):
        self.show(dockable = True)


class HyperlinkLabel(QLabel):
    def __init__(self, parent=None):
        super(HyperlinkLabel, self).__init__()
        self.setStyleSheet('color: yellow;')
        self.setOpenExternalLinks(True)
        self.setParent(parent)
        self.setAlignment(Qt.AlignCenter)


if __name__ == "__main__":
    a = FlooodPaintMainWindow()
    a.run()
