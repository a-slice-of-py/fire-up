#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import textwrap
import datetime
import argparse

class FireUp:

    def __init__(self,
                 project_name='new_project',
                 author='placeholder',
                 email='placeholder'
                ):

        format_code = lambda x: textwrap.dedent(x).strip()
        project_name = project_name.replace(' ', '_')
        today = str(datetime.datetime.now().date()).replace('-','')
        year = today[:4]
        requirements = ['pandas>=1.0.3', 'numpy>=1.18.0', 'plotly>=4.5.4', 'streamlit>=0.56.0']
        project_name_str = ''.join(list(map(lambda x: x.capitalize(), f'{project_name}'.split('_'))))

        streamlit_code = format_code(
            f'''
            #!/usr/bin/env python3
            # -*- coding: utf-8 -*-

            import streamlit as st
            import sys
            sys.path.append('../{project_name}')
            from {project_name} import {project_name}

            def main():
                st.sidebar.markdown("# {project_name_str}")
                st.write("# Hello from {project_name_str}!")
                st.write({project_name}.{project_name}_test("{project_name} successfully tested!"))

            if __name__ == "__main__":
                main()
            '''
        )

        notebook_code = format_code(
            f'''
            {{
            "cells": [
            {{
            "cell_type": "code",
            "metadata": {{
            }},
            "outputs": [],
            "source": [
                "import sys\\n",
                "sys.path.append('../{project_name}')\\n",
                "from {project_name} import {project_name}\\n",
                "\\n",
                "{project_name}.{project_name}_test('{project_name} successfully tested!')"
            ]
            }}
            ],
            "metadata": {{
            }},
            "nbformat": 4,
            "nbformat_minor": 2
            }}
            '''
        )

        sphinx_conf_code = format_code(
            f'''
            # Configuration file for the Sphinx documentation builder.
            #
            # This file only contains a selection of the most common options. For a full
            # list see the documentation:
            # https://www.sphinx-doc.org/en/master/usage/configuration.html

            # -- Path setup --------------------------------------------------------------

            # If extensions (or modules to document with autodoc) are in another directory,
            # add these directories to sys.path here. If the directory is relative to the
            # documentation root, use os.path.abspath to make it absolute, like shown here.
            #
            import os
            import sys
            sys.path.insert(0, os.path.abspath("../{project_name}"))

            numpydoc_show_class_members = False
            # -- Project information -----------------------------------------------------

            project = '{project_name_str}'
            copyright = '{year}, {author}'
            author = '{author}'

            # The full version, including alpha/beta/rc tags
            release = '1.0.0'

            # -- General configuration ---------------------------------------------------

            # Add any Sphinx extension module names here, as strings. They can be
            # extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
            # ones.
            extensions = ['sphinx.ext.napoleon', 'autoapi.extension']

            # Autoapi settings.
            autoapi_dirs = ['../{project_name}']
            autoapi_keep_files = True

            # Napoleon extension settings.
            napoleon_google_docstring = True
            napoleon_numpy_docstring = True
            napoleon_include_init_with_doc = True
            napoleon_include_private_with_doc = True
            napoleon_include_special_with_doc = True
            napoleon_use_admonition_for_examples = False
            napoleon_use_admonition_for_notes = False
            napoleon_use_admonition_for_references = False
            napoleon_use_ivar = False
            napoleon_use_param = True
            napoleon_use_keyword = True
            napoleon_use_rtype = False

            # Add any paths that contain templates here, relative to this directory.
            templates_path = ['_templates']

            # List of patterns, relative to source directory, that match files and
            # directories to ignore when looking for source files.
            # This pattern also affects html_static_path and html_extra_path.
            exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

            # -- Options for HTML output -------------------------------------------------

            # The theme to use for HTML and HTML Help pages.  See the documentation for
            # a list of builtin themes.
            #
            html_theme = 'sphinx_rtd_theme'

            # Add any paths that contain custom static files (such as style sheets) here,
            # relative to this directory. They are copied after the builtin static files,
            # so a file named "default.css" will overwrite the builtin "default.css".
            html_static_path = ['_static']
            '''
        )

        sphinx_index_code = format_code(
            f'''
            .. {project_name_str} documentation master file, created by
               sphinx-quickstart on {today}.
               You can adapt this file completely to your liking, but it should at least
               contain the root `toctree` directive.

            Welcome to {project_name_str} documentation!
            =============================================================================

            .. toctree::
               :maxdepth: 2
               :caption: Contents:

               {project_name}

            Indices and tables
            ==================

            * :ref:`genindex`
            * :ref:`modindex`
            * :ref:`search`
            '''
        )

        sphinx_package_code = format_code(
            f'''
            {project_name} module
            =============

            .. automodule:: {project_name}
               :members:
               :undoc-members:
               :inherited-members:
               :show-inheritance:
               :private-members:
            '''
        )

        sphinx_makebat_code = format_code(
            f'''
            @ECHO OFF

            pushd %~dp0

            REM Command file for Sphinx documentation

            if "%SPHINXBUILD%" == "" (
                set SPHINXBUILD=sphinx-build
            )
            set SOURCEDIR=.
            set BUILDDIR=_build

            if "%1" == "" goto help

            %SPHINXBUILD% >NUL 2>NUL
            if errorlevel 9009 (
                echo.
                echo.The 'sphinx-build' command was not found. Make sure you have Sphinx
                echo.installed, then set the SPHINXBUILD environment variable to point
                echo.to the full path of the 'sphinx-build' executable. Alternatively you
                echo.may add the Sphinx directory to PATH.
                echo.
                echo.If you don't have Sphinx installed, grab it from
                echo.http://sphinx-doc.org/
                exit /b 1
            )

            %SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
            goto end

            :help
            %SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%

            :end
            popd
            '''
        )

        sphinx_makefile_code = format_code(
            f'''
            # Minimal makefile for Sphinx documentation
            #

            # You can set these variables from the command line, and also
            # from the environment for the first two.
            SPHINXOPTS    ?=
            SPHINXBUILD   ?= sphinx-build
            SOURCEDIR     = .
            BUILDDIR      = _build

            # Put it first so that "make" without argument is like "make help".
            help:
                @$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

            .PHONY: help Makefile

            # Catch-all target: route all unknown targets to Sphinx using the new
            # "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
            %: Makefile
                @$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
            '''
        )

        readme_code = format_code(
            f'''
            # {project_name_str}
            {project_name_str} is a Python package.
            ## Installation
            Use the package manager [pip](https://pip.pypa.io/en/stable/) to install {project_name} in edit mode.
            ```python
            pip install -e . # in the root folder (look for setup.py)
            ```
            ## Usage
            ### Requirements
            Install [pipreqs](https://pypi.org/project/pipreqs/) via `pip` and execute the following in the root folder
            ```python
            >>> pipreqs ./
            ```
            to save dependencies to ./requirements.txt.
            ### Git
            Cheatsheet for basic `git` usage (recommended w/ GitKraken 6.5.1):
            - `git init` in the root folder to initialize repository
            - `git status` to check Git staging area status
            - `git add .` to add every unstaged file to the Git repository
            - `git commit -m <message>` to commit staged files
            - `git log` to obtain commit log history
            - `git checkout <commit_id>` to step back/forward to a given commit
            - `git push` to push to remote repository
            - `git pull` to pull from remote repository
            - `git merge` to merge two branches
            ### Sphinx
            Install both [sphinx](https://www.sphinx-doc.org/en/master/usage/installation.html), [sphinxcontrib-napoleon](https://pypi.org/project/sphinxcontrib-napoleon/) and [sphinx-autoapi](https://pypi.org/project/sphinx-autoapi/) via `pip` (recommended usage w/ Visual Studio Code `autoDocstring` extension). Then, execute the following in the root directory to build html docs
            ```python
            >>> cd ./docs
            >>> make clean && make html
            ```
            ### Streamlit
            Install [streamlit](https://docs.streamlit.io/) via `pip` and execute the following in the root folder to run Streamlit sample app (by default on port 8501)
            ```python
            >>> cd ./app
            >>> streamlit run {project_name}_app.py
            ```
            ### Docker
            Cheatsheet for basic Docker usage:
            - `docker image build -t <image_name> .` in the root folder (look for Dockerfile) to build project image attached to the terminal
            - `docker container run --publish <forward_port>:<container_port> --detach --name <container_alias> <image_name>` to launch container (runnable instance of the given image) detached from the terminal
            - `docker container rm --force <container_alias>` to shutdown the given container
            ## Authors
            * **{author}**
            '''
        )

        setup_code = format_code(
            f'''
            """A setuptools based setup module.
            See:
            https://packaging.python.org/guides/distributing-packages-using-setuptools/
            https://github.com/pypa/sampleproject
            """

            # Always prefer setuptools over distutils
            from setuptools import setup, find_packages
            from os import path

            # Arguments marked as "Required" below must be included for upload to PyPI.
            # Fields marked as "Optional" may be commented out.

            setup(
                # This is the name of your project. The first time you publish this
                # package, this name will be registered for you. It will determine how
                # users can install this project, e.g.:
                #
                # $ pip install sampleproject
                #
                # And where it will live on PyPI: https://pypi.org/project/sampleproject/
                #
                # There are some restrictions on what makes a valid project name
                # specification here:
                # https://packaging.python.org/specifications/core-metadata/#name
                name='{project_name}',  # Required

                # Versions should comply with PEP 440:
                # https://www.python.org/dev/peps/pep-0440/
                #
                # For a discussion on single-sourcing the version across setup.py and the
                # project code, see
                # https://packaging.python.org/en/latest/single_source_version.html
                version='1.0.0',  # Required

                # This is a one-line description or tagline of what your project does. This
                # corresponds to the "Summary" metadata field:
                # https://packaging.python.org/specifications/core-metadata/#summary
                description='{project_name_str}',  # Optional

                # This should be your name or the name of the organization which owns the
                # project.
                author='{author}',  # Optional

                # This should be a valid email address corresponding to the author listed
                # above.
                author_email='{email}',  # Optional

                # This field adds keywords for your project which will appear on the
                # project page. What does your project relate to?
                #
                # Note that this is a string of words separated by whitespace, not a list.
                keywords='sample setuptools development',  # Optional

                # When your source code is in a subdirectory under the project root, e.g.
                # `src/`, it is necessary to specify the `package_dir` argument.
                package_dir={{'': '{project_name}'}},  # Optional

                # You can just specify package directories manually here if your project is
                # simple. Or you can use find_packages().
                #
                # Alternatively, if you just want to distribute a single Python file, use
                # the `py_modules` argument instead as follows, which will expect a file
                # called `my_module.py` to exist:
                #
                #   py_modules=["my_module"],
                #
                packages=find_packages(where='{project_name}'),  # Required

                # Specify which Python versions you support. In contrast to the
                # 'Programming Language' classifiers above, 'pip install' will check this
                # and refuse to install the project if the version does not match. If you
                # do not support Python 2, you can simplify this to '>=3.5' or similar, see
                # https://packaging.python.org/guides/distributing-packages-using-setuptools/#python-requires
                python_requires='>=3.5',

                # This field lists other packages that your project depends on to run.
                # Any package you put here will be installed by pip when your project is
                # installed, so they must be valid existing projects.
                #
                # For an analysis of "install_requires" vs pip's requirements files see:
                # https://packaging.python.org/en/latest/requirements.html
                install_requires={requirements},  # Optional
            )
            '''
        )

        git_code = format_code(
            f'''

            # Created by https://www.gitignore.io/api/osx,linux,python,windows,pycharm,visualstudiocode

            ### Linux ###
            *~

            # temporary files which can be created if a process still has a handle open of a deleted file
            .fuse_hidden*

            # KDE directory preferences
            .directory

            # Linux trash folder which might appear on any partition or disk
            .Trash-*

            # .nfs files are created when an open file is removed but is still being accessed
            .nfs*

            ### OSX ###
            *.DS_Store
            .AppleDouble
            .LSOverride

            # Icon must end with two \r
            Icon

            # Thumbnails
            ._*

            # Files that might appear in the root of a volume
            .DocumentRevisions-V100
            .fseventsd
            .Spotlight-V100
            .TemporaryItems
            .Trashes
            .VolumeIcon.icns
            .com.apple.timemachine.donotpresent

            # Directories potentially created on remote AFP share
            .AppleDB
            .AppleDesktop
            Network Trash Folder
            Temporary Items
            .apdisk

            ### PyCharm ###
            # Covers JetBrains IDEs: IntelliJ, RubyMine, PhpStorm, AppCode, PyCharm, CLion, Android Studio and Webstorm
            # Reference: https://intellij-support.jetbrains.com/hc/en-us/articles/206544839

            # User-specific stuff:
            .idea/**/workspace.xml
            .idea/**/tasks.xml
            .idea/dictionaries

            # Sensitive or high-churn files:
            .idea/**/dataSources/
            .idea/**/dataSources.ids
            .idea/**/dataSources.xml
            .idea/**/dataSources.local.xml
            .idea/**/sqlDataSources.xml
            .idea/**/dynamic.xml
            .idea/**/uiDesigner.xml

            # Gradle:
            .idea/**/gradle.xml
            .idea/**/libraries

            # CMake
            cmake-build-debug/

            # Mongo Explorer plugin:
            .idea/**/mongoSettings.xml

            ## File-based project format:
            *.iws

            ## Plugin-specific files:

            # IntelliJ
            /out/

            # mpeltonen/sbt-idea plugin
            .idea_modules/

            # JIRA plugin
            atlassian-ide-plugin.xml

            # Cursive Clojure plugin
            .idea/replstate.xml

            # Ruby plugin and RubyMine
            /.rakeTasks

            # Crashlytics plugin (for Android Studio and IntelliJ)
            com_crashlytics_export_strings.xml
            crashlytics.properties
            crashlytics-build.properties
            fabric.properties

            ### PyCharm Patch ###
            # Comment Reason: https://github.com/joeblau/gitignore.io/issues/186#issuecomment-215987721

            # *.iml
            # modules.xml
            # .idea/misc.xml
            # *.ipr

            # Sonarlint plugin
            .idea/sonarlint

            ### Python ###
            # Byte-compiled / optimized / DLL files
            __pycache__/
            *.py[cod]
            *$py.class

            # C extensions
            *.so

            # Distribution / packaging
            .Python
            build/
            develop-eggs/
            dist/
            downloads/
            eggs/
            .eggs/
            lib/
            lib64/
            parts/
            sdist/
            var/
            wheels/
            *.egg-info/
            .installed.cfg
            *.egg

            # PyInstaller
            #  Usually these files are written by a python script from a template
            #  before PyInstaller builds the exe, so as to inject date/other infos into it.
            *.manifest
            *.spec

            # Installer logs
            pip-log.txt
            pip-delete-this-directory.txt

            # Unit test / coverage reports
            htmlcov/
            .tox/
            .coverage
            .coverage.*
            .cache
            .pytest_cache/
            nosetests.xml
            coverage.xml
            *.cover
            .hypothesis/

            # Translations
            *.mo
            *.pot

            # Flask stuff:
            instance/
            .webassets-cache

            # Scrapy stuff:
            .scrapy

            # Sphinx documentation
            docs/_build/
            **/Makefile
            autoapi

            # PyBuilder
            target/

            # Jupyter Notebook
            .ipynb_checkpoints
            *.ipynb*

            # pyenv
            .python-version

            # celery beat schedule file
            celerybeat-schedule.*

            # SageMath parsed files
            *.sage.py

            # Environments
            .env
            .venv
            env/
            venv/
            ENV/
            env.bak/
            venv.bak/

            # Spyder project settings
            .spyderproject
            .spyproject

            # Rope project settings
            .ropeproject

            # mkdocs documentation
            /site

            # mypy
            .mypy_cache/

            ### VisualStudioCode ###
            .vscode/*
            !.vscode/settings.json
            !.vscode/tasks.json
            !.vscode/launch.json
            !.vscode/extensions.json
            .history

            ### Windows ###
            # Windows thumbnail cache files
            Thumbs.db
            ehthumbs.db
            ehthumbs_vista.db

            # Folder config file
            Desktop.ini

            # Recycle Bin used on file shares
            $RECYCLE.BIN/

            # Windows Installer files
            *.cab
            *.msi
            *.msm
            *.msp

            # Windows shortcuts
            *.lnk

            # Build folder

            */build/*

            # Chalice build
            .chalice/deployments/

            # charts
            *.pdf
            *.pptx

            # text documents
            *.doc
            *.docx

            # xlsx and csv
            *.xls
            *.xlsx
            *.csv

            # JPEG
            *.jpg
            *.jpeg
            *.jpe
            *.jif
            *.jfif
            *.jfi

            # JPEG 2000
            *.jp2
            *.j2k
            *.jpf
            *.jpx
            *.jpm
            *.mj2

            # JPEG XR
            *.jxr
            *.hdp
            *.wdp

            # Graphics Interchange Format
            *.gif

            # RAW
            *.raw

            # Web P
            *.webp

            # Portable Network Graphics
            *.png

            # Animated Portable Network Graphics
            *.apng

            # Multiple-image Network Graphics
            *.mng

            # Tagged Image File Format
            *.tiff
            *.tif

            # Scalable Vector Graphics
            *.svg
            *.svgz

            # Portable Document Format
            *.pdf

            # X BitMap
            *.xbm

            # BMP
            *.bmp
            *.dib


            # End of https://www.gitignore.io/api/osx,linux,python,windows,pycharm,visualstudiocode
            '''
        )

        docker_code = format_code(
            f'''
            # Copyright (c).
            # Confidential and intended for internal use only.

            # base image
            ARG BASE_CONTAINER=python:3.7
            FROM $BASE_CONTAINER

            LABEL maintainer="{author} <{email}>"

            # Copy project files
            COPY ./ /./

            # streamlit-specific commands
            RUN mkdir -p /root/.streamlit
            RUN bash -c 'echo -e "\
            [general]\n\
            email = \"\"\n\
            " > /root/.streamlit/credentials.toml'
            RUN bash -c 'echo -e "\
            [server]\n\
            enableCORS = false\n\
            " > /root/.streamlit/config.toml'

            # exposing default port for streamlit
            EXPOSE 8501

            # copy over and install packages
            RUN pip install -r ./requirements.txt

            # run app
            CMD streamlit run ./app/{project_name}_app.py
            '''
        )

        requirements_code = format_code('\n'.join(requirements))

        # make project root directory
        root_dir = f'./{project_name}'
        if not os.path.exists(root_dir):
            os.makedirs(root_dir)

        # make project auxiliary directories
        aux_dirs = [project_name, 'app', 'data', 'notebook', 'scripts']
        for dir_ in aux_dirs:
            new_dir = f'{root_dir}/{dir_}'
            if not os.path.exists(new_dir):
                os.makedirs(new_dir)

        # make project main directories
        main_dirs = [project_name, 'bin', 'docs']
        for dir_ in main_dirs:
            new_dir = f'{root_dir}/{project_name}/{dir_}'
            if not os.path.exists(new_dir):
                os.makedirs(new_dir)

        # make utils subpackage directory
        new_dir = f'{root_dir}/{project_name}/{project_name}/utils'
        if not os.path.exists(new_dir):
                os.makedirs(new_dir)

        # initialize '<project_name>' and 'utils' as proper Python packages
        pkg_dirs = {
            project_name: format_code(
            f'''
            from . import utils
            def {project_name}_test(message: str) -> str:
                """Test function for {project_name} module.

                Parameters
                ----------
                message : str
                    The message to be printed and returned.

                Returns
                -------
                str
                    The returned message.
                """
                utils_message = utils.utils_test("utils successfully tested!")
                print(message)
                return utils_message + ' ' + message
            '''
            ),
            f'{project_name}/utils': format_code(
            f'''
            def utils_test(message: str) -> str:
                """Test function for utils module.

                Parameters
                ----------
                message : str
                    The message to be printed and returned.

                Returns
                -------
                str
                    The returned message.
                """
                print(message)
                return message
            '''
            )
            }
        for dir_ in pkg_dirs:
            with open(f'{root_dir}/{project_name}/{dir_}/__init__.py', 'w') as file:
                if dir_ == f'{project_name}/utils':
                    file.write(format_code(f'''from .utils import *'''))
                file.close()
            with open(f"{root_dir}/{project_name}/{dir_}/{dir_.split('/')[-1]}.py", 'w') as file:
                file.write(pkg_dirs.get(dir_))
                file.close()

        # initialize README.md
        with open(f'{root_dir}/{project_name}/README.md', 'w') as file:
            file.write(readme_code)
            file.close()

        # initialize setup.py
        with open(f'{root_dir}/{project_name}/setup.py', 'w') as file:
            file.write(setup_code)
            file.close()

        # initialize requirements.txt
        with open(f'{root_dir}/{project_name}/requirements.txt', 'w') as file:
            file.write(requirements_code)
            file.close()

        # initialize .gitignore
        with open(f'{root_dir}/{project_name}/.gitignore', 'w') as file:
            file.write(git_code)
            file.close()

        # initialize Dockerfile
        with open(f'{root_dir}/{project_name}/Dockerfile', 'w') as file:
            file.write(docker_code)
            file.close()

        # initialize sample notebook
        with open(f'{root_dir}/notebook/{today}_notebook.ipynb', 'w') as file:
            file.write(notebook_code)
            file.close()

        # initialize sample Streamlit app
        with open(f'{root_dir}/app/{project_name}_app.py', 'w') as file:
            file.write(streamlit_code)
            file.close()

        # initialize Sphinx conf.py
        with open(f'{root_dir}/{project_name}/docs/conf.py', 'w') as file:
            file.write(sphinx_conf_code)
            file.close()

        # initialize Sphinx index.rst
        with open(f'{root_dir}/{project_name}/docs/index.rst', 'w') as file:
            file.write(sphinx_index_code)
            file.close()

        # initialize Sphinx make.bat
        with open(f'{root_dir}/{project_name}/docs/make.bat', 'w') as file:
            file.write(sphinx_makebat_code)
            file.close()

        # initialize Sphinx Makefile
        with open(f'{root_dir}/{project_name}/docs/Makefile', 'w') as file:
            file.write(sphinx_makefile_code)
            file.close()

        # initialize Sphinx '<project_name>'.rst
        with open(f'{root_dir}/{project_name}/docs/{project_name}.rst', 'w') as file:
            file.write(sphinx_package_code)
            file.close()



def main():
    parser = argparse.ArgumentParser(description='Initialize a Python project folder.')
    parser.add_argument(
        '-n',
        '--name',
        action="store",
        dest="project_name",
        help="the name of the project (will be used for root dir and package name)",
        default="fire_up"
    )
    parser.add_argument(
        '-a',
        '--author',
        action="store",
        dest="author",
        help="the name of the author",
        default="placeholder"
    )
    parser.add_argument(
        '-m',
        '--mail',
        action="store",
        dest="email",
        help="the email of the author",
        default="placeholder"
    )
    args = parser.parse_args()
    if (args.author != 'placeholder') and (args.email != 'placeholder'):
        FireUp(
            project_name=args.project_name,
            author=args.author,
            email=args.email
        )
    else:
        FireUp(project_name=args.project_name)

if __name__ == '__main__':
    main()