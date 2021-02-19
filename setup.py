import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="BAClangUtils",
    version="1.0.8",
    author="BenArvin",
    author_email="benarvin93@outlook.com",
    description="Clang utils for parse Objective-C code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BenArvin/BAClangUtils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
