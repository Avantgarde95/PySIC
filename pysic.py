import sys, os
from pysic.lib.shell import PsShell
from pysic.lib.parse import PsParser
from pysic.lib.interpret import PsInterpreter
from pysic.lib.exception import PsParserInterrupt

def print_usage():
    print 'Usage : python pysic.py source.psc\n'

if __name__ == '__main__':
    # check the number of arguments
    if len(sys.argv) == 1:
        print_usage()
        sys.exit(1)

    # check the extension
    filename = sys.argv[1]

    if not filename.endswith('.psc'):
        print "Error : Source extension should be '.psc'!"
        sys.exit(2)

    # open the source file
    try:
        #curpath = os.path.dirname(__file__)
        #relpath = os.path.relpath(filename, '.')
        #fullpath = os.path.join(curpath, filename)
        # print curpath, fullpath
        p = open(filename, 'r')
    except IOError:
        print "Error : Can't open the source file!"
        sys.exit(3)

    source = p.read()
    p.close()

    ps = PsShell()
    parser = PsParser()
    interpreter = PsInterpreter(
        func = {
            'stdin' : ps.input,
            'stdout' : ps.output,
            'stderr' : ps.error
        }
    )

    ps.start()

    flag_interpret = True

    try:
        tokendata = parser.parse(source)
    except PsParserInterrupt as e:
        ps.error(e)
        flag_interpret = False

    if flag_interpret:
        interpreter.digest(*tokendata)
        interpreter.run()

    ps.end()

    sys.exit(0)
