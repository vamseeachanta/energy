## Introduction
The document describes the python principles to be the followed for the python repositories:

## Summary

The key python 

- TBA

## Conda Environments

### General working

### IDE: VS Code 

For general working in VS code:
[https://code.visualstudio.com/docs/languages/python](https://code.visualstudio.com/docs/languages/python)

The typical extensions required are:
- Python (from Microsoft)
- Python Extension Pack

Setting up the project specific environment


### CI/CD Deployments

- If altering environment, consider the following:
  - delete environment and recreate fresh. 
    - This will help avoid run time performance issues. 
	- Possibly remnant files/folders confuse the python process
	- Also, if a fast route compilation (numba) is used. Without warning the numba can be disabled.
  - This will require disabling the tasks or kill ongoing tasks in a server machine



## Packaging

The good practices are as follows:
- Write tests. Preferably utilize pytest. 
- Example test and file structure
	- https://github.com/jumptrading/luddite
	- Utilized test_package.py for all tests 
	- pytest.ini file for pytest configurations
	- Utilize github test workflows
	- https://github.com/jumptrading/luddite/blob/master/.github/workflows/tests.yml
- Others considerations
	- Pypi supports Readme.rst (restructured Text)  and  Readme.md files. If only 1 format is used in a package, prefer to utilize a package to alternate if required.
	- https://stackoverflow.com/questions/10718767/have-the-same-readme-both-in-markdown-and-restructuredtext

## Steps - Overview

| Step |  Description | Commands/Detailed Description | Reference |
|---|---|---|---|
| 1 | Create python project with directory structure | Follow pep8 guidelines | [https://www.freecodecamp.org/news/build-your-first-python-package/](https://www.freecodecamp.org/news/build-your-first-python-package/) |
| 2 | Package compliance | Ensure all directories are package modules using __init__.py  | [https://www.freecodecamp.org/news/build-your-first-python-package/](https://www.freecodecamp.org/news/build-your-first-python-package/) |
| 3 | Add setup.py and build wheels | python setup.py sdist bdist_wheel  | [https://www.freecodecamp.org/news/build-your-first-python-package/](https://www.freecodecamp.org/news/build-your-first-python-package/)|
| 4 | Create account on pypi and upload using twine package | These commands will push the .whl and .tar.gz file into the pypi repository <br> conda install twine <br> twine upload dist/*  | [https://www.freecodecamp.org/news/build-your-first-python-package/](https://www.freecodecamp.org/news/build-your-first-python-package/)|


### References

[https://www.freecodecamp.org/news/build-your-first-python-package/](https://www.freecodecamp.org/news/build-your-first-python-package/)

[https://python-packaging-tutorial.readthedocs.io/en/latest/setup_py.html](https://python-packaging-tutorial.readthedocs.io/en/latest/setup_py.html)

[https://packaging.python.org/](https://packaging.python.org/)

Guidelines to contribute to libraries:
[https://pandas.pydata.org/docs/development/contributing.html#contributing](https://pandas.pydata.org/docs/development/contributing.html#contributing)
