
from enum import Enum
from drugi_dan.interpreter.lekser import lex, Token

class Integer:
    def __init__(self, value):
        self.value = value


class BinaryOperation:
    class Type(Enum):
        MULTIPLICATION = 0
        DIVISION = 1

    def __init__(self):
        self.type = None
        self.left = None
        self.right = None

    @property
    def value(self):
        if self.type == self.Type.MULTIPLICATION:
            return self.left.value * self.right.value
        elif self.type == self.Type.DIVISION:
            # if self.right.value == 0:
            #     self.right.value = 1
            return self.left.value / self.right.value


def parse(tokens):
    result = BinaryOperation()
    have_lhs = False
    i = 0
    while i < len(tokens):
        token = tokens[i]

        if token.type == Token.Type.INTEGER:
            integer = Integer(int(token.text))
            if not have_lhs:
                result.left = integer
                have_lhs = True
            else:
                result.right = integer
        elif token.type == Token.Type.MUL:
            result.type = BinaryOperation.Type.MULTIPLICATION
        elif token.type == Token.Type.DIV:
            result.type = BinaryOperation.Type.DIVISION
        elif token.type == Token.Type.LPAREN:  # note: no if for RPAREN
            j = i
            while j < len(tokens):
                if tokens[j].type == Token.Type.RPAREN:
                    break
                j += 1
            # preprocess subexpression
            subexpression = tokens[i + 1:j]
            element = parse(subexpression)
            if not have_lhs:
                result.left = element
                have_lhs = True
            else:
                result.right = element
            i = j  # advance
        i += 1
    return result


def eval(input):
    tokens = lex(input)
    print(' '.join(map(str, tokens)))

    parsed = parse(tokens)
    print(f'{input} = {parsed.value}')


if __name__ == '__main__':
    eval('(3*4)/(12/2)')
    eval('1*(3/4)')
    eval('10*(32/0)')
