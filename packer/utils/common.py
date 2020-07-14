import os
import sys


def hello_world(message):
    output = "Hello " + message
    return output


def python_info():
    print("===> Python locations: ")
    for idx, i in enumerate(sys.path):
        print(str(idx)+'. '+i)

def lstGenerator(lst_path, folder_path):
    with open(lst_path, 'w') as f:
        for root, dirs, files in os.walk(folder_path, topdown=False):
            for name in files:
                f.write(os.path.join(root, name)+'\n')

def mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)

if __name__ == '__main__':
    lstGenerator('./lst.txt', r'C:\Users\41251\OneDrive\图片')