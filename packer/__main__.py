from argparse import ArgumentParser,ArgumentDefaultsHelpFormatter
from packer.utils.common import hello_world


def parse_args():
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter,
                            conflict_handler='resolve')
    parser.add_argument("--mess","-m",help="type your message", default="packer main")
    args = parser.parse_args()
    return args


def main(args):
    message = args.mess
    output = hello_world(message)
    print(output)


if __name__ == "__main__":
    main(parse_args())