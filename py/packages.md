

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



[https://realpython.com/pypi-publish-python-package/](https://realpython.com/pypi-publish-python-package/)

Python wheels are great. Building them across Mac, Linux, Windows, on multiple versions of Python, is not. cibuildwheel is here to help. See link below
[https://pypi.org/project/cibuildwheel/](https://pypi.org/project/cibuildwheel/)

More CI/CD streamlining for python packages:
- use cookiecutter to generate a package template
- set up travis CI for auto deployment of package to pypi


https://github.com/audreyfeldroy/cookiecutter-pypackage
https://cookiecutter-pypackage.readthedocs.io/en/latest/tutorial.html
https://pypi.org/project/cookiecutter/


## CI

Helps cover testing, test coverage, etc.

### Github CI

https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python

https://hynek.me/articles/python-github-actions/


### Travis CI

https://jacobtomlinson.dev/posts/2021/testing-and-continuous-integration-for-python-packages-with-github-actions/
https://github.com/ksator/continuous-integration-with-python

https://medium.com/swlh/automate-python-testing-with-github-actions-7926b5d8a865

## Steps - Overview (Using twine)

| Step |  Description | Commands/Detailed Description | Reference |
|---|---|---|---|
| 1 | Create python project with directory structure | Follow pep8 guidelines | [https://www.freecodecamp.org/news/build-your-first-python-package/](https://www.freecodecamp.org/news/build-your-first-python-package/) |
| 2 | Package compliance | Ensure all directories are package modules using __init__.py  | [https://www.freecodecamp.org/news/build-your-first-python-package/](https://www.freecodecamp.org/news/build-your-first-python-package/) |
| 3 | Add setup.py and build wheels | python setup.py sdist bdist_wheel  | [https://www.freecodecamp.org/news/build-your-first-python-package/](https://www.freecodecamp.org/news/build-your-first-python-package/)|
| 4 | Create account on pypi and upload using twine package | These commands will push the .whl and .tar.gz file into the pypi repository <br> conda install twine <br> twine upload dist/*  | [https://www.freecodecamp.org/news/build-your-first-python-package/](https://www.freecodecamp.org/news/build-your-first-python-package/)|


## Steps - Overview (Using toml file, bumpver and twine )

| Step |  Description | Commands/Detailed Description | Reference |
|---|---|---|---|
| 1 | Create python project with directory structure | Follow pep8 guidelines | [https://www.freecodecamp.org/news/build-your-first-python-package/](https://www.freecodecamp.org/news/build-your-first-python-package/) |
| 2 | Package compliance | Ensure all directories are package modules using __init__.py  | [https://www.freecodecamp.org/news/build-your-first-python-package/](https://www.freecodecamp.org/news/build-your-first-python-package/) |
| 3 | Add .toml file and setup.py to build wheels | pip install bumpver <br> bumpver update --patch  <br> pip install build <br> python -m build | https://realpython.com/pypi-publish-python-package/ |
| 4 | Create account on pypi and upload using twine package | These commands will push the .whl and .tar.gz file into the pypi repository <br> conda install twine <br> twine upload dist/*  | https://realpython.com/pypi-publish-python-package/ |


### Building A Package Locally

•	Add following package to the base environment
o	Install conda-buiild
o	Conda install conda-build
•	Utilize the below to build the package in current path. A specific path can also be specified.
o	Conda develop . 
o	https://docs.conda.io/projects/conda-build/en/latest/user-guide/tutorials/build-pkgs.html


### Testing A Package Locally

A package can be imported locally from another code and thoroughly tested as well if required. The steps to do so are:
- TBA


### References

[https://www.freecodecamp.org/news/build-your-first-python-package/](https://www.freecodecamp.org/news/build-your-first-python-package/)

[https://python-packaging-tutorial.readthedocs.io/en/latest/setup_py.html](https://python-packaging-tutorial.readthedocs.io/en/latest/setup_py.html)

[https://packaging.python.org/](https://packaging.python.org/)

Guidelines to contribute to libraries:
[https://pandas.pydata.org/docs/development/contributing.html#contributing](https://pandas.pydata.org/docs/development/contributing.html#contributing)

https://realpython.com/pypi-publish-python-package/
