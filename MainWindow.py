import sys
import os
from PyQt5.QtWidgets import QVBoxLayout,QMessageBox
from PyQt5 import QtWidgets, uic, QtCore, QtGui
import resources
from generator import *

class MyWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = uic.loadUi("GUI.ui", self)
		self.letters = [self.ui.pushButton_9,self.ui.pushButton_10,self.ui.pushButton_11,self.ui.pushButton_12,self.ui.pushButton_13,self.ui.pushButton_14,self.ui.pushButton_15,self.ui.pushButton_16,self.ui.pushButton_17,self.ui.pushButton_18,self.ui.pushButton_19,self.ui.pushButton_20,self.ui.pushButton_21,self.ui.pushButton_22,self.ui.pushButton_23,self.ui.pushButton_24,self.ui.pushButton_25,self.ui.pushButton_26,self.ui.pushButton_27,self.ui.pushButton_28,self.ui.pushButton_29,self.ui.pushButton_30,self.ui.pushButton_31,self.ui.pushButton_32,self.ui.pushButton_33,self.ui.pushButton_34]
		self.mistakeFrames = [self.ui.frame_2,self.ui.frame_3,self.ui.frame_5,self.ui.frame_4,self.ui.frame]
		self.mistakeLabels = [self.ui.label_2,self.ui.label_3,self.ui.label_4,self.ui.label_5,self.ui.label_6]
		try:
			generate_word(random.choice(RandomWordTypes))
		except:
			self.modes = ['country', 'animal', 'footballer']
			self.showDialog("Can't use words mode (No Internet Connection)")
		else:
			self.modes = ['word', 'country', 'animal', 'footballer']
		# mode = random.choice(self.modes)
		# if mode == 'word':
		# 	wordtype = random.choice(RandomWordTypes)
		# 	self.word = generate_word(wordtype).lower()
		# 	self.ui.label_7.setText("A word (" + wordtype + ')')
		# 	print(self.word)
		# elif mode == 'country':
		# 	country = generate_country()
		# 	wordtype = random.choice(CountryTypes)
		# 	self.word = country[wordtype].lower()
		# 	if wordtype == 'name':
		# 		self.ui.label_7.setText('A country (' + country['region'] + ')')
		# 	elif wordtype == 'capital':
		# 		self.ui.label_7.setText('The capital of ' + country['name'])
		# elif mode == 'animal':
		# 	animal = generate_animal()
		# 	self.word = animal.lower()
		# 	self.ui.label_7.setText('An animal')


		# self.ui.PlayAgain.setVisible(False)
		# self.ui.Quit.setVisible(False)
		# self.finished = False
		# self.gameOver = False
		# self.mistakes = 0
		# self.plain = ''
		# for i in range(len(self.word)):
		# 	if self.word[i] == ' ':
		# 		self.plain += '$'
		# 	else:
		# 		self.plain = self.plain + '_ '
		# if len(self.plain) >= 18:
		# 	for i in range(len(self.plain)):
		# 		if self.plain[i] == '$':
		# 			self.plain = self.plain[:i] + '\n' + self.plain[i+1:]
		# 			break
		# tempplain = self.plain.replace('$',' ')
		# self.ui.label.setText(tempplain)
		self.playAgain()

		for i in self.letters:
			i.clicked.connect(lambda checked=True ,j=i: self.play_word(j))
		self.ui.Quit.clicked.connect(self.closeWindow)
		self.ui.PlayAgain.clicked.connect(self.playAgain)
		self.ui.settings.clicked.connect(self.settingsWindow)

	def settingsWindow(self):
		win = Settings()
		win.setWindowTitle("Settings")
		win.setWindowIcon(QtGui.QIcon("assets\\settings.png"))
		win.show()

	def play_word(self,guess):
		if self.finished == False and self.gameOver == False:
			guess.setEnabled(False)
			if guess.text().lower() in self.word:
				self.ui.widget.setStyleSheet("border-image: url(:/background/assets/alive.png) 0 0 0 0 stretch stretch;background-repeat: no-repeat;background-position: center top;")
				# self.plain = self.plain.replace(' ','$')
				for i,letter in enumerate(self.word):
					if guess.text().lower() == letter:
						self.plain = self.plain.replace(' ','')
						self.plain = self.plain[:i] + letter + self.plain[i+1:]
						self.plain = self.plain.replace('_','_ ')
				tempplain = self.plain.replace('$',' ')
				self.ui.label.setText(tempplain)
						
			else:
				if self.mistakes < 5:
					self.mistakes += 1
					self.checkMistakes()
		if '_' not in self.plain:
			self.finished = True
			self.ui.label.setText(self.word + "\nCongrats, You Won!")
			self.ui.PlayAgain.setVisible(True)
			self.ui.Quit.setVisible(True)
			self.ui.label_7.setVisible(False)
			self.ui.label.setStyleSheet("background-color: rgba(0,0,0,0);border: 0px;color: green;")
			self.ui.widget.setStyleSheet("border-image: url(:/background/assets/smile.png) 0 0 0 0 stretch stretch;background-repeat: no-repeat;background-position: center top;")

	def checkMistakes(self):
		for i in range(self.mistakes):
			self.mistakeFrames[i].setStyleSheet("margin-left: 10px;margin-right: 10px;border-radius: 10px;background-color: rgb(95, 197, 255);border: 2px solid black;")
			self.mistakeLabels[i].setStyleSheet("border: 0px;padding: 0px;background-color: rgba(0,0,0,0);color: red;")
		self.ui.widget.setStyleSheet("border-image: url(:/background/assets/angry.png) 0 0 0 0 stretch stretch;background-repeat: no-repeat;background-position: center top;")
		if self.mistakes >= 5:
			self.gameOver = True
			self.ui.widget.setStyleSheet("border-image: url(:/background/assets/dead.png) 0 5 -25 0 stretch stretch;background-repeat: no-repeat;background-position: center top;")
			self.ui.label.setText("You Lost... Try Again?\n(Word was: " + self.word + ")")
			self.ui.label.setStyleSheet("background-color: rgba(0,0,0,0);border: 0px;color:red;")
			# self.ui.label_7.setText("You Lost... Try Again?")
			self.ui.PlayAgain.setVisible(True)
			self.ui.Quit.setVisible(True)
			self.ui.label_7.setVisible(False)
	
	def playAgain(self):
		for i in self.letters:
			i.setEnabled(True)
		for i,j in zip(self.mistakeLabels,self.mistakeFrames):
			i.setStyleSheet("border: 0px;padding: 0px;background-color: rgba(0,0,0,0);color: rgba(0,0,0,50)")
			j.setStyleSheet("margin-left: 10px;margin-right: 10px;border-radius: 10px;background-color: rgba(255,255,255,200);border: 2px solid black;padding: 0px;")
		self.ui.widget.setStyleSheet("border-image: url(:/background/assets/alive.png) 0 0 0 0 stretch stretch;background-repeat: no-repeat;background-position: center top;")
		self.ui.PlayAgain.setVisible(False)
		self.ui.Quit.setVisible(False)
		self.ui.label.setStyleSheet("background-color: rgba(0,0,0,0);border: 0px;")
		mode = random.choice(self.modes)
		if mode == 'word':
			wordtype = random.choice(RandomWordTypes)
			self.word = generate_word(wordtype).lower()
			self.ui.label_7.setText("A word (" + wordtype + ')')
			print(self.word)
		elif mode == 'country':
			country = generate_country()
			wordtype = random.choice(CountryTypes)
			self.word = country[wordtype].lower()
			if wordtype == 'name':
				self.ui.label_7.setText('A country (' + country['region'] + ')')
			elif wordtype == 'capital':
				self.ui.label_7.setText('The capital of ' + country['name'])
		elif mode == 'animal':
			self.word = generate_animal().lower()
			self.ui.label_7.setText('An animal')
		elif mode == 'footballer':
			footballer = generate_footballer()
			self.word = footballer['name'].lower()
			self.ui.label_7.setText('A ' + str(footballer['age']) + ' years old ' + footballer['nationality'].lower() + ' ' + footballer['position'].lower() + ' footballer from ' + footballer['team'])


		self.ui.PlayAgain.setVisible(False)
		self.ui.Quit.setVisible(False)
		self.ui.label_7.setVisible(True)
		self.finished = False
		self.gameOver = False
		self.mistakes = 0
		self.plain = ''
		for i in range(len(self.word)):
			if self.word[i] == ' ':
				self.plain += '$'
			else:
				self.plain = self.plain + '_ '
		if len(self.plain) >= 18:
			for i in range(len(self.plain)):
				if self.plain[i] == '$':
					self.plain = self.plain[:i] + '\n' + self.plain[i+1:]
					break
		tempplain = self.plain.replace('$',' ')
		self.ui.label.setText(tempplain)
				

	def closeWindow(self):
		self.close()

	def showDialog(self,msg):
		msgBox = QMessageBox()
		msgBox.setIcon(QMessageBox.Information)
		msgBox.setText(msg)
		msgBox.setWindowTitle("QMessageBox Example")
		msgBox.setStandardButtons(QMessageBox.Ok)
		# msgBox.buttonClicked.connect(msgButtonClick)

		returnValue = msgBox.exec()
		if returnValue == QMessageBox.Ok:
			print('OK clicked')

