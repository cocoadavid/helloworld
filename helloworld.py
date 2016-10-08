import sys

def world():
    no_name = len(sys.argv) <= 1
    if no_name:
        print("World!")

def username():
    there_is_name = len(sys.argv) > 1
    if there_is_name:
        for arg in sys.argv[1: ]:
            print(arg + "!")

print("Hello ", end="")
world()
username()