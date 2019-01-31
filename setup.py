from setuptools import setup, find_packages


setup(
    name='geoquery',
    version='1.0.0',
    install_requires=[
        'unicodecsv'
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'geoquery = geoquery.bin:run'
        ]
    }
)
