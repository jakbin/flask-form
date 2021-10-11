from setuptools import setup, find_packages
from deb import __version__

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setup(
    name="flask-form",
    version=__version__,
    author="Jak Bin",
    author_email="jakbin4747@gmail.com",
    description="A flexible forms validation and rendering library for python",
    long_description=readme,
    long_description_content_type="text/markdown",
    license="MIT License",
    url="https://github.com/jakbin/flask-form",
    python_requires=">=3.6",
    install_requires=[""],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
    ],
    keywords='FLask,flask-form,form',
    packages=find_packages(),
    zip_safe=False,
)
