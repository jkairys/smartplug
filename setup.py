from setuptools import setup, find_packages

setup(
    name='smartplug',
    version='0.1.0',
    py_modules=['smartplug'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'smartplug = smartplug.cli.commands:cli',
        ],
    },
)