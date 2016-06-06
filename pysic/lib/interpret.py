# interpret the parsed data

from exception import PsInterpreterInterrupt

class PsInterpreter(object):
    ''' Pysic interpreter '''
    def __init__(self, func, debug = False):
        ''' class initialization 
        * The argunemt 'func' should be a dict with three keys : 'stdin',
        'stdout', 'stderr'.
        '''
        self.var = {}
        self.block = {}
        self.data_parsed = []

        self.func = func

        self.line = 0 # index of the current line
        self.line_limit = 0 # (index of the last line) + 1

        self.debug = debug

    def input(self):
        ''' helper function for input support '''
        value = self.func['stdin']().strip()

        if value:
            # integer (3, -5, ...) -> integer
            try:
                return int(value)
            except ValueError:
                # "integer" ("3", "-5", ...) -> string
                try:
                    return int(value.strip('"'))
                # else -> string
                except ValueError:
                    return value
        else:
            # blank -> blank string
            return ''

    def output(self, data_values):
        ''' helper function for printing the data '''
        self.func['stdout'](*data_values)

    def error(self, message): 
        ''' print the message to stderr '''
        self.func['stderr'](message)

    def raise_exception(self, type_error, *args):
        ''' raise an exception to stop the interpreter '''
        if type_error == 'AssignError':
            message = "AssignError in line %d : You can't assign"\
                    ' a value to the constant!'\
                    % self.line
        
        elif type_error == 'VarError':
            message = "VarError in line %d : There doesn't exist"\
                    ' a variable with the name [%s]!'\
                    % (self.line, args[0])
        
        elif type_error == 'BlockError':
            message = "BlockError in line %d : There doesn't exist"\
                    ' a block with the name [%s]!'\
                    % (self.line, str(args[0]))
        
        elif type_error == 'TypeError':
            message = "TypeError in line %d : Type of [%s] should be"\
                    ' %s!'\
                    % (self.line, str(args[0]), args[1])
        
        else:
            message = "Unidentified Error in line %d!"

        raise PsInterpreterInterrupt(message)

    def get_var(self, elem):
        ''' If the given element is a name, then lookup the variable
        table and return its value. Otherwise, just return the value
        of the element directly.
        '''
        v, t = elem
        
        # name -> lookup the variable table
        if t == 'name':
            try:
                return self.var[v]
            except KeyError:
                self.raise_exception('VarError', v)

        # int or str -> return the value directly
        else:
            return v

    def get_block(self, elem):
        ''' Lookup the block table and return its value (= line number) '''
        v, t = elem

        try:
            return self.block[v]
        except KeyError:
            self.raise_exception('BlockError', v)

    def check_type(self, value, value_type):
        ''' check the type of the value and raise exception if wrong '''
        if value_type == 'int':
            if isinstance(value, (int, long)):
                return True
            else:
                self.raise_exception('TypeError', value, 'int')
                return False
        elif value_type == 'str':
            if isinstance(value, str):
                return True
            else:
                self.raise_exception('TypeError', value, 'int')
                return False
        else:
            return True

    def interpret(self):
        ''' main routine for interpreting '''
        self.line_limit = len(self.data_parsed)
        self.line = 0

        if self.debug:
            print '*** Debug mode ***'
            print '- Lines = %d' % self.line_limit
            print '- Blocks = %s\n' % str(self.block)

        while self.line < self.line_limit:
            keyword, arguments = self.data_parsed[self.line]

            if self.debug:
                print '---------'
                print '- line = %d' % self.line
                print '- keyword = %s' % keyword
                print '- arguments = %s' % ' '.join(map(str, arguments))
                print '- variables = %s' % str(self.var)
                print '---------'

            # I/O
            if keyword == 'in':
                name, type_name = arguments[0]

                if type_name == 'name':
                    self.var[name] = self.input()    
                else:
                    self.raise_exception('AssignError')

            elif keyword == 'out':
                data_output = []

                for arg in arguments:
                    value = self.get_var(arg)
                    data_output.append(value)

                self.output(data_output)

            # variable
            elif keyword == 'let':
                name, type_name = arguments[0]

                if type_name == 'name':
                    value = self.get_var(arguments[1])
                    self.var[name] = value
                else:
                    self.raise_exception('AssignError')

            # flow control
            elif keyword == 'goto':
                line_block = self.get_block(arguments[0])
                self.line = line_block              
                continue

            elif keyword == 'pass':
                pass

            elif keyword == 'exit':
                break

            # conditional
            elif keyword == 'if' or keyword == 'if=' or keyword == 'if==':
                value_1 = self.get_var(arguments[0])
                value_2 = self.get_var(arguments[1])

                if value_1 == value_2:
                    line_block = self.get_block(arguments[2])
                    self.line = line_block
                    continue
                else:
                    line_block = self.get_block(arguments[3])
                    self.line = line_block
                    continue

            elif keyword == 'if>':
                value_1 = self.get_var(arguments[0])
                value_2 = self.get_var(arguments[1])

                if value_1 > value_2:
                    line_block = self.get_block(arguments[2])
                    self.line = line_block
                    continue
                else:
                    line_block = self.get_block(arguments[3])
                    self.line = line_block
                    continue
            
            elif keyword == 'if<':
                value_1 = self.get_var(arguments[0])
                value_2 = self.get_var(arguments[1])

                if value_1 < value_2:
                    line_block = self.get_block(arguments[2])
                    self.line = line_block
                    continue
                else:
                    line_block = self.get_block(arguments[3])
                    self.line = line_block
                    continue

            elif keyword == 'if>=':
                value_1 = self.get_var(arguments[0])
                value_2 = self.get_var(arguments[1])

                if value_1 >= value_2:
                    line_block = self.get_block(arguments[2])
                    self.line = line_block
                    continue
                else:
                    line_block = self.get_block(arguments[3])
                    self.line = line_block
                    continue

            elif keyword == 'if<=':
                value_1 = self.get_var(arguments[0])
                value_2 = self.get_var(arguments[1])

                if value_1 <= value_2:
                    line_block = self.get_block(arguments[2])
                    self.line = line_block
                    continue
                else:
                    line_block = self.get_block(arguments[3])
                    self.line = line_block
                    continue

            elif keyword == 'if!=':
                value_1 = self.get_var(arguments[0])
                value_2 = self.get_var(arguments[1])

                if value_1 != value_2:
                    line_block = self.get_block(arguments[2])
                    self.line = line_block
                    continue
                else:
                    line_block = self.get_block(arguments[3])
                    self.line = line_block
                    continue

            # arithmetic
            elif keyword == 'add':
                name, type_name = arguments[0]

                value_1 = self.get_var(arguments[1])
                value_2 = self.get_var(arguments[2])

                self.check_type(value_1, 'int')
                self.check_type(value_2, 'int')

                self.var[name] = value_1 + value_2

            elif keyword == 'sub':
                name, type_name = arguments[0]

                value_1 = self.get_var(arguments[1])
                value_2 = self.get_var(arguments[2])

                self.check_type(value_1, 'int')
                self.check_type(value_2, 'int')

                self.var[name] = value_1 - value_2

            elif keyword == 'mul':
                name, type_name = arguments[0]

                value_1 = self.get_var(arguments[1])
                value_2 = self.get_var(arguments[2])

                self.check_type(value_1, 'int')
                self.check_type(value_2, 'int')

                self.var[name] = value_1 * value_2

            elif keyword == 'div':
                name, type_name = arguments[0]

                value_1 = self.get_var(arguments[1])
                value_2 = self.get_var(arguments[2])

                self.check_type(value_1, 'int')
                self.check_type(value_2, 'int')

                self.var[name] = value_1 / value_2

            # future...
            else:
                pass

            # move to the next line
            self.line += 1

    def digest(self, data_blocks, data_parsed):
        ''' push new source codes into the interpreter '''
        self.block.update(data_blocks)
        self.data_parsed += data_parsed

    def run(self):
        ''' start the interpreter '''
        try:
            self.interpret()
        except PsInterpreterInterrupt as e:
            self.error(e)

