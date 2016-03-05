# define a Pysic shell

import sys

_ps_platform = sys.platform
_ps_version = '1.0'

class PsShell(object):
    ''' simple interactive shell with I/O support '''
    def __init__(self, platform = _ps_platform, version = _ps_version):
        ''' class initialization '''
        self.platform = platform
        self.version = version

        self.count = {
            'stdin' : 0,
            'stdout' : 0,
            'stderr' : 0
        }

        self.head = {
            'stdin' : 'In',
            'stdout' : 'Out',
            'stderr' : 'Error'
        }

    def input(self):
        ''' read a string from stdin '''
        data_input = raw_input(
            '%s [%d] - '% (self.head['stdin'], self.count['stdin'])
        ).strip()

        self.count['stdin'] += 1

        return data_input

    def output(self, *data):
        ''' print a list of objects on stdout '''
        data_output = '%s [%d] - %s' % (
            self.head['stdout'],
            self.count['stdout'],
            ''.join(map(str, data))
        )

        self.count['stdout'] += 1

        print data_output

    def error(self, message):
        ''' print a message on stderr '''
        data_error = '%s - %s' % (self.head['stderr'], message)
        self.count['stderr'] += 1

        print data_error

    def start(self):
        ''' settings before initiating '''
        self.count['stdin'] = 0
        self.count['stdout'] = 0
        self.count['stderr'] = 0

        print 'Pysic %s (platform : %s)\n' % (self.version, self.platform)

    def end(self):
        ''' end the shell '''
        raw_input('\nProgram end. Press any key to exit!')

if __name__ == '__main__':
    ps = PsShell()

    ps.start()
    a = ps.input()
    b = ps.input()

    ps.output('a = ', a, ', b = ', b)
    ps.output()
    
    ps.error('Something is wrong!')
    
    ps.end()
