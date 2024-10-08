import setuptools

setuptools.setup(
    name="getfileList",
    version="0.0.1",
    install_requires = [],
    entry_points={
        'console_scripts': [
            'getfileList=getfileList:main',
        ],
    },
    packages=setuptools.find_packages(),
    description="sample packages by legacy-setup.py"
)
