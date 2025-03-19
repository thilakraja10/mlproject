from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT='-e.'
def get_requirements(file_path: str) -> List[str]:
    '''
    Read requirements from a text file and return a list of requirements.
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
       
        if HYPEN_E_DOT in requirements:
           requirements.remove(HYPEN_E_DOT)

    return requirements
setup(
    name='mlproject',  # Replace with your project name
    version='0.1.0',
    author='thilak',
    author_email='thilakraja10@gmail.com',
    description='A machine learning project',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/thilakraja10/mlproject.git',  # Replace with your repo link
    packages=find_packages(),
    install_requires =get_requirements('requirements.txt'),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
