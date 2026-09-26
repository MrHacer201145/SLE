import re


class UndefinedWordError(BaseException):
    "Exception for words that do not exist"


class StackEngine:
    def __init__(self, 
                words={},
                stack=[],
                recognizers={},
                regex_recognizers={},
                undefined_error_msg=lambda word: f"Word '{word}' is not defined",
                token_spec = [
                    ("STR", r'"[^"]*"'),
                    ("INT", r'\d+(\.\d+)?'),
                    ("IDENT", r'\S+'),
                    ("SKIP", r'[ \n\t]')
                ]
            ):
        self.words = words
        self.stack = stack
        self.error_msg = undefined_error_msg
        self.recognizers = recognizers
        self.regex_recognizers = regex_recognizers
        self.token_spec = token_spec

    def add_word(self, name: str, func) -> None:
        self.words[name] = func
    def del_word(self, name: str) -> None:
        del self.words[name]

    def reg_word(self, name):
        def wrapper(func):
            self.words[name] = func
        return wrapper

    def add_recognizer(self, name: str, pattern: str, on_regex: callable, on_interpret: callable) -> None:
        self.token_spec.insert(0, (name, pattern))
        self.recognizers[name] = on_interpret
        self.regex_recognizers[name] = on_regex

    def new_stack(self, name, content=[], create_api=False):
        self.__dict__[name] = content

        if create_api:
            self.__dict__[f'{name}_push'] = lambda val: self.__dict__[name].append(val)
            self.__dict__[f'{name}_pop'] = lambda: self.__dict__[name].pop()

    def push(self, value: any) -> None:
        self.stack.append(value)
    def pop(self) -> any:
        return self.stack.pop()
    def clear(self) -> None:
        self.stack.clear()
    def latest(self) -> any:
        return self.stack[-1]

    def _parse(self, text: str) -> list[tuple[str, any]]:
        tokens = []
        tok_regex = "|".join(f"(?P<{pair[0]}>{pair[1]})" for pair in self.token_spec)

        for mo in re.finditer(tok_regex, text):
            kind, val = mo.lastgroup, mo.group()

            if kind == "SKIP": continue
            elif kind in self.regex_recognizers:
                val = self.regex_recognizers[kind](val)
            elif kind == "STR": val = val[1:-1]
            elif kind == "INT": val = int(val)
            tokens.append((kind, val))

        return tokens

    def exec(self, text: str) -> None:
        "Interprets given string"
        words = self._parse(text)

        for word in words:
            kind, val = word
            if kind == "IDENT":
                if val in self.words:
                    self.words[val]()
                else:
                    raise UndefinedWordError(self.error_msg(val))
            elif kind in self.recognizers:
                self.recognizers[kind](val)
            else:
                self.stack.append(val)
