x = 4
print(f"Global Var(x) = {x}")

def localvar():
    # x = 12 local variable
    global x
    print(f"Local Var(x) = {x}")
    x = 6

localvar()
print(f"Global Var(x) = {x}")