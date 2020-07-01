import os
import sys


def hello_world(message):
    output = "Hello " + message
    return output


def python_info():
    print("===> Python locations: ")
    for idx, i in enumerate(sys.path):
        print(str(idx)+'. '+i)


def mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)
