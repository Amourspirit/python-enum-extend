import pathlib
from setuptools import setup, find_packages

MODULE_ROOT_NAME='enum_extend'
PKG_NAME='enum-extend'
SRC_DIR='src'
MAJOR = 0
MINOR = 1
MICRO = 0
ISRELEASED = True
VERSION = "{0}.{1}.{2}".format(MAJOR,MINOR,MICRO)


# The directory containing this file
HERE = pathlib.Path(__file__).parent
# The text of the README file
with open(HERE / "README.md") as fh:
    README = fh.read()


# This call to setup() does all the work
setup(
    name=PKG_NAME,
    version=VERSION,
    python_requires='>=3.4.0',
    description="Enum base classes that support enum comparsion and auto numbering with doc strings",
    long_description_content_type="text/markdown",
    long_description=README,
    url="https://github.com/Amourspirit/python-enum-extend",
    author=":Barry-Thomas-Paul: Moss",
    author_email='bigbytetech@gmail.com',
    license="MIT",
    # packages=[MODULE_ROOT_NAME],
    packages=find_packages(where='src', exclude=('tests',)),
    package_dir={'': 'src'},
    # py_modules=MODULES,
    keywords=['python', 'enum', 'autoenum', 'compare-enum', 'enum-compare', 'enum-docstring'],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    include_package_data=True,
)
