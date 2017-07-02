#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Arun T
"""
import pint

def uom_conversion(measurement, from_uom, to_uom):
  from_uom = from_uom.strip().lower()
  to_uom = to_uom.strip().lower()
  uom_dict = {
   "mm": ["millimeter", "milli meter", "mm"],
   "cm": ["centimeter", "centi meter", "cm"],
   "ft": ["foot", "feet", "ft"],
   "in": ["inch", "inches", "in"],
   "m": ["meter", "m"]
  }
  ureg = pint.UnitRegistry()
  for key, value in uom_dict.items():
    if from_uom in value: source = measurement * ureg(key)
    if to_uom in value: target = key
  if (source and target): return(str(source.to(target)).split(" ")[0])
  return(None)

def uom_std_abb(measure):
  measure = measure.strip().lower()
  uom_dict = {
  "LBS": ["pound", "pounds", "lbs", "lb"],
  "KGS": ["kilo", "kilos", "kilogram", "kilograms", "kilo gram", "kilo grams", "kg", "kgs"]
  }
  for key, value in uom_dict.items():
    if measure in value: return(key)
  return(None)