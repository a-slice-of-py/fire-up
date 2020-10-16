# FireUp 🔥👆

FireUp is a stripped-to-bare-bones Python project template creator.

It somehow resembles projects like [Cookiecutter](https://github.com/cookiecutter/cookiecutter) or [PyScaffold](https://github.com/pyscaffold/pyscaffold) regarding the shared aim, but it has been designed with a crucial difference in its premise. FireUp goal is to provide a hard-coded and restricted set of template features while reducing at most the dependencies required to do so.

The main features are:

- [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/home.html) app folder;
- [Streamlit](https://www.streamlit.io/) dashboard template, used as project entry point configured via [Hydra](https://hydra.cc/docs/intro/);
- [Docker Compose](https://docs.docker.com/compose/) support via Dockerfile and docker-compose.yml templates;
- project documentation provided by [MkDocs](https://www.mkdocs.org/), with [Material theme](https://squidfunk.github.io/mkdocs-material/getting-started/) and [mkdocstrings](https://github.com/pawamoy/mkdocstrings) for automated Google docstrings documentation;
- sample [Jupyter Notebook](https://jupyter.org/);
- tests folder for unit testing with [pytest](https://github.com/pytest-dev/pytest/) and logging via [Loguru](https://github.com/Delgan/loguru);
- [Makefile](https://www.gnu.org/software/make/) support for basic tasks execution;
- [pipreqs](https://github.com/bndr/pipreqs) support for improved requirements creation;
- [python-dotenv](https://github.com/theskumar/python-dotenv) support for environment variables management.

Its name is inspired to [Google's Python Fire](https://github.com/google/python-fire#why-is-it-called-fire): while it fires off a Python script, FireUp lets you to initialize your Python project.

## Prerequisites

You need just three ingredients to fully use FireUp:

- [Python](https://www.python.org/downloads/) (>= 3.6)
- [GNU Make](https://www.gnu.org/software/make/)
- [virtualenv](https://virtualenv.pypa.io/en/latest/)
- [Click](https://click.palletsprojects.com/en/7.x/#documentation)
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) configured and [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/home.html) installed

## Usage

To initialize a new python project with FireUp, all you need to do is clone this gist repo and install FireUp via `pip install -e .` in the virtual enviroment you want to run your experiments. It's now sufficient to execute

```python
fireup
```

and you will be prompted for project creation setup. Once the project folder has been created, you can cd into it from your base Python enviroment and execute `make create-env`.

You are now ready to further setup your project switching to the brand new enviroment and browsing all the default possibilities through `make help`.
