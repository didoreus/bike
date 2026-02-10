from setuptools import setup, find_packages

setup(
    name='citibikepj'
    , version='0.0.6'
    , description='A package for the Citi Bike Project'
    , author='Dieuseul D.'
    , packages=find_packages(where='./src')
    , package_dir={'': './src'}
    , install_requires=['setuptools']
    , python_requires='>=3.8'
    )