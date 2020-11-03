import sys


def hello(name):
    print("hello + " + name)


if len(sys.argv) < 2:
    print("wrong,please again")
else:
    hello(sys.argv[1])

print('nothing')
