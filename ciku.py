new = ['arccos', 'arcsin', 'arctan', 'cosh', 'coth', 'frac', 'sign', 'sinh', 'tanh', 'zeta', 'Cap', 'Chi', 'Cup', 'Eta', 'Lsh',
        'Phi', 'Psi', 'Rho', 'Rsh', 'Tau', 'arg', 'ast', 'bot', 'cap', 'chi', 'cos', 'cot', 'csc', 'cup', 'deg', 'det', 'dim',
        'div', 'dot', 'ell', 'end', 'eta', 'eth', 'exp', 'gcd', 'geq', 'ggg', 'hom', 'inf', 'ker', 'leq', 'lim', 'log', 'lor',
        'max', 'mid', 'min', 'mod', 'neg', 'neq', 'not', 'phi', 'pod', 'psi', 'rho', 'sec', 'sgn', 'sim', 'sin', 'sum', 'sup',
        'tag', 'tan', 'tau', 'top', 'vec', 'vee', 'Mu', 'Nu', 'Pi', 'Pr', 'Re', 'cr', 'lg', 'ln', 'mp', 'pi']

aim = list(map(lambda x: "\\" + x,
               new))  # 多余的 = ['leftrightsquigarrow', 'Longleftrightarrow', 'longleftrightarrow', 'leftrightharpoons',
