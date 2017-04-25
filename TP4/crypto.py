#!/usr/bin/python
# -*- coding:Utf-8 -*-
from string import upper

class Crypto:
	"""Ciptare folosinf algoritmul lui Caesar
	ch = chaine, d = decalage"""
	def __init__(self, ch, d):
		self.ch, self.d = ch, d
		#Initializam dictionarele pentru ca apoi sa accesam fiecare element din ele.
		#Correspondance pentru criptare, decorrespondance pentru decodare
		self.correspondance = {}
		self.decorrespondance = {}
		
		#Cum dictionarele au nevoie de liste, vom crea unele dupa cum urmeaza:
		#  alpha = alfabet normal. ald = alfabet decalat
		self.alpha = [chr(x) for x in xrange(97, 123)]
		self.ald = [self.alpha[(i+self.d)%26] for i in xrange(26)] #Utilisation du modulo pour éviter le OutOfRange
		#Constructia corespondentei intre cele doua liste
		for x in xrange(26):
			self.correspondance[self.alpha[x]] = self.ald[x]
		
	def inverser_dico(self):
		"""Constructia decorespondentei intre cele doua alfabete,care se face inainte de traducere prin inversarea cheii de decalaj """
		for (k, v) in self.correspondance.items():
			self.decorrespondance[v] = k
		return self.decorrespondance

	def code(self, p):
		"""Codarea si decodarea textului"""
		self.new_ch = []
		self.inverser_dico()
		for car in self.ch:
			if car is ' ':
				self.new_ch.append(' ')
			else:
				if p is True:
					self.new_ch.append(self.correspondance[car])
				else: 
					self.new_ch.append(self.decorrespondance[car])

		return self.new_ch

if __name__ == "__main__":
	while 1:
		chx = raw_input("Tapez C pour crypter ou D pour decrypter : ")
		if chx.upper() == 'C':
			x = True
		elif chx.upper() == 'D':
			x = None
		else:
			print "Esseyez encore une fois !"
			break
		
		decalage = raw_input("De combien de lettres voulez vous decaler votre code : ")
		if decalage.isdigit():
			txt = raw_input("Veuillez entrer votre texte :\n")
			a = Crypto(txt.lower(), int(decalage))
		else:
			print "Vous devez entrer un nombre !"
			break
		
		try:
			a.code(x)
			print ''.join(a.code(x))
		except:
			print "Vous ne devez rentrer que des lettres !"
			break
				
		r = raw_input("Autre texte a coder ( 1: Oui, Entree: Non ) : ")
		if r == '1':
			continue
		else:
			break