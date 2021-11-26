from setuptools import setup
from Cython.Build import cythonize

setup(
    name='CythonApp',
    ext_modules=cythonize("main_Cython.py"),
    zip_safe=False,
)