**example:**

.. code-block:: python

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