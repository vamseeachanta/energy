REM Runs in Anaconda windows prompt
ECHO Setting up Anaconda Python environment
CALL conda create -n ML_env1 python=3.5
CALL activate ML_env1
CALL conda install numpy
CALL conda install pandas
CALL conda install scikit-learn
CALL conda install matplotlib
ECHO Run "deactivate ML_env1" to exit virtual environment
ECHO Run "activate ML_env1" to enter dynaCard_env virtual environment
ECHO To remove virtual environment, Deactivate and Remove using following instructions
ECHO "deactivate ML_env1"
ECHO "conda-env remove -n ML_env1"
ECHO Run "spyder" to open IDE and work in Python
ECHO Location of virtual environment is "Active_Python_folder\envs\ML_env1"
REM
