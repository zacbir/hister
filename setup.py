import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hister",
    version="0.0.1",
    author="Zachery Bir",
    author_email="zbir@zacbir.net",
    description="A command line tool for working with browser history",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zacbir/hister",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires=[],
    entry_points='''
        [console_scripts]
        hister=hister:cli
    ''',
)

