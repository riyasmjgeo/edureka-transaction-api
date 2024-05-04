import argparse

# Getting inpus from user
parser = argparse.ArgumentParser(description="Simple Calculator")
parser.add_argument("operation", type=str, 
                    help="Choose 'add' for Addition, 'sub' for Subtraction, 'div' for Division, and 'mul' for Multiplication")
parser.add_argument("x", type=float, help="Value of X")
parser.add_argument("y", type=float, help="Value of Y")
args = parser.parse_args()

# function for addition
def add(x=args.x, y=args.y):
    return x+y

# function for subtraction
def sub(x=args.x, y=args.y):
    return x - y

# function for division
def div(x=args.x, y=args.y):
    if y==0:
        print("Can't divide by zero")
        return None
    else:
        return x/y

# function for multiplication -<TBD>

result = eval(f"{args.operation}()")
print(f"The action {args.operation} between {args.x} and {args.y} resulted in {result}")
