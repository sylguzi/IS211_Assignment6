#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 6 tests"""

import conversions
import unittest
#note: use assertAlmostEqual...? we're not rounding tho.
#include 5 cases per test
class KnownValues(unittest.TestCase):

	fahrenheit = [5.0,50.0,100.04,131.0,212.0]
	celsius = [-15.0,10.0,37.8,55.0,100.0]
	kelvin = [258.15,283.15,310.95,328.15,373.15]

	def testCelsiustoKelvin(self):
		"""celsius/kelvin values should match"""
		for i in range(len(self.celsius)):
			testedKelvin = conversions.convertCelsiusToKelvin(
					self.celsius[i])
			self.assertEqual(self.kelvin[i],testedKelvin,msg=
				'{}K != {}K'.format(
					testedKelvin,self.kelvin[i]))

	def testCelsiustoFahrenheit(self):
		"""celsius/fahrenheit values should match"""
		for i in range(len(self.celsius)):
			testedFahrenheit = conversions.convertCelsiusToFahrenheit(
					self.celsius[i])
			self.assertEqual(self.fahrenheit[i],testedFahrenheit,msg=
				'{}F != {}F'.format(
					testedFahrenheit,self.fahrenheit[i]))

	def testFahrenheittoCelsius(self):
		"""fahrenheit/celsius values should match"""
		for i in range(len(self.fahrenheit)):
			testedCelsius = conversions.convertFahrenheitToCelsius(
						self.fahrenheit[i])
			self.assertEqual(self.celsius[i],testedCelsius,msg=
				'{}C != {}C'.format(
					testedCelsius,self.celsius[i]))

	def testFahrenheittoKelvin(self):
		"""fahrenheit/kelvin values should match"""
		for i in range(len(self.fahrenheit)):
			testedKelvin = conversions.convertFahrenheitToKelvin(
				self.fahrenheit[i])
			self.assertEqual(self.kelvin[i],testedKelvin,msg=
				'{}K != {}K'.format(
					testedKelvin,self.kelvin[i]))

	def testKelvintoCelsius(self):
		"""kelvin/celsius values should match"""
		for i in range(len(self.kelvin)):
			testedCelsius = conversions.convertKelvinToCelsius(
				self.kelvin[i])
			self.assertEqual(self.celsius[i],testedCelsius,msg=
				'{}C != {}C'.format(
					testedCelsius,self.celsius[i]))

	def testKelvintoFahrenheit(self):
		"""kelvin/fahrenheit values should match"""
		for i in range(len(self.kelvin)):
			testedFahrenheit = conversions.convertKelvinToFahrenheit(
				self.kelvin[i])
			self.assertEqual(self.fahrenheit[i],testedFahrenheit,msg=
				'{}F != {}F'.format(
					testedFahrenheit,self.fahrenheit[i]))

if __name__ == '__main__':
		unittest.main()