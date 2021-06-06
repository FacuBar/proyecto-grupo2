from distutils.core import setup
import os


scripts = []
if os.name == 'posix':
    scripts = ['bin/docmgr']
elif os.name == 'nt':
    scripts = ['bin/docmgr.bat']
else:
    scripts = ['bin/docmgr']

setup(
    name = 'docmgr',
    version = '0.0.0',
    author = 'Facundo Escobar, Iñaki Rodriguez',
    packages = ['docmgr'],
    scripts = scripts,
)
