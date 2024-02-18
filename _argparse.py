from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-n", "--name", dest="name", type=str, help="select a name (required)")
parser.add_argument("-t", "--times", dest="times", type=int, help="Several times you want to try?")

parser.add_argument("-o", "--on", action="store_true", dest="state")
parser.add_argument("-f", "--off", action="store_false", dest="state")

args = parser.parse_args()

if not args.name:
    parser.error('name is not given')

if args.state:
    print('you turned the state on (-o | --on)')
else:
    print('you turned the state off (-f | --off)')

print(args)
