Example Help
============

.. code-block:: python
    :caption: help(ExAutoEnum)

    >>> help(ExAutoEnum)

    Help on class ExAutoEnum in module ex:

    class ExAutoEnum(enum_extend.AutoEnum)
     |  ExAutoEnum(value, names=None, *, module=None, qualname=None, type=None, start=1)
     |  
     |  This class inherits from :doc:`../class/AutoEnum` and is a just an example
     |  
     |  Method resolution order:
     |      ExAutoEnum
     |      enum_extend.AutoEnum
     |      enum_extend.EnumComparable
     |      enum.Enum
     |      builtins.object
     |  
     |  Data and other attributes defined here:
     |  
     |  EX_FIVE = <ExAutoEnum.EX_FIVE: 5>
     |  
     |  EX_FOUR = <ExAutoEnum.EX_FOUR: 4>
     |      .. tip::
     |      This equals 4
     |  
     |  
     |  EX_ONE = <ExAutoEnum.EX_ONE: 1>
     |      This is a simple example of enum doc string
     |  
     |  
     |  EX_TEN = <ExAutoEnum.EX_TEN: 10>
     |      This value was set 10
     |  
     |  
     |  EX_THREE = <ExAutoEnum.EX_THREE: 3>
     |      .. include:: ../inc/ex/inc_ex.rst
     |  
     |  
     |  EX_TWO = <ExAutoEnum.EX_TWO: 2>
     |      Represents **TWO**.
     |      
     |      This is a multi-line `docstring <https://www.python.org/dev/peps/pep-0257/>`_
     |      
     |      Are there any questions?

.. code-block:: python
    :caption: help(ExAutoEnum.EX_ONE)

    >>> help(ExAutoEnum.EX_ONE)

    Help on ExAutoEnum in module ex:

    <ExAutoEnum.EX_ONE: 1>
        This is a simple example of enum doc string