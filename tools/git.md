## Introduction

Git is a Verson control tool

## Summary




## General Workflows

[https://guides.github.com/introduction/flow/](https://guides.github.com/introduction/flow/)

### Cloning a repo
Git cloning instructions:
- Copy the repository link in git bash 
    - $git  clone <repository_url>
    - $git  clone https://vamseeachanta@dev.azure.com/vamseeachanta/aceengineer/_git/aceengineer



### Forking a repo

### Cloning vs. Forking

### Code Development

The typical workflow followed in Azure Devops is given below:
- Pull the latest master code
- The typical workflow followed in Azure Devops is given below:
    - Pull the latest master code
    - Start working on your local branch
- Create a local branch (Never work in master on your computer)
    - git branch <branchname>
    - git branch <ExistingCodes>
    - or use GUI alternatively as below and create “New Branch”
- Checkout the local branch
    - Git branch (to view all the existing branches)
    - git checkout <branchname>
    - git checkout <ExistingCodes>
- Create files, edit codes per the project needs

When branch is ready for review (and/or approval):
- Push the branch to the origin
    - Commit the relevant files in following steps
    - Add the files:
        - git add –A (Add all files)
        - git add ASMEB31\ASMEB31Sizing.py (Add all files)
    - Git commit -m "Initial Push"
    - Push the files to the origin 
        - git push -u origin <branch>
        - git push -u origin <ExistingCodes>
- Create a pull request
    - Go to Azure devops or github website
    - Create the pull request
-	Copy the person who should be reviewing the code in the pull request.




### Rebase

Git Rebase. Always rebase the local branch that typically (way) behind master. Rebase is more easier to merge stale code than direct merge.

- Working steps in PyCharm:
    - Pre-steps:
    - Ensure the latest master branch (or intended commit) is pulled into local
- Execution steps:
    - Select the select branch (intended) to rebase 
    - Click (but do not select) on Master branch menu
    - Click rebase current (i.e. select branch) onto Selected (i.e. master).
- Key references:

https://stackoverflow.com/questions/804115/when-do-you-use-git-rebase-instead-of-git-merge
https://www.perforce.com/blog/vcs/git-rebase-vs-merge-which-better
https://www.atlassian.com/git/tutorials/merging-vs-rebasing


## Installation


If version shows up, this means that git is successfully installed. 
Check Installation and version
git –version

Install using the below link:

[https://git-scm.com/download/win](https://git-scm.com/download/win)

## Files to ignore guidance

|   Language |  Extensions |  Links |   comments |
|---|---|---|---|
| Python  | *.pyc | - | n/a | 


## References

| S.No |   Short Description |  Comment |  Links |   Additional comments |
|---|---|---|---|---|
| 1 | Intro  | A very good Git intro video | [https://www.youtube.com/watch?v=HVsySz-h9r4](https://www.youtube.com/watch?v=HVsySz-h9r4) | n/a | 
| 2 | Add .gitignore file  | - | [https://stackoverflow.com/questions/10744305/how-to-create-gitignore-file	](https://stackoverflow.com/questions/10744305/how-to-create-gitignore-file	) |  |
| 3 | Branch Features and Production  | - | [http://nvie.com/posts/a-successful-git-branching-model/](http://nvie.com/posts/a-successful-git-branching-model/) |  |
| 4 | sparseCheckout  | - | [http://scriptedonachip.com/git-sparse-checkout	](http://scriptedonachip.com/git-sparse-checkout) |  |
| 5 | clone only a subdirectory  | - | [https://stackoverflow.com/questions/600079/how-do-i-clone-a-subdirectory-only-of-a-git-repository](https://stackoverflow.com/questions/600079/how-do-i-clone-a-subdirectory-only-of-a-git-repository) |  |
| 6 | submodules  | - | [https://git-scm.com/book/en/v2/Git-Tools-Submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules) |  |
| 7 | cheatsheet  | - | [https://github.com/github/training-kit/blob/master/downloads/github-git-cheat-sheet.md](https://github.com/github/training-kit/blob/master/downloads/github-git-cheat-sheet.md) |  |



