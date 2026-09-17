import re

class StackEngine:
    def __init__(self, words={}, stack=[]):
        self.words = words
        self.stack = stack

    def add_word(self, name, func):
        self.words[name] = func
    def del_word(self, name):
        del self.words[name]

    def new_stack(self, name, content=[]):
        self.__dict__[name] = content

    @staticmethod
    def _parse(text):
        tokens = []
        token_spec = [
            ("STR", r'"[^"]*"'),
            ("NUM", r'\d+(\.\d+)?'),
            ("IDENT", r'[a-zA-Z_][a-zA-Z0-9_]*'),
            ("SKIP", r'[ \n\t]')
        ]
        tok_regex = "|".join(f"(?P<{pair[0]}>{pair[1]})" for pair in token_spec)

        for mo in re.finditer(tok_regex, text):
            kind, val = mo.lastgroup, mo.group()

            if kind == "SKIP": continue
            elif kind == "STR": val = val[1:-1]
            elif kind == "NUM": val = int(val)
            tokens.append((kind, val))

        return tokens

    def exec(self, text):
        words = self._parse(text)

        for word in words:
            kind, val = word
            if kind == "IDENT":
                if val in self.words:
                    self.words[val]()
            else:
                self.stack.append(val)
