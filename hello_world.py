def divide(a, b):
    return a/b

def multiply(a,b):
    return a*b

def subtract(a, b):
    return a - b
def add(a, b):
    return a + b



def main():
    print("Hello World!!")
    a, b = 10, 5
    print(f"Subtraction of {a} - {b} = {subtract(a, b)}")
    print(f"Additon of {a} + {b} = {add(a,b)}")
    print(f"Division of {a} / {b} = {divide(a, b)}")
    print(f"Multiply of {a} * {b} = {multiply(a,b)}")

if __name__ == '__main__':
    main()
