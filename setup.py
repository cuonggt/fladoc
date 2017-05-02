from setuptools import setup

setup(
    name='Fladoc',
    version='1.0',
    long_description=__doc__,
    py_modules=['fladoc'],
    include_package_data=True,
    install_requires=[
        'Flask>=0.12',
        'Lxml>=3.7',
        'Mistune>=0.7'
        'Click>=6.7',
        'Algoliasearch>=1.12',
    ],
    entry_points='''
        [console_scripts]
        indexer=indexer:cli
    ''',
)