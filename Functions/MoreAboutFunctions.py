# Global Scope
a = 10
b = 12

def add():
    # Local Scope
    c = a + b
    print("Sum is",c)

def sub():
    c = a - b
    print("Diff is",c)

add()
sub()