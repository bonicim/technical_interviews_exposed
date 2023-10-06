import os.path
from setuptools import find_packages, setup

readme_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "README.md"))
with open(readme_path, "r", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="technical-interview-questions",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    version="0.1.0",
    # metadata to display on PyPI
    author="Mark Bonicillo",
    author_email="markabonicillo@gmail.com",
    description="Simple and clean solutions for typical technical interview questions.",
    long_description=readme,
    license="GPLv3",
    url="https://github.com/bonicim/technical_interviews_exposed",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Algorithms",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
