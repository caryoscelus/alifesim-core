from setuptools import setup, find_packages

from alifesim.version import __version__

setup(
    name='alifesim',
    version=__version__,
    description="core of a life sim",
    url='https://github.com/caryoscelus/',
    author='caryoscelus',
    author_email='caryoscelus@gmx.com',
    license='GPLv3+',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',

        'Topic :: Games/Entertainment',
    ],
    packages=find_packages(),
    install_requires=[
        #'rekeiton'
    ],
)
