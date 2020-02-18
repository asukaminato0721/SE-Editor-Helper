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
    "exp": r"\exp ",
    r"\\sin": r"\sin ",
    r"\\cos": r"\cos ",
    r"\\ln": r"\ln ",
    r"\\sec": r"\sec ",
    r"\\tan": r"\tan ",
    r"\\cot": r"\cot ",
    r"\\min": r"\min ",
    r"\\max": r"\max ",
    r"arc\tan ": r"\arctan ",
    r"\\exp": r"\exp "
}

greek = {
    r"\theta": "θ",
    r"\alpha": "α",
    r"\beta": "β",
    r"\pi": "π",
    r"\psi": "ψ",
    r"\lambda": "λ",
    r"\partial": "∂",
    r"\gamma": "γ",
    r"\omega": "ω",
    r"\Omega": "Ω",
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
    r"\cdot": "⋅",
    r"\pm": "±",
    # r"\leq": "⩽",
    # r"\le": "⩽",
    #  r"\geq": "⩾",
    #  r"\ge": "⩾"
}

repl = [func, greek, bracket, symbol]
