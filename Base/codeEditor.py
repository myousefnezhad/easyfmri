from shutil import ExecError
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

from dir import getDIR

class codeEditor():
    def __init__(self, ui=None, ObjType=None):
        self.ObjType = ObjType
        if self.ObjType == 1 or self.ObjType is None:
            try:
                import logging
                logging.basicConfig(level=logging.DEBUG)
                from pyqode.core import api
                from pyqode.core import modes
                from pyqode.core import panels
                font = QFont()
                font.setBold(True)
                font.setWeight(75)
                self.Obj = api.CodeEdit(ui.Code)
                self.Obj.backend.start(getDIR() + '/backend/server.py')
                self.Obj.modes.append(modes.CodeCompletionMode())
                self.Obj.modes.append(modes.CaretLineHighlighterMode())
                self.Obj.modes.append(modes.PygmentsSyntaxHighlighter(ui.txtCode.document()))
                self.Obj.panels.append(panels.LineNumberPanel(),api.Panel.Position.LEFT)
                self.Obj.setFont(font)
                self.ObjType = 1
                return
            except:
                self.ObjType = None
        if self.ObjType == 2 or self.ObjType is None:
            try:
                from PyQt6.Qsci import QsciScintilla, QsciLexerPython
                self.ARROW_MARKER_NUM = 8
                self.Obj = QsciScintilla()
                font = QFont()
                font.setFamily('Arial')
                font.setFixedPitch(True)
                font.setPointSize(14)
                self.Obj.setFont(font)
                self.Obj.setMarginsFont(font)
                self.Obj.setMarginLineNumbers(0, True)
                self.Obj.setMarginsBackgroundColor(QColor("#cccccc"))
                self.Obj.setMarginSensitivity(1, True)
                self.Obj.marginClicked.connect(self.on_margin_clicked)
                self.Obj.markerDefine(QsciScintilla.MarkerSymbol.RightArrow, self.ARROW_MARKER_NUM)
                self.Obj.setMarkerBackgroundColor(QColor("#ee1111"), self.ARROW_MARKER_NUM)
                self.Obj.setBraceMatching(QsciScintilla.BraceMatch.SloppyBraceMatch)
                self.Obj.setCaretLineVisible(True)
                self.Obj.setCaretLineBackgroundColor(QColor("#34e2e2"))
                lexer = QsciLexerPython()
                lexer.setDefaultFont(font)
                lexer.setDefaultPaper(QColor("#ffffff"))
                lexer.setDefaultColor(QColor("#000000"))
                self.Obj.setLexer(lexer)
                text = bytearray(str.encode("Arial"))
                self.Obj.SendScintilla(QsciScintilla.SCI_STYLESETFONT, 1, text)
                self.Obj.SendScintilla(QsciScintilla.SCI_SETHSCROLLBAR, 0)
                self.Obj.setMinimumSize(400, 400)
                self.Obj.toPlainText = self.toPlainText
                self.Obj.setPlainText = self.setPlainText
                self.ObjType = 2
            except Exception as e:
                self.ObjType = None
        if self.ObjType != 1 and self.ObjType != 2:
            self.Obj = QTextEdit()
            self.Obj.toPlainText = self.toPlainText
            self.Obj.setPlainText = self.setPlainText
            self.ObjType = 0
        print("Editor ID:", self.ObjType)

    def setText(self, text):
        if self.ObjType == 1:
            self.Obj.setPlainText(text, "", "")
        else:
            self.Obj.setText(text)
    
    def setPlainText(self, text, _a=None, _b=None):
        self.Obj.setText(text)

    def toPlainText(self):
        return self.Obj.text()

    def setObjectName(self, name):
            self.Obj.setObjectName(name)

    def on_margin_clicked(self, nmargin, nline, modifiers):
        # Toggle marker for the line the margin was clicked on
        if self.markersAtLine(nline) != 0:
            self.markerDelete(nline, self.ARROW_MARKER_NUM)
        else:
            self.markerAdd(nline, self.ARROW_MARKER_NUM)


