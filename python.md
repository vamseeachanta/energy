## Introduction

The document describes the python learning for typical programming:

## Summary

- follow guidelines as a good samaritan, [good_samaritan_guidelines.md](good_samaritan_guidelines.md)

- See "First Steps" section below


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

- Why is Refactoring important?

[https://github.com/bmihovski/software-development-ebooks-1/blob/master/%5BRefactoring%20Improving%20the%20Design%20of%20Existing%20Code%20(Addison-Wesley%20Object%20Technology%20Series)%20Kindle%20Edition%20by%20Martin%20Fowler%20-%202002%5D.pdf](https://github.com/bmihovski/software-development-ebooks-1/blob/master/%5BRefactoring%20Improving%20the%20Design%20of%20Existing%20Code%20(Addison-Wesley%20Object%20Technology%20Series)%20Kindle%20Edition%20by%20Martin%20Fowler%20-%202002%5D.pdf)

### End of learning Checklist

The key python learnings are:
- data structures
- classes and class functions
- virtual environments
- 


### First Steps (Week 3)

- listen to all the podcasts to get good idea of what is possible using the technology

- Create account in below website
    - dev.azure.com

- Learn Test Driven Development (TDD) principles

### Technology Training (Weeks 3, 4, 5, 6, 7)

- Start the course work given in summary
- document all the learnings in the repository
- save all code as programming (.py) files


- Pick 5 full stack projects from below link
    - https://compscicentral.com/python-projects/
	- https://dev.to/mrsaeeddev/5-absolutely-free-projects-you-should-do-to-become-a-full-stack-superman-before-the-2020-ends-2ci1
	- https://www.upgrad.com/blog/full-stack-projects-github-beginners/

    - for each project:
        - document the project in md file
            - exlain the architecture
            - learn about plantuml using document: [tools\plantuml.md](tools\plantuml.md)
            - draw project flowchart(s) in plantuml
                - an overview flowchart
                - detailed flowcharts as needed
        - Run project in playground
        - add tests to demonstrate test driven development principles:
			- 2-3 unit tests 
			- 2-3 behavior (BDD) tests 

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

### References

https://tutswiki.com/python/