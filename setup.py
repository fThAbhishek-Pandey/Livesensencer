from setuptools import find_packages, setup
# from typing import list
from typing import List
def get_requirements()->list[str]:
    requirement_list= list[str]={}
    return requirement_list
setup (
    name='sensor',
    version='0.0.1',
    author='Abhishek Pandey',
    author_email='abhishek830564@gmail.com',
    packages= find_packages(),
    install_requires= get_requirements() # ["pymongo"]
)