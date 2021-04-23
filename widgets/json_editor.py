__copyright__ = "Copyright 2020, 3Liz"
__license__ = "GPL version 3"
__email__ = "info@3liz.org"
__revision__ = "$Format:%H$"

from PyQt5.QtWidgets import QWidget
from qgis.PyQt import Qsci


class JsonEditor(Qsci.QsciScintilla):
    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent)
        self.setLexer(Qsci.QsciLexerJSON(self))
