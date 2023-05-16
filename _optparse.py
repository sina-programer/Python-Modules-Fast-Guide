from optparse import OptionParser


parser = OptionParser()
parser.add_option("-n", "--name", dest="name", type="string", help="select a name (required)")
parser.add_option("-t", "--times", dest="times", type="int", help="Several times you want to try?")

parser.add_option("-o", "--on", action="store_true", dest="state")
parser.add_option("-f", "--off", action="store_false", dest="state")

options, args = parser.parse_args()

if not options.name:
    parser.error('name is not given')

if options.state:
    print('you turned the state on (-o | --on)')
else:
    print('you turned the state off (-f | --off)')

print(options)
