import random

class Expression:

    def __init__(self, op, *args):
        self.op = str(op)
        self.args = args

    def __invert__(self):
        return Expression('~', self)

    def __and__(self, rhs):
        return Expression('&', self, rhs)

    def __or__(self, rhs):
        return Expression('|', self, rhs)

    def __rand__(self, lhs):
        return Expression('&', lhs, self)

    def __ror__(self, lhs):
        return Expression('|', lhs, self)

    def __hash__(self):
        return hash(self.op) ^ hash(self.args)

    def __repr__(self):
        op = self.op
        args = [str(arg) for arg in self.args]
        if op.isidentifier():  # x
            return op
        elif len(args) == 1:  # ~x
            return op + args[0]
        else:  # (x | y)
            edited_args = []
            for arg in args:
                if str(arg[-1]) == ')':
                    edited_args.append(arg[1:len(arg)-1])
                else:
                    edited_args.append(arg)
            opp = (' ' + op + ' ')
            return '(' + opp.join(edited_args) + ')'


def clause_symbols(clause):
    if not isinstance(clause, Expression):
        return set()
    elif isinstance(clause.op, str) and clause.op[:1].isalpha() and clause.op[0].isupper():
        return {clause}
    else:
        symbols = set()
        for arg in clause.args:
            for symbol in clause_symbols(arg):
                symbols.add(symbol)
        return symbols

def pl_true(exp, model={}):
    if exp in (True, False):
        return exp
    op, args = exp.op, exp.args
    if isinstance(op, str) and op[:1].isalpha() and op[0].isupper():
        return model.get(exp)
    elif op == '~':
        p = pl_true(args[0], model)
        if p is None:
            return None
        else:
            return not p
    elif op == '|':
        result = False
        for arg in args:
            p = pl_true(arg, model)
            if p is True:
                return True
            if p is None:
                result = None
        return result
    elif op == '&':
        result = True
        for arg in args:
            p = pl_true(arg, model)
            if p is False:
                return False
            if p is None:
                result = None
        return result
    else:
        raise ValueError('Illegal operator CNF' + str(exp))