class Settings(QtWidgets.QDialog):
	def __init__(self):
		super().__init__()
		self.ui = uic.loadUi("settings.ui", self)
		self.Noun = True
		self.Verb = True
		self.Adverb = True
		self.Adjective = True
		self.Words = True
		self.Animal = True
		self.Misc = True
		self.Country = True
		self.Capital = True
		self.Countries = True
		self.Football = True
		self.Sports = True

		self.checkBoxes = [self.ui.noun,self.ui.verb,self.ui.adverb,self.ui.adjective,self.ui.animal,self.ui.country,self.ui.capital,self.ui.football]
		for i in self.checkBoxes:
			i.clicked.connect(self.checkUniBoxes)
		self.ui.words.clicked.connect(self.checkWords)
		self.ui.misc.clicked.connect(self.checkMisc)
		self.ui.countries.clicked.connect(self.checkCountries)
		self.ui.sports.clicked.connect(self.checkSports)

	def checkUniBoxes(self):
		self.Noun = self.ui.noun.isChecked()
		self.Verb = self.ui.verb.isChecked()
		self.Adverb = self.ui.adverb.isChecked()
		self.Adjective = self.ui.adjective.isChecked()
		self.Animal = self.ui.animal.isChecked()
		self.Country = self.ui.country.isChecked()
		self.Capital = self.ui.capital.isChecked()
		self.Football = self.ui.football.isChecked()
		if all([self.Noun,self.Verb,self.Adverb,self.Adjective]):
			self.ui.words.setChecked(True)
		else:
			self.ui.words.setChecked(False)
		if all([self.Country,self.Capital]):
			self.ui.countries.setChecked(True)
		else:
			self.ui.countries.setChecked(False)
		if all([self.Animal]):
			self.ui.misc.setChecked(True)
		else:
			self.ui.misc.setChecked(False)
		if all([self.Football]):
			self.ui.sports.setChecked(True)
		else:
			self.ui.sports.setChecked(False)

	def checkWords(self):
		state = self.ui.words.isChecked()
		for i in self.checkBoxes[:4]:
			i.setChecked(state)

	def checkCountries(self):
		state = self.ui.countries.isChecked()
		for i in self.checkBoxes[5:7]:
			i.setChecked(state)

	def checkMisc(self):
		state = self.ui.misc.isChecked()
		for i in self.checkBoxes[4:5]:
			i.setChecked(state)

	def checkSports(self):
		state = self.ui.sports.isChecked()
		for i in self.checkBoxes[7:8]:
			i.setChecked(state)