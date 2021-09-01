**example:** simple doc string

.. code-block:: python

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