
from antlr4 import *
if "." in __name__:
    from .PasswordParser import PasswordParser
else:
    from PasswordParser import PasswordParser

# This class defines a complete generic visitor for a parse tree produced by PasswordParser.

class PasswordVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PasswordParser#palindrome.
    def visitPalindrome(self, ctx:PasswordParser.PalindromeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PasswordParser#entry.
    def visitEntry(self, ctx:PasswordParser.EntryContext):
        return self.visitChildren(ctx)



del PasswordParser
