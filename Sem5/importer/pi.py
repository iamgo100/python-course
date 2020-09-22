import sys
import importer

# importer.url_hook('https://test.pypi.org/project/useful-pkg-iamgo100/')
# sys.path.append('https://test.pypi.org/project/useful-pkg-iamgo100/')

# from useful_pkg_iamgo100 import tools

# print(tools('work!'))

importer.url_hook('https://github.com/iamgo100/python-course/tree/master/Sem5/package/useful.py')
sys.path.append('https://github.com/iamgo100/python-course/tree/master/Sem5/package/useful.py')

from useful import boo

print(boo())