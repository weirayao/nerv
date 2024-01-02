import io
import os
from typing import List, Set

import setuptools

ROOT_DIR = os.path.dirname(__file__)

def get_path(*filepath) -> str:
    return os.path.join(ROOT_DIR, *filepath)

def read_readme() -> str:
    """Read the README file if present."""
    p = get_path("README.md")
    if os.path.isfile(p):
        return io.open(get_path("README.md"), "r", encoding="utf-8").read()
    else:
        return ""


def get_requirements() -> List[str]:
    """Get Python package dependencies from requirements.txt."""
    with open(get_path("requirements.txt")) as f:
        requirements = f.read().strip().split("\n")
    return requirements


setuptools.setup(
    name="xos",
    version="0.0.1",
    author="Weiran Yao",
    license="Apache 2.0",
    description=("XGen OS: An interface model for "
                 "multimodal agents"),
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/weiayao/nerv",
    project_urls={
        "Homepage": "https://github.com/weirayao/nerv",
        "Documentation": "TBD",
    },
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    packages=setuptools.find_packages(exclude=("docs", "tests")),
    python_requires=">=3.10",
    install_requires=get_requirements(),
    package_data={"nerv": ["py.typed"]},
)