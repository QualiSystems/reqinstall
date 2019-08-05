from setuptools import setup, find_packages

setup(name='reqinstall',
      version='0.0.2',
      description='',
      author='Quali',
      license='MIT License',
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Console',
                   'Intended Audience :: End Users/Desktop',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'License :: OSI Approved :: MIT License'],
      packages=find_packages(exclude=['tests']),
      install_requires=[])
