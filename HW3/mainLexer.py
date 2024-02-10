
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,8,123,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,4,0,27,8,0,
        11,0,12,0,28,1,1,4,1,32,8,1,11,1,12,1,33,1,2,1,2,1,2,1,2,1,2,1,2,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,4,5,66,8,5,11,5,12,5,67,1,5,1,5,
        4,5,72,8,5,11,5,12,5,73,1,6,4,6,77,8,6,11,6,12,6,78,1,6,1,6,4,6,
        83,8,6,11,6,12,6,84,1,6,1,6,4,6,89,8,6,11,6,12,6,90,1,7,4,7,94,8,
        7,11,7,12,7,95,1,8,4,8,99,8,8,11,8,12,8,100,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,4,9,111,8,9,11,9,12,9,112,1,10,1,10,1,11,4,11,118,8,
        11,11,11,12,11,119,1,11,1,11,0,0,12,1,0,3,0,5,1,7,2,9,3,11,4,13,
        5,15,0,17,0,19,6,21,7,23,8,1,0,4,7,0,37,37,43,43,45,46,48,57,65,
        90,95,95,97,122,4,0,45,46,48,57,65,90,97,122,1,0,48,57,3,0,9,10,
        13,13,32,32,129,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,
        0,13,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,1,26,1,0,0,0,
        3,31,1,0,0,0,5,35,1,0,0,0,7,41,1,0,0,0,9,52,1,0,0,0,11,65,1,0,0,
        0,13,76,1,0,0,0,15,93,1,0,0,0,17,98,1,0,0,0,19,102,1,0,0,0,21,114,
        1,0,0,0,23,117,1,0,0,0,25,27,7,0,0,0,26,25,1,0,0,0,27,28,1,0,0,0,
        28,26,1,0,0,0,28,29,1,0,0,0,29,2,1,0,0,0,30,32,7,1,0,0,31,30,1,0,
        0,0,32,33,1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,34,4,1,0,0,0,35,36,
        3,1,0,0,36,37,5,64,0,0,37,38,3,3,1,0,38,39,5,46,0,0,39,40,3,3,1,
        0,40,6,1,0,0,0,41,42,3,21,10,0,42,43,3,21,10,0,43,44,3,21,10,0,44,
        45,3,21,10,0,45,46,3,21,10,0,46,47,3,21,10,0,47,48,3,21,10,0,48,
        49,3,21,10,0,49,50,3,21,10,0,50,51,3,21,10,0,51,8,1,0,0,0,52,53,
        6,4,0,0,53,54,3,21,10,0,54,55,3,21,10,0,55,56,3,21,10,0,56,57,3,
        21,10,0,57,58,3,21,10,0,58,59,3,21,10,0,59,60,3,21,10,0,60,61,3,
        21,10,0,61,62,3,21,10,0,62,63,3,21,10,0,63,10,1,0,0,0,64,66,7,2,
        0,0,65,64,1,0,0,0,66,67,1,0,0,0,67,65,1,0,0,0,67,68,1,0,0,0,68,69,
        1,0,0,0,69,71,5,46,0,0,70,72,7,2,0,0,71,70,1,0,0,0,72,73,1,0,0,0,
        73,71,1,0,0,0,73,74,1,0,0,0,74,12,1,0,0,0,75,77,7,2,0,0,76,75,1,
        0,0,0,77,78,1,0,0,0,78,76,1,0,0,0,78,79,1,0,0,0,79,80,1,0,0,0,80,
        82,5,46,0,0,81,83,7,2,0,0,82,81,1,0,0,0,83,84,1,0,0,0,84,82,1,0,
        0,0,84,85,1,0,0,0,85,86,1,0,0,0,86,88,5,46,0,0,87,89,7,2,0,0,88,
        87,1,0,0,0,89,90,1,0,0,0,90,88,1,0,0,0,90,91,1,0,0,0,91,14,1,0,0,
        0,92,94,7,0,0,0,93,92,1,0,0,0,94,95,1,0,0,0,95,93,1,0,0,0,95,96,
        1,0,0,0,96,16,1,0,0,0,97,99,7,1,0,0,98,97,1,0,0,0,99,100,1,0,0,0,
        100,98,1,0,0,0,100,101,1,0,0,0,101,18,1,0,0,0,102,103,3,15,7,0,103,
        104,5,58,0,0,104,105,5,47,0,0,105,106,5,47,0,0,106,107,1,0,0,0,107,
        110,3,15,7,0,108,109,5,46,0,0,109,111,3,17,8,0,110,108,1,0,0,0,111,
        112,1,0,0,0,112,110,1,0,0,0,112,113,1,0,0,0,113,20,1,0,0,0,114,115,
        7,2,0,0,115,22,1,0,0,0,116,118,7,3,0,0,117,116,1,0,0,0,118,119,1,
        0,0,0,119,117,1,0,0,0,119,120,1,0,0,0,120,121,1,0,0,0,121,122,6,
        11,1,0,122,24,1,0,0,0,12,0,28,33,67,73,78,84,90,95,100,112,119,2,
        1,4,0,6,0,0
    ]

class mainLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    EMAIL = 1
    NATIONAL_NUMBER = 2
    POSTAL_CODE = 3
    DECIMAL_NUMBER = 4
    SOFTWARE_VERSION = 5
    WEBSITE_ADDRESS = 6
    DIGIT = 7
    WS = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "EMAIL", "NATIONAL_NUMBER", "POSTAL_CODE", "DECIMAL_NUMBER", 
            "SOFTWARE_VERSION", "WEBSITE_ADDRESS", "DIGIT", "WS" ]

    ruleNames = [ "LOCAL_SUBPART", "DOMAIN_SUBPART", "EMAIL", "NATIONAL_NUMBER", 
                  "POSTAL_CODE", "DECIMAL_NUMBER", "SOFTWARE_VERSION", "SUBPART1", 
                  "SUBPART2", "WEBSITE_ADDRESS", "DIGIT", "WS" ]

    grammarFileName = "main.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[4] = self.POSTAL_CODE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def POSTAL_CODE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            input.LT(1).getText() != "0" and input.LT(1).getText() != "2"
     


