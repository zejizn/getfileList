import setuptools

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="getfileList",
    version="0.0.1",
    install_requires = requirements,
    entry_points={
        'console_scripts': [
            'getfileList=getfileList:main',
        ],
    },
    packages=setuptools.find_packages(),
    description="sample packages by legacy-setup.py"
)
