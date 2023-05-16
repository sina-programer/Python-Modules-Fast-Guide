from optparse import OptionParser


parser = OptionParser()
parser.add_option("-n", "--name", dest="name", type="string", help="select a name (required)")
parser.add_option("-t", "--times", dest="times", type="int", help="Several times you want to try?")
options, args = parser.parse_args()

if not options.name:
    parser.error('name is not given')

print(options)
