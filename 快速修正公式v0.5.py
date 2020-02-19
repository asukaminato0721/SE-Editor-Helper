from function import replace_dollar_tex
import pyperclip

l = pyperclip.paste()
l = "".join(l)  # 得到一串
# 测试用例 l = r"I will test this tool to do sth$logx+logy=logxy$ $$supf(x)$$ $arctan x$"
l = replace_dollar_tex(l)

print(l)

pyperclip.copy(l)
