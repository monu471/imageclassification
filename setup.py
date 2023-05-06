import setuptools
### readme file ko description m convert krna hai if we upload our code in the pypi package 
with open("Readme.md","r",encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "imageclassification"
AUTHOR_NAME = "monu471"
SRC_REPO = "DogCat" ## hamare project folder ka name 
AUTHOR_EMAIL = "monujoshi471@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version= __version__ ,
    author= AUTHOR_NAME,
    description= "a package for cnn app",
    long_description= long_description,
    long_description_content = "text/markdown",
    url = f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_url = {
        "Bug Tracker":f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues" 
    },
    package_dir = {"": "src"}, 
    #src is the folder where all the code is written 
    packages = setuptools.find_packages(where = "src")
    )
