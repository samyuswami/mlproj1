from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e .'



def get_requirements(file_path:str)->List[str]:
    '''
    this function returns the list of requirements that we have in requirements.txt
    We need this for our model package
    '''
    requirements=[]
    with open(file_path)as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name='mlproj1',
    version='0.0.1',
    author='Samyuktha',
    author_email='samyuswami28@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)