## Introduction

Typically python enviornments and associated libraries is installed using a package manager like Conda. The following instructions will help install Miniconda, a minimal installer for conda.

### Installation Steps

- If reinstalling conda:
    - backup any conda environments you might be interested in. Export packages using conda env export. [https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
    - Uninstall the existing version of Anaconda/ Miniconda.

- Navigate to https://docs.conda.io/en/latest/miniconda.html
    - Pick the installer based on your Operating System, python version and processor type (32 bit vs 64 bit).  
        - recommend python version >= 3.7.x
        - Under Installation Type, select the "Just Me" option.

    - Keep the default options for the rest of the installation screens. 
    - In the final screen, the installation should complete usually within 5 minutes.


The following actions will resolve typical SSL errors encountered during package installations. These will also be helpful when inside typical corporate firewalls:

- For Conda SSL errors:
    - Open miniconda prompt:
        - Go to Start > Search for Miniconda
        - Open Miniconda Command Prompt
    -  Run following commands inside Miniconda shell to disable ssl and increase timeout to 20 mins     
    <pre> conda config --set ssl_verify False   
    conda config --set remote_read_timeout_secs 2000 
    </pre>
    - Close and reopen the shell for the settings to take effect.

- For pip SSL errors:
    - Create directory C:\Users\<<user_network_id>>\pip 
    - copy pip.ini, see [py\ref\pip.ini](py\ref\pip.ini) to above created pip directory.

