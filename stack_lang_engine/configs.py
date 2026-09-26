regex_recognizers = {
    "STR": lambda val: val[1:-1],
    "INT": lambda val: int(val)
}

token_spec = [
    ("STR", r'"[^"]*"'),
    ("INT", r'\d+(\.\d+)?'),
    ("IDENT", r'\S+'),
    ("SKIP", r'[ \n\t]')
]
