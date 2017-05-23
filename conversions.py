#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 6 conversions"""

import decimal

#notes: use %.3f - specifies the length for the whole number
#need 6 converts C>K | C>F | F>K | F>C | K>F | K>C
def convertCelciusToKelvin(degrees):
    kdegrees = degrees + 273.15
    return float("%.3f" % kdegrees)
    

def convertCelciusToFahrenheit(degrees):
    fdegrees = (1.8 * degrees) + 32
    return float("%.3f" % fdegrees)


def convertFahrenheitToKelvin(degrees):
    kdegrees = ((degrees - 32) / 1.8) + 273.15
    return float("%.3f" % kdegrees)


def convertFahrenheitToCelcius(degrees):
    cdegrees = (degrees - 32) / 1.8
    return float("%.3f" % cdegrees)


def convertKelvinToFahrenheit(degrees):
    fdegrees = (degrees - 273.15) * 1.8 + 32
    return float("%.3f" % fdegrees)


def convertKelvinToCelcius(degrees):
    cdegrees = degrees - 273.15
    return float("%.3f" % cdegrees)