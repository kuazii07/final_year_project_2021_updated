from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requiremnets(file_path:str)->List[str]:
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements
    

setup(
    name="visual_malware_classification",
    version="0.0.1",
    author="Noel Kuasmapa",
    packages=find_packages(),

    author_email = "noeljackkuasmapa@gmail.com",
    install_requires = get_requiremnets("requirements.txt")
)    