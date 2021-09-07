[![codecov](https://codecov.io/gh/Amourspirit/python-enum-extend/branch/master/graph/badge.svg?token=FR0OBGG97C)](https://codecov.io/gh/Amourspirit/python-enum-extend) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/enum-extend) ![PyPI - Wheel](https://img.shields.io/pypi/wheel/enum-extend)

# Python enum-extended module

Enum Extend classes.

## Docs

Read the docs [here](https://python-enum-extend.readthedocs.io/)

## Install

### CONDA

enum-extend on [Anaconda](https://anaconda.org/conda-forge/enum-extend)

```bash
conda install -c conda-forge enum-extend
```

### PIP

enum-extend on [PyPI](https://pypi.org/project/enum-extend/):

```bash
pip install enum-extend
```

## EnumComparable

EnumComparable class is designed for comparsion of Integer based enums.

Allows child classes to be compared using the following comparsion operaters.

`==`, `!=`, `<`, `<=`, `>`, `>=`, `+`, `+=`, `-`, and `-=`.

## AutoEnum

AutoEnum class is a child class of EnumComparable.

Allows child classed to be auto numbered with Docstring.
