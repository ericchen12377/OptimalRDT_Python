import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="OptimalRDTinPython",
    version="0.1.0",
    author="Suiyao Chen",
    author_email="suiyaochen@mail.usf.edu",
    description="A comprehensive package for Optimal Reliability Demonstration Test Design in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
