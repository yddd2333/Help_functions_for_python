from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from packer.utils.common import hello_world
from packer.utils.common import python_info
from packer.utils.common import lstGenerator


def parse_args():
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter,
                            conflict_handler='resolve')
    parser.add_argument("-lg", action="store_true", help="type your message")
    parser.add_argument("--folderPath", "-f", help="type your message", default="./test")
    parser.add_argument("--listPath", "-l", help="type your message", default="./lst.txt")
    args = parser.parse_args()
    return args


def main(args):
    if args.lg:
        lstGenerator(lst_path=args.listPath, folder_path=args.folderPath)
        print('Images from \"%s\" has generated list in \"%s\"' %(args.folderPath, args.listPath))
    else:
        output = hello_world('')
        python_info()
        print(output)


if __name__ == "__main__":
    main(parse_args())
