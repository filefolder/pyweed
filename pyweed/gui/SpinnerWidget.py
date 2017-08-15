# -*- coding: utf-8 -*-
"""
Spinner overlay to indicate that an operation is in progress.

:copyright:
    Mazama Science, IRIS
:license:
    GNU Lesser General Public License, Version 3
    (http://www.gnu.org/copyleft/lesser.html)
"""

from PyQt4 import QtGui
from logging import getLogger
from pyweed.gui.uic import SpinnerWidget

LOGGER = getLogger(__name__)


class SpinnerWidget(QtGui.QFrame, SpinnerWidget.Ui_SpinnerWidget):
    """
    Spinner overlay widget. When shown, this covers the parent window and
    plays an animated spinner graphic along with a text message.
    """
    def __init__(self, labelText, parent=None):
        super(SpinnerWidget, self).__init__(parent=parent)
        self.setupUi(self)
        self.movie = QtGui.QMovie(":qrc/rotator-32.gif")
        self.icon.setMovie(self.movie)
        self.label.setText(labelText)
        self.hide()

    def showEvent(self, *args, **kwargs):
        """
        Widget is being shown
        """
        self.setGeometry(self.parent().contentsRect())
        self.movie.start()
        return super(SpinnerWidget, self).showEvent(*args, **kwargs)

    def hideEvent(self, *args, **kwargs):
        """
        Widget is being hidden
        """
        self.movie.stop()
        return super(SpinnerWidget, self).hideEvent(*args, **kwargs)