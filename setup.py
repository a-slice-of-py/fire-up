from setuptools import setup

setup(
    name='FireUp',
    version='1.0',
    py_modules=['fire_up'],
    entry_points='''
        [console_scripts]
        fireup=fire_up:main
    ''',
)