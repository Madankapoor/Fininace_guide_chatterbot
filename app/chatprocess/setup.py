from distutils.core import setup
from Cython.Build import cythonize

setup(
  name="Engine",
  ext_modules = cythonize("Engine.pyx")
)