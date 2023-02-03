#!/usr/bin/python

import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar,
)

# from Config_Tab import Config

WINDOW_SIZE = 1024 #???

class Window(QMainWindow):
   
   def __init__(self):
      super().__init__(parent=None)
      self.setWindowTitle("QMainWindow")
      self.setFixedSize(1024, WINDOW_SIZE)
      self.setCentralWidget(QLabel("I'm the Central Widget"))
      #   self._createMenu()
      self._createToolBar()
      self._createStatusBar()

   def _createMenu(self):
      menu = self.menuBar().addMenu("&Menu")
      menu.addAction("&Exit", self.close)

   def _createToolBar(self):
      tools = QToolBar()
      tools.addAction("Exit", self.close)
      self.addToolBar(tools)

      button = QAction("Button #1", self)
      button.setStatusTip("The first button that can be pressed")
      button.triggered.connect(self.toolBarButtonClicked)
      button.setCheckable(True)
      tools.addAction(button)


   def _createStatusBar(self):
      status = QStatusBar()
      #   status.showMessage("I'm the Status Bar")
      self.setStatusBar(status)

   def toolBarButtonClicked(self, s):
      print("[DEBUG] Toolbar button clicked, ", s)

if __name__ == "__main__":
   app = QApplication([])
   window = Window()
   window.show()
   sys.exit(app.exec())