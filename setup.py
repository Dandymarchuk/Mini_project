import setuptools
with open("README.md", "r", encoding = "UTF-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "FilmFinder_Dymarchuk_Danylo",
    version = "0.0.1",
    author = "Dymarchuk Danylo",
    author_email = "danylo.dymarchuk@ucu.edu.ua",
    description = "A package for find favourite films",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = " ",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires = '>=3.8'
) 