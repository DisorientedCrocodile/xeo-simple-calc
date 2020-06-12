import setuptools

with open("README.txt", "r") as fh:
    long_description = fh.read()
with open("CHANGELOG.txt", "r") as CHANGELOG:
    changes = CHANGELOG.read()

setuptools.setup(
    name="xeo_simple_calc",
    version="0.0.2",
    author="Grigoriy Agasiyants",
    author_email="xeoplay123456@gmail.com",
    description="A small basic calculator",
    long_description=long_description + "\n\n" + changes,
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)