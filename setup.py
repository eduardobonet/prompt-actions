from setuptools import setup, find_packages

setup(
    name='prompter',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'prompter=prompter.cli:cli'
        ]
    },
    install_requires=[
        'click',
        'jinja2',
        'requests'
    ]
)
