import re
from refine import refine


def replace_dollar_tex(s):
    l = len(s)
    i, j, stack = 0, 0, 0
    new_txt = []
    while i < l:
        if s[i] == "\\" and (i + 1) < l:  # 读到 \$ 的判断
            if s[i + 1] == '$':
                # skip if it is escaped dollar
                new_txt += '$'
                i += 1
            elif stack == 0:
                # otherwise just copy it
                new_txt += s[i]
        elif s[i] == '$':
            if stack == 0:  # first open dollar
                stack = 1
                j = i + 1
            elif stack == 1:  # second dollar
                if i == j:
                    # consecutive dollar
                    # (second open dollar)
                    stack = 2
                    j = i + 1
                else:
                    # non-consecutive dollar
                    # (close dollar)
                    stack = 0
                    # print('single: %s' % s[j:i])
                    new_txt.append(r"$"),
                    new_txt.append(refine(s[j:i]))
                    new_txt.append(r"$")    # 更改定界符
            else:  # stack == 2
                # first close dollar
                stack = 0
                # print('double: %s' % s[j:i])
                new_txt.append(r"$$")
                new_txt.append(refine(s[j:i]))
                new_txt.append(r"$$")  # 更改定界符
                # skip the second close dollar
                i += 1
        elif stack == 0:
            # non-escaped and non enclosed characters
            new_txt += s[i]
        i += 1
    return "".join(new_txt)


# def replace_display_tex(s):
#     # replace '\[ * \]'
#     regex = re.compile('\\\\\[(.+?)\\\\\]')
#     return re.sub(regex, r"[imath]\1[/imath]", s)


replace_dollar_tex("$tanx+tanhx+cosx+coshx$")


# def replace_inline_tex(s):
#     # replace '\\( * \\)'
#     regex = re.compile('\\\\\\\\\((.+)\\\\\\\\\)')
#     return re.sub(regex, r"[imath]\1[/imath]", s)

# curl http://math.stackexchange.com/questions/1886701/justify-a-function-series-is-approximating-another-function
# to test everything.
