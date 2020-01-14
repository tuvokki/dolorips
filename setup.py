import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dolorips",
    version="0.0.10",
    author="Wouter Roosendaal",
    author_email="wouter@wouterroosendaal.nl",
    description="A small package that generates paragraphs from long texts using the markov generator algorithm.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TuvokVersatileKolinahr/dolorips",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
