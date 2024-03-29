
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,6,35,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,
        0,1,0,1,0,1,0,1,0,3,0,19,8,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,
        4,5,30,8,5,11,5,12,5,31,1,5,1,5,0,0,6,1,1,3,2,5,3,7,4,9,5,11,6,1,
        0,5,1,0,48,57,1,0,65,90,1,0,97,122,4,0,32,64,91,91,93,95,123,125,
        2,0,9,10,13,13,39,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,
        0,0,9,1,0,0,0,0,11,1,0,0,0,1,18,1,0,0,0,3,20,1,0,0,0,5,22,1,0,0,
        0,7,24,1,0,0,0,9,26,1,0,0,0,11,29,1,0,0,0,13,19,3,5,2,0,14,19,3,
        7,3,0,15,19,3,3,1,0,16,19,3,9,4,0,17,19,5,0,0,1,18,13,1,0,0,0,18,
        14,1,0,0,0,18,15,1,0,0,0,18,16,1,0,0,0,18,17,1,0,0,0,19,2,1,0,0,
        0,20,21,7,0,0,0,21,4,1,0,0,0,22,23,7,1,0,0,23,6,1,0,0,0,24,25,7,
        2,0,0,25,8,1,0,0,0,26,27,7,3,0,0,27,10,1,0,0,0,28,30,7,4,0,0,29,
        28,1,0,0,0,30,31,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,33,1,0,0,
        0,33,34,6,5,0,0,34,12,1,0,0,0,3,0,18,31,1,6,0,0
    ]

class PasswordLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    CHAR = 1
    DIGIT = 2
    UPPERCASE = 3
    LOWERCASE = 4
    SYMBOL = 5
    WS = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "CHAR", "DIGIT", "UPPERCASE", "LOWERCASE", "SYMBOL", "WS" ]

    ruleNames = [ "CHAR", "DIGIT", "UPPERCASE", "LOWERCASE", "SYMBOL", "WS" ]

    grammarFileName = "Password.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


