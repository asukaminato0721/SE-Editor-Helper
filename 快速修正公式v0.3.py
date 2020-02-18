# -*- coding: UTF-8 -*-
import re
import pyperclip

# 导入库

func = {
    "sin": r"\sin ",
    "cos": r"\cos ",
    "ln": r"\ln ",
    "log": r"\log ",
    "tan": r"\tan ",
    "cot": r"\cot ",
    "sec": r"\sec ",
    "min": r"\min ",
    "max": r"\max ",
    r"\\sin": r"\sin ",
    r"\\cos": r"\cos ",
    r"\\ln": r"\ln ",
    r"\\sec": r"\sec ",
    r"\\tan": r"\tan ",
    r"\\cot": r"\cot ",
    r"\\min": r"\min ",
    r"\\max": r"\max "
}

greek = {
    r"\theta": "θ",
    r"\alpha": "α",
    r"\beta": "β",
    r"\pi": "π",
    r"\psi": "ψ",
    r"\lambda": "λ"
}

bracket = {
    "(": r"\left(",
    ")": r"\right)",  # 小括号匹配
    "[": r"\left[",
    "]": r"\right]",  # 中
    r"\{": r"\left\{",
    r"\}": r"\right\}",  # 大
    r"\left\left": r"\left",
    r"\right\right": r"\right",
}

symbol = {
    r"\to": "→",
    r"\rightarrow": "→",
    r"\int": "∫",
    r"\neq": "≠",
    r"\sum": "∑",
    # r"\leq": "⩽",
    # r"\le": "⩽",
    #  r"\geq": "⩾",
    #  r"\ge": "⩾"
}

repl = [func, greek, bracket, symbol]

# 匹配替换规则


def f(matched: str):  # 此函数由 QQ: 1159841057 提供
    res = matched.group()
    for i in repl:
        for j in i:
            res = res.replace(j, i[j])
    return res


l = pyperclip.paste()
l = "".join(l)  # 得到一串

pattern = re.compile("\$.*?\$")  # 匹配 $XXX$ 的
p = re.sub(pattern, f, l)
l = "".join(p)


pattern = re.compile("\$\$.*?\$\$")  # 匹配单行 $$XXX$$ 的
p = re.sub(pattern, f, l)
l = "".join(p)

# pattern = re.compile("\$\$[(.)[0-9]\n[a-z]] *?\$\$")  # 匹配多行 $$XXX$$ 的
# p = re.sub(pattern, f, l)
# l = "".join(p)

pyperclip.copy(l)

# $sinx$cosx$$cosx$$
# $cosx$$\sin x$cosx$$\cos x$$
# $sinx$
# $cosx$

"""
$$sinx\\
cosx
$$
"""
