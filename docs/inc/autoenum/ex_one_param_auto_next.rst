**example:** One Param to set only auto-number next sequence

.. code-block:: python

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