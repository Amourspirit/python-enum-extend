# coding: utf-8
from enum import Enum
import numbers
import re

# region class EnumComparable


class EnumComparable(Enum):
    '''
    Base class for creation enums that can be compared.
    Can be used with operators `==`, `!=`, `<`, `<=`, `>`, `>=`, `+`, `+=`, `-`, and `-=`.

    Values on the right side of the operator can be other Enum, number, str.

    @example:
    ```
    class MyEnum(EnumComparable):
        NONE = 0
        FIRST = 1
        SECOND = 2
        THIRD = 3
        FOURTH = 4

    print(MyEnum.NONE < MyEnum.First) # True
    print(MyEnum.SECOND <= MyEnum.SECOND) # True
    print(MyEnum.THIRD > MyEnum.THIRD) # False
    print(MyEnum.NONE > MyEnum.THIRD) # False
    print(MyEnum.NONE == MyEnum.THIRD) # False
    print(MyEnum.NONE != MyEnum.THIRD) # True

    my_enum = MyEnum.FIRST + MyEnum.THIRD
    print(my_enum.value) # 4

    my_enum = MyEnum.FIRST + MyEnum.FIRST + MyEnum.SECOND
    print(my_enum.value) # 4

    my_enum = MyEnum.FIRST + 3
    print(my_enum.value) # 4

    my_enum = MyEnum.FIRST + "THIRD"
    print(my_enum.value) # 4

    my_enum = MyEnum.FIRST + "< MyEnum.SECOND >  " + 1
    print(my_enum.value) # 4

    my_enum = MyEnum.SECOND - MyEnum.FIRST
    print(my_enum.value) # 1
    ```
    '''
    # Original: https://stackoverflow.com/questions/39268052/how-to-compare-enums-in-python

    def __str_to_enum_comparable(self, enum_str: str) -> 'EnumComparable':
        str_lst = enum_str.split('.')
        for str_chars in str_lst:
            # try_str will contain all alpha numeric chars containd in str_chars
            # all other chars are ignored includeing whitespace
            try_str = "".join(re.findall("[a-zA-Z0-9]+", str_chars))
            if hasattr(self.__class__, try_str):
                return getattr(self.__class__, try_str)
        msg = "String '{0}' can not be converted into '{1}'".format(
            enum_str, self.__class__.__name__)
        raise ValueError(msg)

    def __gt__(self, other: 'EnumComparable'):
        try:
            return self.value > other.value
        except:
            pass
        if isinstance(other, numbers.Real):
            return self.value > other
        try:
            if isinstance(other, str):
                obj = self.__str_to_enum_comparable(other)
                return self.value > obj.value
        except ValueError as ex:
            raise ex
        return NotImplemented

    def __lt__(self, other: 'EnumComparable'):
        try:
            return self.value < other.value
        except:
            pass
        if isinstance(other, numbers.Real):
            return self.value < other
        try:
            if isinstance(other, str):
                obj = self.__str_to_enum_comparable(other)
                return self.value < obj.value
        except ValueError as ex:
            raise ex
        return NotImplemented

    def __ge__(self, other: 'EnumComparable'):
        try:
            return self.value >= other.value
        except:
            pass
        if isinstance(other, numbers.Real):
            return self.value >= other
        try:
            if isinstance(other, str):
                if self.name == other:
                    return True
                obj = self.__str_to_enum_comparable(other)
                return self.value >= obj.value
        except ValueError as ex:
            raise ex
        return NotImplemented

    def __le__(self, other: 'EnumComparable'):
        try:
            return self.value <= other.value
        except:
            pass
        if isinstance(other, numbers.Real):
            return self.value <= other
        try:
            if isinstance(other, str):
                if self.name == other:
                    return True
                obj = self.__str_to_enum_comparable(other)
                return self.value <= obj.value
        except ValueError as ex:
            raise ex
        return NotImplemented

    def __eq__(self, other: 'EnumComparable'):
        # if self.__class__ is other.__class__:
        #     return self == other # causes infinate loop
        try:
            return self.value == other.value
        except:
            pass
        if isinstance(other, numbers.Real):
            return self.value == other
        try:
            if isinstance(other, str):
                obj = self.__str_to_enum_comparable(other)
                return self.value == obj.value
        except ValueError:
            return False
        return NotImplemented

    def __add__(self, other: 'EnumComparable'):
        if isinstance(other, EnumComparable):
            try:
                new_val = self.value + other.value
                obj = self.__class__(new_val)
                return obj
            except ValueError as ex:
                msg = "'{0}.{1}' with a value of '{2}' can not be added to '{3}'".format(
                    other.__class__.__name__,
                    other.name,
                    other.value,
                    self.__class__.__name__)
                msg = msg + "\nAttempt to add is out of range for '{0}'".format(
                    self.__class__.__name__)
                raise ValueError(msg) from ex
        
        if isinstance(other, numbers.Real):
            try:
                new_val = self.value + other
                obj = self.__class__(new_val)
                return obj
            except ValueError as ex:
                msg = "Number '{0}' can not be converted into '{1}'".format(
                    new_val, self.__class__.__name__)
                raise ValueError(msg) from ex
        if isinstance(other, str):
            try:
                other_enum = self.__str_to_enum_comparable(other)
                new_val = self.value + other_enum.value
                obj = self.__class__(new_val)
                return obj
            except ValueError as ex:
                ex_msg = str(ex)
                if ex_msg.endswith("'{0}'".format(self.__class__.__name__)):
                    raise ex
                else:
                    msg = "Adding '{0}' to current instance can not be converted into '{1}'".format(
                        other, self.__class__.__name__)
                    raise ValueError(msg)
        try:
            new_val = self.value + other.value
            obj = self.__class__(new_val)
            return obj
        except:
            pass
        return NotImplemented

    def __sub__(self, other: 'EnumComparable'):
        if isinstance(other, EnumComparable):
            try:
                
                new_val = self.value - other.value
                obj = self.__class__(new_val)
                return obj
            except ValueError as ex:
                msg = "'{0}.{1}' with a value of '{2}' can not be subtracted from '{3}'".format(
                    other.__class__.__name__,
                    other.name,
                    other.value,
                    self.__class__.__name__)
                msg = msg + "\nAttempt to subtract is out of range for '{0}'".format(
                    self.__class__.__name__)
                raise ValueError(msg) from ex
        if isinstance(other, numbers.Real):
            try:
                new_val = self.value - other
                obj = self.__class__(new_val)
                return obj
            except ValueError as ex:
                msg = "Number '{0}' can not be converted into '{1}'".format(
                    new_val, self.__class__.__name__)
                raise ValueError(msg) from ex
        if isinstance(other, str):
            try:
                other_enum = self.__str_to_enum_comparable(other)
                new_val = self.value - other_enum.value
                obj = self.__class__(new_val)
                return obj
            except ValueError as ex:
                ex_msg = str(ex)
                if ex_msg.endswith("'{0}'".format(self.__class__.__name__)):
                    raise ex
                else:
                    msg = "Subtracting '{0}' from current instance can not be converted into '{1}'".format(
                        other, self.__class__.__name__)
                    raise ValueError(msg)
        return NotImplemented

    def __hash__(self):
        return id(self)

