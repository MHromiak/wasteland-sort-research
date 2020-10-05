import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wasteland_sort",
    version="0.0.1",
    author="Markian Hromiak",
    author_email="mhromiak3@gatech.edu",
    description="Draft version of the sort with testing and comparison",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MHromiak/wasteland_sort.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        # "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8.2',
)
