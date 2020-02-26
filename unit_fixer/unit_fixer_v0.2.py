# -*- coding: utf-8 -*-
"""
Created on 2020/2/23 21:06
版权所有（c）<2020> 11598
github:https://github.com/HydrogenDeuterium
使用正则替换来解决类似mmHg生成\mathrm{\mathrm{mm}Hg}的问题
"""

import re

import pyperclip

unit_list = ["kg", "sec", "mmHg", "mm", "meter", "gram", "Pa"]
regex_string = "|".join(unit_list)
regex_clean = r'\\mathrm{(' + regex_string + ')}'
unit_clean = re.compile(regex_clean)
unit_regex = re.compile(regex_string)


def clean(matched):
    return matched.group()[8:-1]


def process(matched):
    return r"\mathrm{" + matched.group() + "}"


string = pyperclip.paste()

while unit_clean.search(string):
    string = re.sub(unit_clean, clean, string)
string = re.sub(unit_regex, process, string)

print(string)
pyperclip.copy(string)
