from lark import Lark, Transformer, Token

class ToJson(Transformer):
	def string(self, s):
		(s,) = s
		return s[1:-1]

	def integer(self, n):
		(n,) = n
		return int(n)
	
	def arg(self, n):
		if len(n) > 1:
			return {str(n[0]): str(n[1].children[0])}
		else:
			return {str(n[0]): None}
	
	def command(self, n):
		i = 0
		args = {}
		for ind, x in enumerate(n[1:len(n)]):
			if not isinstance(x, dict):
				n[ind+1] = {str(i): x}
				i += 1
			args = args | n[ind+1]
		return {"name": str(n[0]), "args": args}
	
class Grammar:
	grammar = Lark(r"""
    start: instruction*
    ?instruction: command
        | string
        | integer
    
    arg: ("-")+ NAME types?
    !types: (string | integer | NAME)?
    NAME: /[a-zA-Z]\w*/
    command: NAME (arg | string | integer)*
    
    string: ESCAPED_STRING
    integer: SIGNED_NUMBER
    
    COMMENT: "#" /[^\n]/*

    %import common.ESCAPED_STRING
    %import common.SIGNED_NUMBER
    %import common.WS
    
    %ignore COMMENT
    %ignore WS
""", start='start')

	@staticmethod
	def analyse(text):
		return ToJson().transform(Grammar.grammar.parse(text)).children