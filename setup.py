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
      data_files=[('templates', ['container.xml', 
                                 'content.opf',
                                 'image.html',
                                 'title-page.html',
                                 'toc.html',
                                 'toc.ncx',
                                 ]),
                  ('test-files', ['revenge.500x800.jpg']),
                  ('epubcheck-3.0b5', ['COPYING.txt',
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
                                       ]),
                 ],
      )

