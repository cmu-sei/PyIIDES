from setuptools import setup, find_packages

VERSION = '0.1.1' 
DESCRIPTION = 'PyIIDES'
LONG_DESCRIPTION = 'Python API for the Insider Incident Data Exchange Standard'

# Setting up
setup(
    name='pyiides',
    version=VERSION,
    packages=find_packages(exclude=["tests", "tests.*", "docs", "docs.*", "venv", "build", "dist", "coverage"]),
    include_package_data=True,
    description='A Python implementation of the Insider Incident Data Exchange Standard (IIDES)',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Software Engineering Institute",
    author_email='abwhisnant@sei.cmu.edu',
    url='https://github.com/cmu-sei/pyiides',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
    license='LICENSE.txt',
)