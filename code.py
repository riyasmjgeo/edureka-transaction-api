import argparse

# Getting inpus from user
parser = argparse.ArgumentParser(description="Simple Calculator")
parser.add_argument("action", type=str, 
                    help="Choose 'add' for Addition, 'sub' for Subtraction, 'div' for Division, and 'mul' for Multiplication")
parser.add_argument("x", type=float, help="Value of X")
parser.add_argument("y", type=float, help="Value of Y")
args = parser.parse_args()

# function for addition -<TBD>

# function for subtraction -<TBD>

# function for division -<TBD>

# function for multiplication -<TBD>