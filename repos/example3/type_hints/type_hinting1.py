# Video example of "magic" or unintuitive code,
# Which also doesn't provide autocompletion in code editors

class Duck:
	def __init__(self):
	
	def __getattr__(self, attr):
		if attr == "quack":
			return lambda: print("quack")
		elif attr == "swim":
			return lambda: print("splash")
		else:
			raise AttributeError
		
var: int = 1