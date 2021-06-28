from setuptools import setup
import os

from docmgr import VERSION

scripts = []
if os.name == 'posix':
    scripts = ['bin/docmgr']
elif os.name == 'nt':
    scripts = ['bin/docmgr.bat']
else:
    scripts = ['bin/docmgr']

setup(
    name='docmgr',
    version=VERSION,
    author='Facundo Escobar, Iñaki Rodriguez',
    packages=['docmgr'],
    scripts=scripts,
)
