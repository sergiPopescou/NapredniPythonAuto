
from enum import Enum


class Token:
    class Type(Enum):
        INTEGER = 0
        MUL = 1
        DIV = 2
        LPAREN = 3
        RPAREN = 4

    def __init__(self, type, text):
        self.type = type
        self.text = text

    def __str__(self):
        return f'`{self.text}`'


def lex(input):
    result = []

    i = 0
    while i < len(input):
        if input[i] == '*':
            result.append(Token(Token.Type.MUL, '*'))
        elif input[i] == '/':
            result.append(Token(Token.Type.DIV, '/'))
        elif input[i] == '(':
            result.append(Token(Token.Type.LPAREN, '('))
        elif input[i] == ')':
            result.append(Token(Token.Type.RPAREN, ')'))
        else:  # must be a number
            digits = [input[i]]
            for j in range(i + 1, len(input)):
                if input[j].isdigit():
                    digits.append(input[j])
                    i += 1
                else:
                    result.append(Token(Token.Type.INTEGER,
                                        ''.join(digits)))
                    break
        i += 1

    return result
