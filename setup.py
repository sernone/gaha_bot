import os
from setuptools import setup

def read(fname):
    file = os.path.join(os.path.dirname(os.path.abspath(__file__)), fname)
    return open(file).read()

setup(
    name = "GAHA_Bot",
    description = ("Automation bot for twitch and discord for GAHA Chairty Event"),
    keywords = "automation twitch charity",
    version = "1.0.0",
    author = "Alex Zabielski",
    author_email = "sern18@gmail.com",
    license = read('LICENSE'),
    packages =[],
    long_description = read('README.md')
)