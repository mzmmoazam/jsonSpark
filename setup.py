import setuptools
import os
try:  # for pip >= 10
    from pip._internal.req import parse_requirements
    from pip._internal.network.session import PipSession
except ImportError:  # for pip <= 9.0.3
    from pip.req import parse_requirements
    from pip.download import PipSession

with open("README.md", "r") as fh:
    long_description = fh.read()
requirements = parse_requirements(os.path.join(os.path.dirname(__file__), 'requirements.txt'), session=PipSession())

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
    install_requires=[str(requirement.requirement) for requirement in requirements]
)
