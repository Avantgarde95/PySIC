# parse the source

from exception import PsParserInterrupt

# data about number of arguments (ex. 'add e e e' -> 3)
_data_arglen = { 
    'in' : 1,
    'out' : -1,
    '#' : -1,
    'add' : 3,
    'sub' : 3,
    'mul' : 3,
    'div' : 3,
    'if' : 4,
    'if=' : 4,
    'if==' : 4,
    'if>' : 4,
    'if<' : 4,
    'if>=' : 4,
    'if<=' : 4,
    'if!=' : 4,
    'let' : 2,
    'block' : 1,
    'goto' : 1,
    'pass' : 0,
    'exit' : 0
}

_data_keyword = _data_arglen.keys()

class PsParser(object):
    ''' Pysic parser '''
    def __init__(self):
        ''' class initialization '''
        self.data_arglen = _data_arglen
        self.data_keyword = _data_keyword

    def parse_token(self, token):
        ''' parse a token and return it with its type'''
        # 345, -35, ... -> int
        try:
            return int(token), 'int'
        except ValueError:
            pass

        # "abc", "An^apple", ... -> str
        if token[0] == '"' and token[-1] == '"':
            return token.strip('"').replace('^', ' '), 'str'

        # else -> name
        return token, 'name'

    def check_syntax(self, keyword, args):
        ''' check the syntax of each line '''
        # check whether the given keyword exists
        if keyword not in self.data_keyword:
            return False

        # check the number of arguments (-1 : variable number)
        arglen = self.data_arglen[keyword]

        if arglen == -1:
            return True
        else:
            return len(args) == arglen

    def parse(self, source):
        ''' parse the given source '''
        data_lines = filter(None, map(str.strip, source.split('\n')))
        data_blocks = {}
        data_parsed = []

        for i, line in enumerate(data_lines):
            keyword, arguments = line.split()[0], line.split()[1:]

            if not self.check_syntax(keyword, arguments):
                raise PsParserInterrupt()
            
            # pass the comments
            if keyword == '#':
                data_parsed.append(('pass', ()))
            
            # hook the block declarations and add them to the dictionary
            # (and the line is converted to the 'pass' statement)
            elif keyword == 'block': 
                data_blocks[arguments[0]] = i
                data_parsed.append(('pass', ()))

            # else, just push the tokens into the stack
            else:
                data_parsed.append(
                    (keyword, tuple(map(self.parse_token, arguments)))
                )
        
        return data_blocks, data_parsed

if __name__ == '__main__':
    source =\
    '''
    let a 1
    let b 2

    in c
    in d

    add e a c
    add f b d

    if e f B1 B2

    block B1
    let res "="

    block B2
    let res "!="

    out "Output^:^" c "^+^1^" res "^" d "^+2"
    '''

    parser = PsParser()
    b, p = parser.parse(source)

    print '- Test source :'
    print source

    print '\n- Dict. of blocks :'
    print b

    print '\n- Parsed source :'

    for i, data in enumerate(p):
        print 'line %d -' % i, str(data)
