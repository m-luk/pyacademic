from ensurepip import version
from gettext import install
from importlib.metadata import entry_points
from unicodedata import name
from setuptools import setup

requirements = open("requirements.txt", "r").readlines()

setup(
    name="pyacademic",
    version="1.0",
    description="set of useful python scripts for academic and more...",
    author_email="mluk@mluk.pl",
    author="m-luk",
    packages=["pyacademic"],
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "mthread=pyacademic.mech.mthread:main",
            "toler=pyacademic.mech.toler:main"
        ],
    },
)
