# Demonstrates defining a function with a return value

def main():
    x = int(input("what is x ? "))
    print("x squared is", square(x))

def square(n):
    return n * n

main()