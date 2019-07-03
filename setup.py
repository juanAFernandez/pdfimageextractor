from setuptools import setup
from pip.req import parse_requirements

setup(name='pdfimageextractor',
      version='1.0',
      description='pdfimageextractor',
      url='https://github.com/juanAFernandez/pdfimageextractor',
      author='Juan A. Fernández',
      author_email='juanfernandezugr@gmail.com',
      license='GNU GPLv3',
      packages=['pdfimageextractor'],
      zip_safe=False,
      entry_points={
            'console_scripts': [
                  'pdfimageextractor = pdfimageextractor.main:main'
            ]
      },
      install_reqs = parse_requirements('requirements.txt', session='hack')
)
