import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='rxnlvl',  
     version='0.3.7',
     scripts=['rxnlvl/__init__.py'] ,
     author="Surat Teerapittayanon",
     author_email="steerapi@gmail.com",
     description="A simple python package for drawing attractive chemical reaction energy level diagrams.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/steerapi/rxnlvl",
     packages=setuptools.find_packages(),
     license="GPL",
     classifiers=[
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
     ],
 )