# 'rightleftharpoons', 'circlearrowright', 'downharpoonright', 'rightharpoondown', 'rightrightarrows', 'vartriangleright',
# 'bigtriangledown', 'circlearrowleft', 'curvearrowright', 'downharpoonleft', 'leftharpoondown', 'leftrightarrows',
# 'nLeftrightarrow', 'nleftrightarrow', 'rightleftarrows', 'rightsquigarrow', 'trianglerighteq', 'vartriangleleft',
# 'Leftrightarrow', 'Longrightarrow', 'curvearrowleft', 'downdownarrows', 'hookrightarrow', 'leftleftarrows', 'leftrightarrow',
# 'longrightarrow', 'looparrowright', 'overrightarrow', 'rightarrowtail', 'rightharpoonup', 'sphericalangle', 'trianglelefteq',
# 'upharpoonright', 'Longleftarrow', 'bigtriangleup', 'divideontimes', 'hookleftarrow', 'leftarrowtail', 'leftharpoonup',
# 'longleftarrow',      'looparrowleft', 'measuredangle', 'overleftarrow', 'smallsetminus', 'triangleright', 'upharpoonleft',
# 'varsubsetneqq', 'varsupsetneqq', 'operatorname', 'triangledown', 'triangleleft', 'varsubsetneq', 'varsupsetneq',
# 'Rrightarrow', 'Updownarrow', 'backepsilon', 'curlyeqprec', 'curlyeqsucc', 'eqslantless', 'nRightarrow', 'nrightarrow',
# 'preccurlyeq', 'precnapprox', 'succcurlyeq', 'succnapprox', 'thickapprox', 'updownarrow', 'vartriangle', 'xrightarrow',
# 'Lleftarrow', 'Rightarrow', 'curlywedge', 'eqslantgtr', 'gtreqqless', 'lessapprox', 'lmoustache', 'longmapsto', 'nLeftarrow',
# 'nleftarrow', 'precapprox', 'rightarrow', 'rmoustache', 'smallfrown', 'smallsmile', 'sqsubseteq', 'sqsupseteq', 'subsetneqq',
# 'succapprox', 'supsetneqq', 'underbrace', 'upuparrows', 'varUpsilon', 'varepsilon', 'varnothing', 'varprojlim', 'xleftarrow',
# 'Arrowvert', 'Downarrow', 'Leftarrow', 'VarLambda', 'arrowvert', 'backsimeq', 'backslash', 'bigotimes', 'bracevert',
# 'downarrow', 'gtrapprox', 'gtreqless', 'gvertneqq', 'impliedby', 'leftarrow', 'lvertneqq', 'mathbbmss', 'mathbbmtt',
# 'ngeqslant', 'nleqslant', 'nparallel', 'nsubseteq', 'nsupseteq', 'overbrace', 'subseteqq', 'subsetneq', 'supseteqq',
# 'supsetneq', 'triangleq', 'varinjlim', 'varliminf', 'varlimsup', 'varmathbb', 'varpropto', 'VarOmega', 'approxeq',
# 'barwedge', 'bigoplus', 'bigsqcup', 'biguplus', 'bigwedge', 'buildrel', 'curlyvee', 'emptyset', 'geqslant', 'gnapprox',
# 'idotsint', 'leftroot', 'leqslant', 'lnapprox', 'mathfrak', 'multimap', 'parallel', 'precneqq', 'precnsim', 'setminus',
# 'smallint', 'sqsubset', 'sqsupset', 'stackrel', 'subseteq', 'succneqq', 'succnsim', 'supseteq', 'textfrak', 'textgoth',
# 'textswab', 'thicksim', 'triangle', 'underset', 'varDelta', 'varGamma', 'varSigma', 'varTheta', 'varkappa', 'varsigma',
# 'vartheta', 'Epsilon', 'Omicron', 'Uparrow', 'Upsilon', 'backsim', 'between', 'bigcirc', 'bigodot',    'dotplus', 'enspace',
# 'epsilon', 'gtrless', 'implies', 'leadsto', 'lessdot', 'lesssim', 'mathbbm', 'mathcal', 'mathpzc', 'mathscr', 'nearrow',
# 'newline', 'nexists', 'npreceq', 'nsucceq', 'nwarrow', 'omicron', 'overset', 'partial', 'precsim', 'projlim', 'searrow',
# 'succsim', 'swarrow', 'uparrow', 'upsilon', 'Lambda', 'Subset', 'Supset', 'approx',, 'bigcap', 'bigcup', 'bigvee', 'bowtie',
# 'choose', 'circeq', 'coprod', 'dbinom', 'ddddot', 'eqcirc', 'exists', 'forall', 'gtrdot', 'gtrsim', 'hspace', 'iddots',
# 'iiiint', 'injlim', 'lambda', 'langle', 'lbrace', 'lbrack', 'lfloor', 'lgroup', 'liminf', 'limsup', 'ltimes', 'mapsto',
# 'mathbb', 'mathds', 'mspace', 'ominus', 'otimes', 'preceq', 'propto', 'rangle', 'rbrace', 'rbrack', 'rfloor', 'rgroup',
# 'rtimes', 'signum', 'subset', 'succeq', 'supset', 'tbinom', 'uproot', 'varPhi', 'varPsi', 'varphi', 'varrho', 'veebar',
# 'Alpha', 'Delta', 'Gamma', 'Kappa', 'Omega', 'Sigma', 'Theta', 'above', 'aleph', 'alpha', 'amalg', 'angle', 'array', 'asymp',
# 'begin', 'binom', 'brack', 'cdots', 'cfrac', 'color', 'dashv', 'dddot', 'ddots', 'delta', 'dfrac', 'dotsb', 'dotsc', 'dotsi',
# 'dotsm', 'dotso', 'empty', 'eqsim', 'equiv', 'frown', 'gamma', 'gggtr', 'gneqq', 'gnsim', 'hskip', 'iiint', 'imath', 'infty',
# 'intop', 'jmath', 'kappa', 'lVert', 'label', 'lceil', 'ldots', 'lneqq', 'lvert', 'mkern', 'mskip', 'nabla', 'ncong', 'ngeqq',
# 'nleqq', 'nless', 'nprec', 'nsucc', 'omega', 'oplus', 'prime', 'qquad', 'rVert', 'rceil', 'right', 'rvert', 'sigma', 'simeq',
# 'sqcap', 'sqcup', 'tfrac', 'theta', 'times', 'unlhd', 'unrhd', 'uplus', 'varPi', 'varXi', 'varpi', 'vdots', 'wedge', 'Beta',
# 'Iota', 'Join', 'Vert', 'Zeta', 'atop', 'beta', 'beth', 'bmod', 'cdot', 'circ', 'cong']

# class Trie:
#     # word_end = -1

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.root = {}
#         self.word_end = -1

#     def insert(self, word):
#         """
#         Inserts a word into the trie.
#         :type word: str
#         :rtype: void
#         """
#         curNode = self.root
#         for c in word:
#             if not c in curNode:
#                 curNode[c] = {}
#             curNode = curNode[c]

#         curNode[self.word_end] = True

#     def search(self, word):
#         """
#         Returns if the word is in the trie.
#         :type word: str
#         :rtype: bool
#         """
#         curNode = self.root
#         for c in word:
#             if not c in curNode:
#                 return False
#             curNode = curNode[c]

#         # Doesn't end here
#         if self.word_end not in curNode:
#             return False

#         return True

#     def startsWith(self, prefix):
#         """
#         Returns if there is any word in the trie that starts with the given prefix.
#         :type prefix: str
#         :rtype: bool
#         """
#         curNode = self.root
#         for c in prefix:
#             if not c in curNode:
#                 return False
#             curNode = curNode[c]

#         return True


# trie = Trie()
# for i in new字典:
#     trie.insert(i)


# def 有前缀(s: str):
#     return trie.startsWith(s)
