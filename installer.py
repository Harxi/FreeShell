import os

if "bin" not in os.listdir():
	os.mkdir("bin")

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