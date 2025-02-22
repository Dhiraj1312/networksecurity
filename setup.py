from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """
    Thiss function will return list of requiremnets

    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            # Read llines from the file
            lines = file.readlines()
            ## process each lne
            for line in lines:
                requirement=line.strip()
                # ignore empty lines and -e .
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirement.txt file not found ")

    return requirement_lst

setup(
    name="Network Security",
    version="0.0.1",
    author="Dhiraj Bhagat",
    author_email="dhirajbhagat1205@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements() 
)