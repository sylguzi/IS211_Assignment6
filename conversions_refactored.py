#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 6 conversions_Refactored"""
import unittest

#note: dont forget keys
class ConversionNotPossible(Exception):
	pass

length = {
		'met': {'yar':(0,1.09361,0),'mil':(0,0.000621371,0)}
		,'yar': {'mil':(0,0.000568182,0),'met':(0,0.9144,0)}
		,'mil': {'met':(0,1609.34,0),'yar':(0,1760,0)}
		}
degrees = {
		'kel':{'cel':(0,1,-273.15),'fah':(-273.15,9/5,32)}
		,'cel':{'kel':(0,1,273.15),'fah':(0,9/5,32)}
		,'fah':{'kel':(-32,5.0/9.0,273.15),'cel':(-32,5.0/9.0,0)}
		}
	
def convert(fromUnit,toUnit,value):
	#needs to convert same type of unit (lengthance vs degrees); use .keys
	fromUnit = fromUnit[0:3].lower()
	toUnit = toUnit[0:3].lower()
	if not ((fromUnit in length.keys() and toUnit in length.keys()
			 ) or (fromUnit in degrees.keys() and toUnit in degrees.keys())):
		raise ConversionNotPossible
	else:
		if fromUnit == toUnit:
			newval = value
		elif fromUnit in length.keys():
			newval = (value + length[fromUnit][toUnit][0]) * length[fromUnit][toUnit][1] + length[fromUnit][toUnit][2]
		else:
			newval = (value + degrees[fromUnit][toUnit][0]) * degrees[fromUnit][toUnit][1] + degrees[fromUnit][toUnit][2]
	return float("%0.2f" %newval)

#note: use assertAlmostEqual...? but they're suppsoed to be equal?
#keep proper units
class ConvertTest(unittest.TestCase):

	def testDegrees(self):
		self.assertEqual(convert('celsius','fahrenheit',0),32.0)
		self.assertEqual(convert('celsius','kelvin',0),273.15)
		self.assertEqual(convert('kelvin','celsius',273.15),0.0)
		self.assertEqual(convert('kelvin','fahrenheit',0),-241.15)
		self.assertEqual(convert('fahrenheit','celsius',32),0.0)
		self.assertEqual(convert('fahrenheit','kelvin',0),255.37)

	def testDist(self):
		self.assertEqual(convert('meter','mile',100),0.06)
		self.assertEqual(convert('meter','yard',10),10.94)
		self.assertEqual(convert('mile','meter',10),16093.4)
		self.assertEqual(convert('mile','yard',10),17600.00)
		self.assertEqual(convert('yard','meter',3),2.74)
		self.assertEqual(convert('yard','mile',300),0.17)

	def correctUnitsTest(self):
		for l in length.keys():
			self.assertEqual(convert(i,i,10),10)
		for d in degrees.keys():
			self.assertEqual(convert(i,i,10),10)

	def testError(self):
		self.assertRaises(ConversionNotPossible,convert,'met','cel',0)

if __name__ == '__main__':
	unittest.main()