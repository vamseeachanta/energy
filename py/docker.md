#	Introduction


# Summary


# Example go-by Code

### Python Environment - Conda Route

Example file:
<pre>
FROM continuumio/miniconda

ARG conda_env=my_env

WORKDIR /app
ADD . /app/

RUN conda update conda
RUN conda config --set ssl_verify False
RUN conda env create -f environment.yml

# Make RUN commands use the new environment:
ENV PATH /opt/conda/envs/$conda_env/bin:$PATH
ENV CONDA_DEFAULT_ENV $conda_env

EXPOSE 5005

# The code to run when container is started:
CMD ["python", "/app/temp_service.py"]
</pre>



Other helpful commands:

Activating environment (NOT working):
<pre>
RUN conda init bash
RUN conda activate my_env
</pre>

Check if Flask is installed:
<pre>
RUN echo "Make sure flask is installed:"
RUN python -c "import flask"
</pre>


Activating environment (working?) and run a code (NOT working) using SHELL & ENTRYPOINT:
<pre>
SHELL ["conda", "run", "-n", "my_env", "/bin/bash", "-c"]
ENTRYPOINT ["conda", "run", "-n", "my_env", "python3", "/app/temp_service.py"]
</pre>

Activating environment (working?) and run a code (NOT working) using SHELL & ENTRYPOINT:
<pre>
SHELL ["conda", "run", "-n", "my_env", "/bin/bash", "-c"]
ENTRYPOINT ["conda", "run", "-n", "my_env", "python3", "/app/temp_service.py"]
</pre>

### Python Environment - pip Route

Example file:
<pre>
FROM python:3.7.9

RUN mkdir /app
WORKDIR /app
ADD . /app/

RUN pip3 install --upgrade pip --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org
#RUN pip3 install -r requirements.txt
RUN pip3 install Flask flask-restplus --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org

EXPOSE 5005
CMD ["python", "/app/temp_service.py"]
</pre>

