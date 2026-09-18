import re


class UndefinedWordError(BaseException):
    "Exception for words that do not exist"


class StackEngine:
    def __init__(self, words={}, stack=[], undefined_error_msg=lambda word: f"Word '{word}' is not defined"):
        self.words = words
        self.stack = stack
        self.error_msg = undefined_error_msg

    def add_word(self, name, func):
        self.words[name] = func
    def del_word(self, name):
        del self.words[name]

    def new_stack(self, name, content=[], create_api=False):
        self.__dict__[name] = content

        if create_api:
            self.__dict__[f'{name}_push'] = lambda val: self.__dict__[name].append(val)
            self.__dict__[f'{name}_pop'] = lambda: self.__dict__[name].pop()

    def push(self, value):
        self.stack.append(value)
    def pop(self):
        return self.stack.pop()
    def clear(self):
        self.stack.clear()

    @staticmethod
    def _parse(text):
        tokens = []
        token_spec = [
            ("STR", r'"[^"]*"'),
            ("INT", r'\d+(\.\d+)?'),
            ("IDENT", r'[a-zA-Z_][a-zA-Z0-9_]*'),
            ("SKIP", r'[ \n\t]')
        ]
        tok_regex = "|".join(f"(?P<{pair[0]}>{pair[1]})" for pair in token_spec)

        for mo in re.finditer(tok_regex, text):
            kind, val = mo.lastgroup, mo.group()

            if kind == "SKIP": continue
            elif kind == "STR": val = val[1:-1]
            elif kind == "INT": val = int(val)
            tokens.append((kind, val))

        return tokens

    def exec(self, text):
        "Interprets given string"
        words = self._parse(text)

        for word in words:
            kind, val = word
            if kind == "IDENT":
                if val in self.words:
                    self.words[val]()
                else:
                    raise UndefinedWordError(self.error_msg(val))
            else:
                self.stack.append(val)
