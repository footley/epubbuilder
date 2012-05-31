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
    with open(file_name) as _file:
        for line in _file.readlines():
            line = line.strip()
            if re.match(r'(\s*#)|(\s*$)', line): # skip comments/empty lines
                continue
            else:
                requirements.append(line)
    
    return requirements

with open('README.md') as _file:
    long_desc = _file.read()

setup(name='epubbuilder',
      version='1.0',
      description='fork of http://code.google.com/p/python-epub-builder/ to programmatically build EPUB books.',
      long_description = long_desc,
      author='Jonathan Butcher',
      author_email='footley@gmail.com',
      url='https://github.com/footley/epubbuilder',
      install_requires=parse_requirements('requirements.txt'),
      packages=['epubbuilder'],
      package_data={'templates': [
                         'container.xml', 
                         'content.opf',
                         'image.html',
                         'title-page.html',
                         'toc.html',
                         'toc.ncx',
                         ],
                    'test-files': ['revenge.500x800.jpg'],
                    'epubcheck-3.0b5': [
                           'COPYING.txt',
                           'README.txt',
                           'epubcheck-3.0b5.jar',
                           'lib/batik-css-1.7.jar',
                           'lib/batik-license.txt',
                           'lib/batik-util-1.7.jar',
                           'lib/commons-compress-1.2.jar',
                           'lib/commons-compress-license.txt',
                           'lib/jing-20120227.jar',
                           'lib/jing-license.txt',
                           'lib/sac-1.3.jar',
                           'lib/sac-license.txt',
                           'lib/saxon-9.1.0.8.jar',
                           'lib/saxon-license.txt',
                           ],
                 },
      )

