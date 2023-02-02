#!/usr/bin/python

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import pyqtSlot

def window():
   
   app = QApplication(sys.argv)

   # Create a Qt widget, which will be our window.
   window = QWidget()
   window.show()  # IMPORTANT!!!!! Windows are hidden by default.

   # Start the event loop.
   app.exec()

if __name__ == '__main__':
   window()