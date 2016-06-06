# define exceptions used internally in the parser & interpreter

class PsParserInterrupt(Exception):
    ''' exception for the parser interruption '''
    def __init__(self, *args, **kwargs):
        super(PsParserInterrupt, self).__init__(*args, **kwargs)

class PsInterpreterInterrupt(Exception):
    ''' exception for the interpreter interruption '''
    def __init__(self, *args, **kwargs):
        super(PsInterpreterInterrupt, self).__init__(*args, **kwargs)
