import sys
import os
from PyQt5.QtWidgets import QVBoxLayout,QMessageBox
from PyQt5 import QtWidgets, uic, QtCore, QtGui
import rc
from word_gen import generate_word

class MyWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = uic.loadUi("GUI.ui", self)
		self.letters = [self.ui.pushButton_9,self.ui.pushButton_10,self.ui.pushButton_11,self.ui.pushButton_12,self.ui.pushButton_13,self.ui.pushButton_14,self.ui.pushButton_15,self.ui.pushButton_16,self.ui.pushButton_17,self.ui.pushButton_18,self.ui.pushButton_19,self.ui.pushButton_20,self.ui.pushButton_21,self.ui.pushButton_22,self.ui.pushButton_23,self.ui.pushButton_24,self.ui.pushButton_25,self.ui.pushButton_26,self.ui.pushButton_27,self.ui.pushButton_28,self.ui.pushButton_29,self.ui.pushButton_30,self.ui.pushButton_31,self.ui.pushButton_32,self.ui.pushButton_33,self.ui.pushButton_34]
		self.mistakeFrames = [self.ui.frame_2,self.ui.frame_3,self.ui.frame_5,self.ui.frame_4,self.ui.frame]
		self.mistakeLabels = [self.ui.label_2,self.ui.label_3,self.ui.label_4,self.ui.label_5,self.ui.label_6]
		self.word = generate_word().lower()
		print(self.word)
		self.finished = False
		self.mistakes = 0
		self.plain = ''
		for i in range(len(self.word)):
			self.plain = self.plain + '_ '
		self.ui.label.setText(self.plain)

		for i in self.letters:
			letter = i.text()
			i.clicked.connect(lambda checked=True ,j=i: self.play_word(j.text()))

	def play_word(self,guess):
		if self.finished == False:
			if guess.lower() in self.word:
				for i,letter in enumerate(self.word):
					if guess.lower() == letter:
						self.plain = self.plain.replace(' ','')
						self.plain = self.plain[:i] + letter + self.plain[i+1:]
						self.plain = self.plain.replace('_','_ ')
						self.ui.label.setText(self.plain)
			else:
				if self.mistakes < 5:
					self.mistakes += 1
					self.checkMistakes()
				else:
					self.finished = True
		if '_' not in self.plain:
			self.finished == True

	def checkMistakes(self):
		for i in range(self.mistakes):
			self.mistakeFrames[i].setStyleSheet("margin-left: 10px;margin-right: 10px;border-radius: 10px;background-color: rgb(95, 197, 255);border: 2px solid black;")
			self.mistakeLabels[i].setStyleSheet("border: 0px;padding: 0px;background-color: rgba(0,0,0,0);color: red;")
	def getButtonText(self,button):
		return lambda: button.text()