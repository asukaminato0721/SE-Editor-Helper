from ciku import new, aim

# 几个案例：

# xtany ，tanx，Asin(wx+φ)


def 处理(s: str) -> str:
    l = len(new)
    temp = s
  #  temp = temp.replace(r"\\", r"\\ ")
    for i in range(l):
        temp = temp.replace(aim[i], new[i])

    return temp


# print(处理(r"$\arctan x$"))


def mark(st: str) -> list:
    s = 处理(st)
    l = len(s)
    record = [0] * l
    for i in new:
        j = 0
        pos = s[j:].find(i)
        while pos != -1:
            pos = s[j:].find(i) + j
            if 1 not in record[pos: pos + len(i)]:
                record[pos: pos + len(i)] = [1]*len(i)  # 在对应位置记录
            j += len(i)
            pos = s[j:].find(i)
            if pos == -1:
                break
            if j+len(i) >= l:
                break
            pos = s[j:].find(i)
    return record


def refine(st: str):  # 完成
    s = 处理(st)
    result = []
    l = mark(s)
    length = len(l)
    for i in range(length):
        if i + 1 == length:  # 收尾
            result.append(s[i])
            break
        result.append(s[i])
        if l[i] == 0 and l[i + 1] == 1:
            result.append("\\")
        elif l[i] == 1 and l[i + 1] == 0:
            result.append(" ")
    if l[0] == 1:
        result.insert(0, "\\")
    return "".join(result)


# s = r"tanhx+sint"
# print(refine(s))
