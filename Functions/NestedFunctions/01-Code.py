def calc():
    x = 10
    y = 12
    def add():
        return x + y

    def sub():
        return x - y

    def show_result(result):
        return result

    # print("Sum is",add())
    return add, sub, show_result

def main():
    x,y,z = calc()
    # print("Sum is",x())
    # print(x[0]())
    print("Sum is",x())
    print("Diff is",y())

    print(z("This is calc demo"))

main()