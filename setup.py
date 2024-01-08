from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = "A calculator package used for summation, subtraction, multiplication, division and taking a root out of a stored value"

# Setting up
setup(
    name="Calculator_karutka_2023",
    version=VERSION,
    author="Kasparas Rutkauskas",
    author_email="kasparas.r7@gmail.com",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['mpi4py>=2.0', 'numpy>=2.0'],
    classifiers=[
        'Intended Audience :: Learning',
        'License :: OSI Approved :: MIT License',  
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)