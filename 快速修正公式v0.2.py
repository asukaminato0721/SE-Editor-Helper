import pyperclip

l = pyperclip.paste()
l = "".join(l).split("\n")
l1 = []
func = {
    "sin": r"\sin ",
    "cos": r"\cos ",
    "ln": r"\ln ",
    "log": r"\log ",
    "tan": r"\tan ",
    "cot": r"\cot",
    "sec": r"\sec",
    r"\\sin ": r"\sin ",
    r"\\cos ": r"\cos ",
    r"\\ln ": r"\ln ",
    r"\\sec": r"\sec",
    r"\\tan": r"\tan",
    r"\\cot": r"\cot"
}

greek = {
    r"\theta": "θ",
    r"\alpha": "α",
    r"\beta": "β",
    r"\pi": "π",
    r"\psi": "ψ",
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

for i in l:
    temp = i
    for j in repl:
        for k in j:
            temp = temp.replace(k, j[k])
    l1.append(temp)
pyperclip.copy("\n".join(l1))
spam = pyperclip.paste()
