from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

PROJECT_NAME = 'DL_StudentPerformance_AWS_CI-CD'
VERSION = '0.0.1'
AUTHOR = 'aiAMAL'
REQUIREMENTS_FILE = 'requirements.txt'


def get_requirements(file_path: str) -> List[str]:
    """
    Reads the requirements file and returns a list of dependencies.

    Args:
        file_path (str): Path to the requirements file.

    Returns:
        List[str]: List of dependencies.
    """
    with open(file_path, 'r') as file:
        # strips any whitespace (including newlines), & removes empty lines
        requirements = [line.strip() for line in file if line.strip()]

    if HYPHEN_E_DOT in requirements:
        # remove the '-e .' requirement if it exists in the list
        requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    packages=find_packages(),
    install_requires=get_requirements(REQUIREMENTS_FILE),
)