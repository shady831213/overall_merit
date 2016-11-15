import unittest
import getopt
import sys
def parse(argv):
    #error
    try:
        opts, args = getopt.getopt(argv[1:], 'at:', ['all', 'test='])
    except getopt.GetoptError, err:
        print str(err)
        sys.exit(2)

    for a, v in opts :
        if a in ('-a', '--all') :
            runAll()
        elif a in ('-t', '--test') :
            run(v)

def runAll():
    """Run all Test"""
    tests = unittest.TestLoader().discover('.')
    unittest.TextTestRunner(verbosity=2).run(tests)

def run(testName):
    test = unittest.TestLoader().discover('.',testName)
    unittest.TextTestRunner(verbosity=2).run(test)

if __name__ == '__main__':
    parse(sys.argv)