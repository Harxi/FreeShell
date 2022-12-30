import os

if "bin" not in os.listdir():
	os.mkdir("bin")
	os.chdir("bin")
	with open("commands.json", "w") as f:
		f.write("""{
	"echo": {
		"filename": "echo.py",
		"permission": 1,
		"package": "standard"
	}
}
""")
	with open("echo.py", "w") as f:
		f.write("""if len(args) > 1:
	print(TMA())
else:
	if "h" in args or "help" in args:
		print('Usage: echo [string]\\n    -h/--help - show this menu')
	elif len(args) < 1:
		print()
	else:
		print(args['0'])""")
	os.chdir("..")
		
if "config" not in os.listdir():
	os.mkdir("config")
	os.chdir("config")
	with open("error.py", "w") as f:
		f.write("""def CNF():
	return f"{name}: command not found"

def TMA():
	return f"{name}: too many arguments"

def PD():
	return f"{name}: permission denied"

def IBC():
	return f"{name}: incorrect build of command" """)
	
	with open("fsh.py", "w") as f: pass
	with open("fshin.py", "w") as f:
		f.write('fshin = f"{path} $ "')
