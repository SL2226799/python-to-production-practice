############################
# ---Type Hinting -----
############################

############################
name = "Peter"

if name == "Peter":
    print("This is an ENglish name")
elif name == "Pedro":
    print("This is an Hispanic name")
else:
    print("Unknown")


def add_numbers(a: float = 1, b: float = 2):
    return a + b


result = add_numbers(3, 4)


def product(a: float = 1, b: float = 2):
    return a * b


result = product(3, 4)
