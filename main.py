import json
import ebnf

path = "~"
user = 1
with open("bin/commands.json", "r") as f:
	commands = json.load(f)

for name in ["error.py", "fshin.py", "fsh.py"]:
	with open(f"config/{name}", "r") as f:
		exec(f.read())

while True:
	command = input(fshin)
	parse = ebnf.Grammar.analyse(command)
	name = parse[0]["name"]
	args = parse[0]["args"]
	try:
		try:
			commandInfo = commands[name]
			commandFile = commandInfo["filename"]
			permission = commandInfo["permission"]
			package = commandInfo["package"]
		except:
			print(IBC())
			continue
			
		if user >= permission:
			with open(f"bin/{commandInfo['filename']}", "r") as f:
				exec(f.read())
		else:
			print(PD())
			
	except KeyError as err:
		print(CNF())