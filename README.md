# What is "Stack Lang Engine"
SLE (Stack Lang Engine) is a simple tool for creating 
stack-oriented DSL or even small programming languages.

# Usage
## Firstly
Of course we need to import a module, and create object with type
"StackEngine"
```py
import stack_lang_engine as sle

eng = sle.StackEngine()
```

## Definition of words:
This is how to define/delete words in StackEngine
```py
# Define new word
eng.add_word("print", lambda: print(eng.pop()))

# Delete word
eng.del_word("print")
```

## How to execute text (given as string)
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

## Usefull APIs
```py
# Instead of writing "eng.stack.pop" or more we can use builtin
# methods like eng.(push, pop, clear)

eng.push(10) # For example
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
print(eng.stack) # It will work correctly, so in stack only 10 and 20
```

## How to write more short code in this engine
```py
# For example we can set words dict instead of creating each
# word over and over

eng = sle.StackEngine(words={
    "print": lambda: print(eng.pop())
})

# You can also read the interpreter's code itself on 
# GitHub to better understand how it works.
```
### Thanks for reading the documentation!

# License
SLE is licensed under GPLv3 License
