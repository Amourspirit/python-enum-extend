from enum_extend import AutoEnum

class ExAutoEnum(AutoEnum):
    '''
    This class inherits from :doc:`../class/AutoEnum` and is a just an example
    '''
    EX_ONE = 'This is a simple example of enum doc string'
    EX_TWO = '''
    Represents TWO.
    
    This is a multi-line doc string
    '''