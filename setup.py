import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='rxnlvl',  
     version='0.1',
     scripts=['rxnlvl'] ,
     author="Surat Teerapittayanon",
     author_email="steerapi@gmail.com",
     description="A simple python package for drawing attractive chemical reaction energy level diagrams.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/steerapi/rxnlvl",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: GPL-3.0",
         "Operating System :: OS Independent",
     ],
 )