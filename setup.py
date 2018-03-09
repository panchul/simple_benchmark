import sys

from setuptools import setup, find_packages


def readme():
    with open('README.rst') as f:
        return f.read()


def version():
    with open('simple_benchmark/__init__.py') as f:
        for line in f:
            if line.startswith('__version__'):
                return line.split(r"'")[1]


setup(name='simple_benchmark',
      version=version(),

      description='A simple benchmarking package.',
      long_description=readme(),
      # Somehow the keywords get lost if I use a list of strings so this is
      # just a longish string...
      keywords='performance timing timeit',
      platforms=["Windows Linux Mac OS-X"],

      classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Utilities',
        'Topic :: System :: Benchmark'
      ],

      license='Apache License Version 2.0',

      url='https://github.com/MSeifert04/simple_benchmark',

      author='Michael Seifert',
      author_email='michaelseifert04@yahoo.de',

      packages=find_packages(exclude=['ez_setup']),

      include_package_data=True,
      zip_safe=False,
)