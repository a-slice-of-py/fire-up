# FireUp!

FireUp is a stripped-to-bare-bones Python project template creator. 

It somehow resembles projects like [`cookiecutter`](https://github.com/cookiecutter/cookiecutter) or [`pyscaffold`](https://github.com/pyscaffold/pyscaffold) regarding the shared aim, but it has been designed with a crucial difference in its premise. FireUp goal is to provide a hard-coded and restricted set of template features while reducing at most the dependencies required to do so.

## Prerequisites

You need just three ingredients to fully use FireUp:
- python (>= 3.6)
- gnu make
- virtualenv

## Usage
To initialize a new python project with FireUp, all you need to do is copy `fire_up.py` in your dev enviroment and execute the following
```python
python fire_up.py --project-name <PROJECT_NAME>
```
replacing `<PROJECT_NAME>` with the desired name for your project.

You can also set via cli other arguments, as the directory in which the project must be initialized and author's name and email.

Once the project folder has been created, you can cd into it from your base Python enviroment and execute `make create-env` (which requires `virtualenv` to be installed in your base env). 

You are now ready to further setup your project switching to the brand new enviroment and browsing all the default possibilities through `make help`.