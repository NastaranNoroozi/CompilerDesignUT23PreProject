
from antlr4 import *
if "." in __name__:
    from .PasswordParser import PasswordParser
else:
    from PasswordParser import PasswordParser

# This class defines a complete listener for a parse tree produced by PasswordParser.
class PasswordListener(ParseTreeListener):

    # Enter a parse tree produced by PasswordParser#palindrome.
    def enterPalindrome(self, ctx:PasswordParser.PalindromeContext):
        pass

    # Exit a parse tree produced by PasswordParser#palindrome.
    def exitPalindrome(self, ctx:PasswordParser.PalindromeContext):
        pass


    # Enter a parse tree produced by PasswordParser#entry.
    def enterEntry(self, ctx:PasswordParser.EntryContext):
        pass

    # Exit a parse tree produced by PasswordParser#entry.
    def exitEntry(self, ctx:PasswordParser.EntryContext):
        pass



del PasswordParser
