**example:** Two Parameters

.. code-block:: python

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