# endregion class EnumComparable

# region internal Methods


def _trim_docstr(docstring: str):
    # https://www.python.org/dev/peps/pep-0257/
    if not docstring:
        return ''
    # Convert tabs to spaces (following the normal Python rules)
    # and split into a list of lines:
    lines = docstring.expandtabs().splitlines()
    # Determine minimum indentation (first line doesn't count):
    max_int = 10000
    indent = max_int
    for line in lines[1:]:
        stripped = line.lstrip()
        if stripped:
            indent = min(indent, len(line) - len(stripped))
    # Remove indentation (first line is special):
    trimmed = [lines[0].strip()]
    if indent < max_int:
        for line in lines[1:]:
            trimmed.append(line[indent:].rstrip())
    # Strip off trailing and leading blank lines:
    while trimmed and not trimmed[-1]:
        trimmed.pop()
    while trimmed and not trimmed[0]:
        trimmed.pop(0)
    # Return a single string:
    return '\n'.join(trimmed)

# endregion internal Methods

# region class AutoEnum


class AutoEnum(EnumComparable):
    """
    Automatically numbers enum members starting from 1.

    `AutoEnum` inherits from `EnumComparable` and thus support all `EnumComparable` operations.

    Can be used with operators `==`, `!=`, `<`, `<=`, `>`, `>=`, `+`, `+=`, `-`, and `-=`.

    Values on the right side of the operator can be other Enum, number, str.

    Includes support for a custom docstring per member.

    Enum Members can be added with one or two parameters.
        When only one parameter is passed it is expcected to be a string.
        This single parameter will be used as doc string

        When two parameters are pass the first parameter is expected to be an `int`.
        The second parameter is expected to be `str`.

        First parameter is the value of the enum member and must not be less or equal the
        highest member value used thus far.

        Second parameter is the doc string.

    @example: simple auto-number, w/o docstring
    ```
    class MyAutoEnum(AutoEnum):
        FIRST = ()
        SECOND = ()
        THIRD = ()
        FOURTH = ()

    print(MyAutoEnum.FIRST.value) # 1
    print(MyAutoEnum.SECOND.value) # 2
    print(MyAutoEnum.THIRD.value) # 3
    print(MyAutoEnum.FOURTH.value) # 4
    ```

    @example: simple doc string

    ```
    import inspect

    class MyAutoEnum(AutoEnum):
        FIRST = 'First value'
        SECOND = 'Second value'
        THIRD = 'Third value'
        FOURTH = 'Fourth value'

    print(MyAutoEnum.FIRST.value) # 1
    print(MyAutoEnum.THIRD.value) # 3
    print(inspect.getdoc(MyAutoEnum.FIRST)) # First value
    print(MyAutoEnum.THIRD.__doc__) # Third value
    ```

    @example: One Parm to set only auto-number next sequence
    ```
    class OnlyAutoEnum(AutoEnum):
        NEG = -999
        LESS_NEG = ()
        NONE = 0
        FIRST = ()
        SECOND = ()
        TEN = 10
        TEN_PLUS = ()
        TWENTY = 20
        TWENTY_PLUS = ()

    print(OnlyAutoEnum.NEG.value) # -999
    print(OnlyAutoEnum.LESS_NEG.value) # -998
    print(OnlyAutoEnum.NONE.value) # 0
    print(OnlyAutoEnum.SECOND.value) # 2
    print(OnlyAutoEnum.TWENTY.value) # 20
    print(OnlyAutoEnum.TEN_PLUS.value) # 11
    print(OnlyAutoEnum.TEN_PLUS > OnlyAutoEnum.TEN) # True
    ```

    @example: Two Parameters
    ```
    class OthAutoEnum(AutoEnum):
        NONE = (0, 'Represents that no value is set yet')
        FIRST = 'First value'
        SECOND = 'Second value'
        TEN = (10, 'Represents 10')
        TEN_PLUS = 'Represents above 10'
        TWENTY = (20, 'Represents 20')
        TWENTY_PLUS = 'Represents above 20'

    print(OthAutoEnum.NONE.value) # 0
    print(OthAutoEnum.SECOND.value) # 2
    print(OthAutoEnum.TWENTY.value) # 20
    print(OthAutoEnum.TEN_PLUS.value) # 11
    print(OthAutoEnum.TEN_PLUS > OthAutoEnum.TEN) # True
    print(OthAutoEnum.TWENTY.__doc__) # Represents 20
    ```
    """
    # Original: https://stackoverflow.com/questions/19330460/how-do-i-put-docstrings-on-enums

    def __new__(cls, *args):
        """Ignores arguments (will be handled in __init__."""
        # add a class level dictionary to handle special class level value in init
        # this can alos be takend advantage of and extended in classes that extend AutoEnum
        if hasattr(cls, '_cls_dict_') is False:
            setattr(cls, '_cls_dict_', dict())
        value = len(cls) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        return obj
    #

    def __init__(self, *args):
        """Can handle 0, 1 or 2 argument; more requires a custom __init__.

        `0`  = auto-number w/o docstring

        `1`  = auto-number if arg is str then w/ docstring. if arg is int set the next auto-number value

        `2`  = First arg next number in auto-number sequence. Second arg docstring

        `3+` = needs custom __init__

        """
        d_cls = self.__class__._cls_dict_
        l_key = '_last_value_'
        last_value = d_cls.get(l_key, None)
        args_len = len(args)
        skip_doc_str = False
        if args_len >= 1 and isinstance(args[0], int):
            if args_len == 1:
                skip_doc_str = True
            value = args[0]
            if last_value is not None and value <= last_value:
                msg = "{0}, value of '{1}' must be greater then all previous values.".format(
                    self.__class__.__name__, value)
                msg = msg + "Try a value greater than '{0}'".format(last_value)
                raise ValueError(msg)
        else:
            # value = len(cls) + 1
            if last_value is None:
                value = 1
            else:
                value = last_value + 1
        d_cls[l_key] = value
        self._value_ = value
        if skip_doc_str is True:
            return None
        if args_len == 1 and isinstance(args[0], str):
            self.__doc__ = _trim_docstr(args[0])
        elif args_len == 2 and isinstance(args[1], str):
            self.__doc__ = _trim_docstr(args[1])
        elif args:
            raise TypeError(
                '%s not dealt with -- need custom __init__' % (args,))

# endregion class AutoEnum
