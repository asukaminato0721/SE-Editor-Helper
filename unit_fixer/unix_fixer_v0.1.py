# -*- coding: utf-8 -*-
"""
Created on 2020/2/23 14:52
版权所有（c）<2020> 11598
github:https://github.com/HydrogenDeuterium
"""
import pyperclip

unitlist = ["kg", "sec", "mm"]

i = pyperclip.paste()

for unit in unitlist:
    i = i.replace(r"\mathrm{" + unit + "}", unit)
    i = i.replace(unit, r"\mathrm{" + unit + "}")
print(i)

pyperclip.copy(i)
