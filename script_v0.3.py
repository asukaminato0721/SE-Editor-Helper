# -*- coding: UTF-8 -*-
import re

import pyperclip

from rules import repl  # 导入替换规则


# 导入库


def f(matched: str):  # 此函数由 QQ: 1159841057 提供
    res = matched.group()
    for i in repl:
        for j in i:
            res = res.replace(j, i[j])
    return res


l = pyperclip.paste()
l = "".join(l)  # 得到一串

# l = "$$sinx\\\ncosx"

pattern = re.compile("\$.*?\$")  # 匹配 $XXX$ 的
p = re.sub(pattern, f, l)
l = "".join(p)

pattern = re.compile("\$\$.*?\$\$")  # 匹配单行 $$XXX$$ 的
p = re.sub(pattern, f, l)
l = "".join(p)

# pattern = re.compile("\$\$[(.)[0-9]\n[a-z]\\]*?\$\$")  # 匹配多行 $$XXX$$ 的
# p = re.sub(pattern, f, l)
# l = "".join(p)

pyperclip.copy(l)

# print(l)
# $sinx$cosx$$cosx$$
# $cosx$$\sin x$cosx$$\cos x$$
# $sinx$
# $cosx$

"""
$$sinx\\
cosx
$$
"""
