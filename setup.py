from setuptools import setup, find_packages

setup(
    name='pelias-wrapper',
    version='0.1.0',
    packages=find_packages(),  # Automatically find all the packages
    install_requires=[          # List of dependencies
        'requests',  # Add other dependencies if needed
    ],
    include_package_data=True,  # Includes non-Python files as specified in MANIFEST.in
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='maniteja bhumaraju',
    author_email='manitejabhumarajuspam@gmail.com',
    description='A Python wrapper for Pelias geocoding API',
    url='https://github.com/Manitejasga/pelias-wrapper',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Minimum Python version
)
