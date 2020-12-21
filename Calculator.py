class Calculator(object):
    def __init__(self):
        self.tokens = None
        self.current_token = None
        self.next_token = None

    @staticmethod
    def tokenize_string(original_string):
        tokenized_string = []
        seps = ['(', ')', '+', '-', '*', '/']
        s = ''
        for char in original_string:
            if char in seps and s != '':
                tokenized_string.extend([s, char])
                s = ''
            elif char in seps:
                tokenized_string.append(char)
            elif char != ' ':
                s += char
        print('Tokenized string: %s' % tokenized_string)
        return iter(tokenized_string)

    def evaluate(self, string):
        print(f'Evaluating {string}')
        self.tokens = self.tokenize_string(string)
        self._advance()

        # expr is the top level grammar. So we invoke that first.
        # it will invoke other function to consume tokens according to grammar rule.
        return self.expr()

    def _advance(self):
        self.current_token, self.next_token = self.next_token, next(self.tokens, None)

    def _accept(self, criteria):
        # if there is next token and token type matches
        if self.next_token and self.next_token == criteria:
            self._advance()
            return True
        else:
            return False

    def _expect(self, criteria):
        if not self._accept(criteria):
            raise SyntaxError('Expected ' + criteria)

    def expr(self):

        expr_value = self.term()
        while self._accept('+') or self._accept('-'):
            op = self.current_token
            right = self.term()
            if op == "+":
                expr_value += right
            elif op == '-':
                expr_value -= right
            else:
                print('EXPR should not arrive here!')

        return expr_value

    def term(self):

        term_value = self.factor()
        while self._accept('*') or self._accept('/'):
            op = self.current_token

            if op == '*':
                term_value *= self.factor()
            elif op == '/':
                term_value /= self.factor()
            else:
                print('TERM should not arrive here! ')

        return term_value

    def factor(self):
        if self.is_number():
            self._accept(f'{self.current_token}')
            return float(self.current_token)
        elif self._accept('('):
            expr_value = self.expr()

            self._expect(')')

            return expr_value
        else:
            print('Expect number or (')

    def is_number(self):
        try:
            i = float(self.current_token)
            return True
        except (ValueError, TypeError):
            return False


def sample_tests():
    print(f'{Calculator().evaluate("2 / 2 + 3 * 4 - 6")} = {7}')
    # print(f'{Calculator().evaluate("3 * 4 + 3 * 7 - 6")} = {27}')
    # print(f'{Calculator().evaluate("1 + 1")} = {2}')
    # print(f'{Calculator().evaluate("((((1)*2)))")} = {2}')
    # print(f'{Calculator().evaluate("(((((((5)))))))")} = {5}')
    # print(f'{Calculator().evaluate("2*(2*(2*(2*1)))")} = {16}')
    # print(f'{Calculator().evaluate("3 * (4 + 7) - 6")} = {27}')
