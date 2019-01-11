import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='gc-data',
    version='0.0.1a8',
    author='Jeremy Bouchard',
    author_email='mukki1996@gmail.com',
    description='Open source extractor of the Canadian Government meteorological data.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Mukki/gc-data',
    package_dir={
        'gc_data': 'src',
    },
    packages=[
        'gc_data',
    ],
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
