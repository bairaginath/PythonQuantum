__author__ = 'veradocs-web'


with open('simple_module.py') as f:
     contents = f.read()

code_obj = compile(contents, 'simple_module.py', 'exec')
exec(code_obj)

an_expression = "5+5"
code_obj = compile(an_expression, '<string>', 'eval')
print (eval(code_obj))

code_obj = compile(an_expression, '<string>', 'single')
exec(code_obj)

