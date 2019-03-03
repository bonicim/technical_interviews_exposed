import os.path
from setuptools import setup

readme_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'README.md'))
with open(readme_path, encoding='utf-8') as f:
    readme = f.read()

setup(
    name = "Technical Interviews Exposed",
    version = "0.1.0",
    author = "Mark Bonicillo",
    author_email = "markabonicillo@gmail.com",
    description = ("Simple and clean solutions for typical technical interview questions."),
    license = "GPLv3",
    keywords = "algorithms technical",
    url = "https://github.com/bonicim/technical_interviews_exposed",
    long_description=readme,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Algorithms",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)