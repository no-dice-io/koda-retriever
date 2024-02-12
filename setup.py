from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='golden-retriever',  # Replace with your own project name
    version='0.1.0',  # Replace with your own version
    packages=find_packages(include=['golden_retriever', 'golden_retriever.src.*']),  # Replace with your own packages
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            # If you want to create any command-line scripts, add them here.
            # For example:
            # 'my-script=golden_retriever.main:main',
        ],
    },
    python_requires='>=3.10',  # Or whatever your project requires
)