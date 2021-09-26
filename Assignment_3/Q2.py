import argparse

# --------------------------------------------------------------------
# What are the command line arguments required? 
parser = argparse.ArgumentParser()

parser.add_argument(
    '-n', 
    '--numbers',
    nargs='+', #makes all command line arguments to list 
    help='Numbers separated by spaces',
    required= True,
    )
parser.add_argument(
    '-op',
    "--operation",
    help = "sum, prod, rec",
    required= True
    )
# --------------------------------------------------------------------

#Grab command line arguments
args = parser.parse_args()

# Sum, product and reciprocal functions -------------------------------
def f(*x,**y):
    def s1(x):
        s = 0
        if x:
            for i in x:
                s += i
            return s

    def p1(x):
        s = 1
        if x:
            for i in x:
                s*= i
            return s

    def rec(x):
        return s1(list(map(lambda v: 1/v, x)))

    if y["action"] == "sum":
        return s1(*x)
    if y["action"] == "prod":
        return p1(*x)
    if y["action"] == "rec":
        return rec(*x)
    else:
        return f"bad argument: {y}"
# --------------------------------------------------------------------

if __name__ == '__main__':
    #Print the program's result
    print(f(map(int,args.numbers), action = args.operation))
                