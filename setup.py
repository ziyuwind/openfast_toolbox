""""Distribution setup"""


import os

from setuptools import setup

ROOT = os.path.abspath(os.path.dirname(__file__))

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

with open(os.path.join(ROOT, "VERSION")) as version_file:
    VERSION = version_file.read().strip()


setup(
    name="pyFAST",
    description="pyFAST",
    long_description=LONG_DESCRIPTION,
    version=VERSION,
    url="https://github.com/openfast/pyFAST/",
    classifiers=[
        "Topic :: Utilities",
        "Topic :: Software Development :: Testing",
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Version Control :: Git",
    ],
    packages=["pyFAST"],
    python_requires=">=3.6",
    install_requires=[
        "matplotlib",
        "openpyxl",
        "numpy>=1.15.2",
        "pandas",
        "pyarrow", # for parquet files
        "scipy",
        "chardet",
        "xarray",  # for netcdf files
        "pytest",
    ],
    test_suite="pytest",
    tests_require=["pytest"],
    entry_points={"console_scripts": ["pyFAST = pyFAST.__main__:main"]},
)
