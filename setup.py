import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="GC-Data",
    version="0.0.1-alpha",
    author="Jeremy Bouchard",
    author_email="mukki1996@gmail.com",
    description="Open source extractor of the Canadian Government meteorological data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Mukki/gc-data",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
