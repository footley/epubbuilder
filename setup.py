import re
from distutils.core import setup

def parse_requirements(file_name):
    """
    Simple requirements parsing, only works for reqs of form:
    genshi==0.6
    genshi
    etc.
    """
    requirements = []
    for line in open(file_name, 'r').read().split('\n'):
        if re.match(r'(\s*#)|(\s*$)', line): # skip comments/empty lines
            continue
        else:
            requirements.append(line)
    
    return requirements

setup(name='epubbuilder',
      version='1.0',
      description='fork of http://code.google.com/p/python-epub-builder/ to programmatically build EPUB books.',
      author='Jonathan Butcher',
      author_email='footley@gmail.com',
      url='https://github.com/footley/epubbuilder',
      py_modules=['epubbuilder'],
      install_requires=parse_requirements('requirements.txt'),
      data_files=[('templates', ['*',
                                 ]),
                  ('test-files', ['revenge.500x800.jpg']),
                  ('epubcheck-3.0b5', ['*',
                                       'lib/*',
                                       ]),
      )

