import pyperclip

from rules import repl

l = pyperclip.paste()
l = "".join(l).split("\n")
l1 = []
for i in l:
    temp = i
    for j in repl:
        for k in j:
            temp = temp.replace(k, j[k])
    l1.append(temp)
pyperclip.copy("\n".join(l1))
spam = pyperclip.paste()
