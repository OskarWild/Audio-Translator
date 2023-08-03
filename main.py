from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi
import sys
from translate import translate_
import speech_recognition as sr
import os
import playsound
from gtts import gTTS


class TransWindow(QMainWindow):
    def __init__(self):
        super(TransWindow, self).__init__()
        loadUi('trans.ui', self)
        self.btn_micro.clicked.connect(self.command)
        self.btn_trans.clicked.connect(self.trans)
        self.btn_speak.clicked.connect(self.speak)
        self.show()

    @pyqtSlot()
    def command(self):
        r = sr.Recognizer()

        with sr.Microphone() as source:
            print('Say something :')
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, 1)
            audio = r.listen(source)
            listening_lang = self.wich_language(
                self.frombox.currentText(), False)

            try:
                task = r.recognize_google(
                    audio, language=listening_lang).lower()
                print(task)
            except sr.UnknownValueError:
                print('I cannot understand you')
                task = self.command()
            self.Edit.setText(task)

    @pyqtSlot()
    def trans(self):
        from_language = self.wich_language(self.frombox.currentText())
        to_language = self.wich_language(self.tobox.currentText())

        self.result.setText(
            str(translate_(self.Edit.text(), from_language, to_language)))

    @pyqtSlot()
    def speak(self):
        text = self.result.text()
        sepaking_language = self.wich_language(self.tobox.currentText())

        tts = gTTS(text=text, lang=sepaking_language)
        filename = "voice.mp3"
        tts.save(filename)
        playsound.playsound(filename)

    def wich_language(self, language, is_for_trans=True):
        if language == 'English':
            if is_for_trans:
                return 'en'
            else:
                return 'en-US'
        elif language == 'French':
            if is_for_trans:
                return 'fr'
            else:
                return 'fr-FR'
        elif language == 'Greek':
            if is_for_trans:
                return 'el'
            else:
                return 'el-GR'


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TransWindow()
    window.show()
    sys.exit(app.exec_())
