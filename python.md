## Introduction
The document describes the python principles to be the followed for the python repositories:

## Summary

The key python learnings are:
- data structures
- classes and class functions
- virtual environments
- 
- TBA

Recommended course on Udemy is:
[https://www.udemy.com/course/the-python-pro-course/](https://www.udemy.com/course/the-python-pro-course/)


- See "First Steps" section below

- Course work:
    - preferred:
        - https://www.udemy.com/course/salesforce-development/
    - further courses under review are below:
        - https://www.udemy.com/courses/search/?q=salesforce+developer&src=sac&kw=salesforce

- Podcasts:
    - [https://realpython.com/podcasts/rpp/](https://realpython.com/podcasts/rpp/)

### First Steps (Week 3)

- listen to all the podcasts to get good idea of what is possible using the technology

- Create account in below website
    - dev.azure.com

- Pick 5 projects from below link
    - https://developer.salesforce.com/code-samples-and-sdks
    - for each project:
        - document the project in md file
            - exlain the architecture
            - learn about plantuml using document: [tools\plantuml.md](tools\plantuml.md)
            - draw project flowchart(s) in plantuml
        - Run the project

- Learn Test Driven Development (TDD) principles

### Course work (Weeks 3, 4, 5, 6, 7)
- Start the course work given in summary
- document all the learnings in the repository
- save all code as programming (.py) files

## Conda Environments

Install miniconda using the instructions in [py\installation_miniconda.md](py\installation_miniconda.md)

## Conda vs. Pip

Conda and pip are package managers. A comparison between pip and conda is given in link below.

Virtual environments can be created using either conda or pip or combination. 

https://towardsdatascience.com/a-guide-to-conda-environments-bc6180fc533
https://conda.io/projects/conda/en/latest/commands.html#conda-vs-pip-vs-virtualenv-commands
https://www.anaconda.com/understanding-conda-and-pip/


### General working

### IDE: VS Code 

For general working in VS code:
[https://code.visualstudio.com/docs/languages/python](https://code.visualstudio.com/docs/languages/python)

The typical extensions required are:
- Python (from Microsoft)
- Python Extension Pack

Setting up the project specific environment:
- ?

### CI/CD Deployments

- If altering environment, consider the following:
  - delete environment and recreate fresh. 
    - This will help avoid run time performance issues. 
	- Possibly remnant files/folders confuse the python process
	- Also, if a fast route compilation (numba) is used. Without warning the numba can be disabled.
  - This will require disabling the tasks or kill ongoing tasks in a server machine

