import sys
from optparse import OptionParser

from common.read_input import read_rectangles

from naive import NaiveRectangleFit
from nfdh import NextDecreasingRectangleFit
from ffdh import FirstDecreasingRectangleFit

def choose_algorithm(identifier):
    return {
        'naive': NaiveRectangleFit,
        'nfdh': NextDecreasingRectangleFit,
        'ffdh': FirstDecreasingRectangleFit
    }[identifier]

def start():
    parser = OptionParser()
    parser.add_option(
        '-t', '--test',
        help='Just test the given algorithm with WIDTH set',
        type='float',
        metavar='WIDTH')
    return parser.parse_args()

options, args = start()

if len(args) < 1:
    print 'You must specify at least an algorithm (naive, nfdh, ffdh, rf).'
    sys.exit(1)

algorithm = choose_algorithm(args[0])

if not algorithm:
    print 'Invalid algorithm: %s' % (algorithm)
    sys.exit(1)    

rectangles = read_rectangles()
if options.test:
    algorithm_instance = algorithm(rectangles)
    print algorithm_instance(options.test, True)
else:
    pass
