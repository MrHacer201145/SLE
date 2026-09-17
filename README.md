# About
SLE (Stack Lang Engine) is a simple tool for creating 
stack-oriented DSL or even small programming languages

# Example of usage
```py
import stack_lang_engine as sle

eng = sle.StackEngine()

eng.add_word("print", lambda: print(eng.stack.pop()))

eng.exec('"test" print') # Will print "test"
```
# License
SLE is licensed under MIT License