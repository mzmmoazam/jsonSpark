import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jsonSpark",
    version="0.0.1",
    author="mzm",
    author_email="mzm.moazam@gmail.com",
    description="This is a wrapper package for pyspark to process json files. It pythonifies the json pyspark object.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mzmmoazam/jsonSpark",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)