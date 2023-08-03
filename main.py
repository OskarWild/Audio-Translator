from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi
import sys
from translate import translate_
import speech_recognition as sr


class TransWindow(QMainWindow):
    def __init__(self):
        super(TransWindow, self).__init__()
        loadUi('trans.ui', self)
        self.btn_micro.clicked.connect(self.command)
        self.btn_trans.clicked.connect(self.function)
        self.show()

    @pyqtSlot()
    def command(self):
        r = sr.Recognizer()

        with sr.Microphone() as source:
            print('Say something :')
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, 1)
            audio = r.listen(source)

            try:
                task = r.recognize_google(audio, language='en-us').lower()
                print(task)
            except sr.UnknownValueError:
                print('I cannot understand you')
                task = self.command()
            self.Edit.setText(task)

    @pyqtSlot()
    def function(self):
        from_language = self.wich_language(self.frombox.currentText())
        to_language = self.wich_language(self.tobox.currentText())

        self.result.setText(
            str(translate_(self.Edit.text(), from_language, to_language)))

    def wich_language(self, language):
        if language == 'English':
            return 'en'
        elif language == 'French':
            return 'fr'
        elif language == 'Greek':
            return 'el'


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TransWindow()
    window.show()
    sys.exit(app.exec_())
