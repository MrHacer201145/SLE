# What is "Stack Lang Engine"
SLE (Stack Lang Engine) is a zero-dependency, 
highly extensible engine for building stack-oriented DSLs and mini-languages.
It was designed to be a lightweight module while offering a useful set of built-in functions.

# Quick Example
```py
import package.stack_lang_engine as sle

eng = sle.StackEngine()

@eng.reg_word("+")
def add():
    b = eng.pop()
    a = eng.pop()
    eng.push(a + b)

eng.exec("10 20 +")
print(eng.latest())
```

# Documentation
## Import Module
Of course we need to import a module, and create object with type
"StackEngine"
```py
import stack_lang_engine as sle

eng = sle.StackEngine()
```

## Definition of words:
```py
# Define new word
@eng.reg_word("print")
def print_pop():
    print(eng.pop())

# or
# eng.add_word("print", lambda: print(eng.pop()))

# Delete word
eng.del_word("print")
```

## How to execute code (given as string)
```py
# If you use the default regex pattern, 
# it automatically recognizes whether it is a string or a number.
eng.exec('10 20 30 "40"')
```

## How to create stack and APIs for it
```py
# Create new stack, we can use "create_api" option
# to create eng.{name}_push, eng.{name}_pop() methods
# for object

eng.new_stack("stacky", create_api=True)
# now we have eng.stacky_push and eng.stacky_pop

eng.stacky_push(10)
print(eng.stacky)
eng.stacky_pop()
```

## Recognizers
```py
# We can create a new regex pattern, 
# and both the parser and the interpreter must handle it.

eng.add_recognizer(
    name="Test", # Name of recognizer
    pattern=r'Test', # Regex pattern
    on_regex=lambda val: val, # What parser should get (or do) when it parses it
    on_interpret=lambda val: print("Hello, Test!?"), # What interpreter should do when it gets it
)

# and if then we execute it will output
# "Hello, Test!?" when it interprets word
# with "Test" kind

eng.exec("Test 10 20")
print(eng.stack) # It will print [10, 20]
```

## Usefull APIs
```py
# Instead of writing "eng.stack.pop" or more we can use builtin
# methods like eng.(push, pop, clear, latest)

eng.push(10) # For example
```

### Thanks for reading the documentation!

# License
SLE is licensed under GPLv3 License