if __name__ == '__main__':
    def demo_input():
        return raw_input('Input) ')

    def demo_output(*s):
        print 'Output) %s' % ''.join(map(str, s))

    def demo_error(s):
        print 'Error) %s' % s
    
    data_blocks = {
        'B1' : 4,
        'B2' : 7,
        'Final' : 10
    }
    
    data_parsed = [
        ('out', (('Input A :', 'str'),)),
        ('in', (('a', 'name'),)),
        ('let', (('b', 'name'), (1, 'int'))),
        ('if>',
         (('a', 'name'), ('b', 'name'), ('B1', 'name'), ('B2', 'name'))),
        ('pass', ()),
        ('let', (('c', 'name'), ('A > 1', 'str'))),
        ('goto', (('Final', 'name'),)),
        ('pass', ()),
        ('let', (('c', 'name'), ('A <= 1', 'str'))),
        ('goto', (('Final', 'name'),)),
        ('pass', ()),
        ('out', (('c', 'name'),)),
        ('out', ()),
        ('out', (('The program is end!', 'str'),))
    ]

    interpreter = PsInterpreter(
        func = {
            'stdin' : demo_input,
            'stdout' : demo_output,
            'stderr' : demo_error
        }
    )
    
    interpreter.digest(data_blocks, data_parsed)
    interpreter.run()

    raw_input('\nEND!')
