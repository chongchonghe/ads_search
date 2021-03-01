from setuptools import setup, find_packages

setup(
    name='adssearch',
    version='0.1.0',
    url='https://github.com/chongchonghe/ads_search.git',
    author='Chong-Chong He',
    author_email='che1234@umd.edu',
    description='A simple ADS search tool that works',
    packages=find_packages(),
    entry_points={'console_scripts': ['ads=adssearch:main']},
    install_requires=['ads', 'argparse'],
)
