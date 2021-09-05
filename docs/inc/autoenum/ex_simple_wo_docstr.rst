**example:** simple auto-number, w/o docstring
    
.. code-block:: python

    class MyAutoEnum(AutoEnum):
        FIRST = ()
        SECOND = ()
        THIRD = ()
        FOURTH = ()

    print(MyAutoEnum.FIRST.value) # 1
    print(MyAutoEnum.SECOND.value) # 2
    print(MyAutoEnum.THIRD.value) # 3
    print(MyAutoEnum.FOURTH.value) # 4