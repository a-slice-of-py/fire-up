#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import textwrap
import datetime
import argparse
import click

class FireUp:

    def __init__(
        self,
        target_dir,
        project_name,
        author,
        email
        ):

        format_code = lambda x: textwrap.dedent(x).strip()

        project_name = project_name.replace(' ', '_')
        project_name_str = ''.join(list(map(lambda x: x.capitalize(), f'{project_name}'.split('_'))))
        project_env = f'.venv-{project_name.replace("_","-")}'

        today = str(datetime.datetime.now().date()).replace('-','')

        requirements = [
            'pipreqs',
            'ipykernel',
            'mkdocs',
            'mkdocs-material',
            'mkdocstrings',
            'python-dotenv',
            'loguru',
            'click',
            'pytest',
            'pytest-html',
            'pydantic',
            'hydra-core',
            'boto3'
            ]
        requirements = format_code('\n'.join(requirements))

        streamlit_app = format_code(
            f'''
            #!/usr/bin/env python3
            # -*- coding: utf-8 -*-
            # pylint: disable=E1120

            import streamlit as st
            from hydra_config import serve_config

            config = serve_config()

            def main(config : dict = config) -> None:

                st.sidebar.markdown("# My-project - dashboard")
                st.write("# Hello from My-project!")
                st.write("_built with FireUp!_")
                st.write(config)

            if __name__ == "__main__":
                main()
            '''
            )

        jupyter_notebook = format_code(
            f'''
            {{
            "cells": [
            {{
            "cell_type": "code",
            "metadata": {{
            }},
            "outputs": [],
            "source": [
                "# sample notebook\\n"
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

        readme = format_code(
            f'''
            # {project_name_str}

            {project_name_str} is a Python package initialized with FireUp!

            ## Installation

            Use the package manager [pip](https://pip.pypa.io/en/stable/) to install {project_name} in edit mode.

            ```python
            >>> pip install -e . # in the root folder (look for setup.py)
            ```

            ## Project tree structure

            ```python
            root/
            │
            ├── {project_env}/
            │
            ├── cdk-app/
            │
            ├── dashboard/
            |   |
            │   ├── assets/
            |   |
            │   ├── components/
            |   |
            │   ├── config/
            |   |
            │   ├── app.py
            |   |
            │   ├── hydra_config.py
            |   |
            │   └── utils.py
            │
            ├── data/
            │
            ├── docker/
            |   |
            │   └── dashboard/
            |       |
            │       └── Dockerfile
            |
            ├── docs/
            |   |
            │   ├── css/
            │   |   └── mkdocstrings.css
            |   |
            │   └── index.md
            |
            ├── notebooks/
            │   └── {today}_notebook.ipynb
            │
            ├── tests/
            |
            ├── {project_name}/
            |   |
            |   ├── __init__.py
            │   │
            |   ├── core/
            │   |   └── __init__.py
            │   │
            |   ├── dashboard/
            │   |   ├── __init__.py
            │   │   └── app.py
            │   │
            |   └── utils/
            │       └── __init__.py
            |
            ├── .dockerignore
            ├── .env
            ├── .gitignore
            ├── config.mk
            ├── docker-compoe.yml
            ├── Makefile
            ├── mkdocs.yml
            ├── README.md
            ├── requirements.txt
            └── setup.py
            ```

            ## Usage

            Install [streamlit](https://docs.streamlit.io/) via `pip` and execute the following in the root folder to run Streamlit sample app (by default on port 8501)

            ```python
            >>> cd ./{project_name}/dashboard
            >>> streamlit run app.py
            ```

            ## Authors

            - **{author}**
            '''
            )

        setup = format_code(
            f'''
            """A setuptools based setup module.
            See:
            https://packaging.python.org/guides/distributing-packages-using-setuptools/
            https://github.com/pypa/sampleproject
            """

            # Always prefer setuptools over distutils
            from setuptools import setup, find_packages
            from os import path

            with open('requirements.txt') as f:
                requirements = f.read().splitlines()

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
                # package_dir={{'': '{project_name}'}},  # Optional

                # You can just specify package directories manually here if your project is
                # simple. Or you can use find_packages().
                #
                # Alternatively, if you just want to distribute a single Python file, use
                # the `py_modules` argument instead as follows, which will expect a file
                # called `my_module.py` to exist:
                #
                #   py_modules=["my_module"],
                #
                packages=find_packages(exclude=['data', 'docs', '{project_env}', 'notebooks']),  # Required

                # Specify which Python versions you support. In contrast to the
                # 'Programming Language' classifiers above, 'pip install' will check this
                # and refuse to install the project if the version does not match. If you
                # do not support Python 2, you can simplify this to '>=3.5' or similar, see
                # https://packaging.python.org/guides/distributing-packages-using-setuptools/#python-requires
                python_requires='>=3.6',

                # This field lists other packages that your project depends on to run.
                # Any package you put here will be installed by pip when your project is
                # installed, so they must be valid existing projects.
                #
                # For an analysis of "install_requires" vs pip's requirements files see:
                # https://packaging.python.org/en/latest/requirements.html
                install_requires=requirements,  # Optional
            )
            '''
            )

        gitignore = format_code(
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
            autoapi

            # mkdocs docs
            site/

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
            {project_env}

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

            # data
            /data/

            # End of https://www.gitignore.io/api/osx,linux,python,windows,pycharm,visualstudiocode
            '''
            )

        dockerfile = format_code(
            f'''
            # Copyright (c).
            # Confidential and intended for internal use only.

            # base image
            ARG BASE_CONTAINER=python:3.7
            FROM $BASE_CONTAINER

            # ENV AWS_PROFILE=ambiente-dev

            LABEL maintainer="{author} <{email}>"

            # Copy project files
            # COPY ./ /./
            COPY . /

            # streamlit-specific commands
            RUN mkdir -p /root/.streamlit
            RUN bash -c 'echo -e "\\
            [general]\\n\\
            email = \\"\\"\\n\\
            " > /root/.streamlit/credentials.toml'
            RUN bash -c 'echo -e "\\
            [server]\\n\\
            enableCORS = false\\n\\
            " > /root/.streamlit/config.toml'

            # exposing default port for streamlit
            EXPOSE 8501

            # copy over and install packages
            # RUN pip install -r ./requirements.txt
            RUN pip install -e .

            # run app
            CMD streamlit run ./{project_name}/dashboard/app.py # -- --profile $AWS_PROFILE --server.headless false
            '''
            )

        docker_compose = format_code(
            f'''
            version: '3'

            services:
              dashboard:
                build:
                  context: .
                  dockerfile: ./docker/dashboard/Dockerfile
                image:
                ports:
                 - "80:8501"
                volumes:
                 - C:/Users/a00018578/.aws:/root/.aws
                 - ./dashboard:/src
            '''
            )

        dockerignore = format_code(
            f'''
            **/.git
            **/.vscode
            **/__pycache__
            **/docs
            **/{project_name}.egg-info
            **/{project_env}
            **/notebooks
            '''
            )

        makefile = format_code(
            f'''
            include config.mk

            ## __LAUNCH_FROM_BASE_ENV__ create-env: initialize python virtual enviroment
            .PHONY: create-env
            create-env:
            	virtualenv $(ENV_NAME)

            ## activate-env: activate python virtual enviroment
            .PHONY: activate-env
            activate-env:
            	@echo "Command stored! You can past and run it in the CLI."
            	@echo "$(ENV_NAME)\\Scripts\\activate.bat" | clip

            ## init: initialize package basic dependencies
            .PHONY: init
            init:
            	$(PYTHON) -m pip install -r ./requirements.txt

            ## register-env: register virtual enviroment in jupyter suite
            .PHONY: register-env
            register-env:
            	$(PYTHON) -m ipykernel install --user --name=$(ENV_NAME)

            ## reqs: save requirements.txt with pipreqs
            .PHONY: reqs
            reqs:
            	pipreqs ./ --encoding latin --ignore $(ENV_NAME)

            ## install-package: install python package in edit mode
            .PHONY: install-package
            install-package:
            	$(PYTHON) -m pip install -e .

            ## streamlit-run: run streamlit app
            .PHONY: streamlit-run
            streamlit-run:
            	cd {project_name}/dashboard && streamlit run app.py

            ## docs-serve: serve package docs on localhost
            .PHONY: docs-serve
            docs-serve:
            	mkdocs serve

            ## docs-build: build package docs as static html website
            .PHONY: docs-build
            docs-build:
            	mkdocs build --no-directory-urls

            ## test: execute tests with pytest and dump html report
            .PHONY: test
            test:
            	cd tests && $(PYTHON) test_loguru.py && pytest --html=pytest-report.html

            .PHONY: help
            help: Makefile
            	@sed -n 's/^## //p' $<
            '''
            )

        make_config = format_code(
            f'''
            ENV_NAME = {project_env}
            PYTHON = $(ENV_NAME)/Scripts/python.exe
            '''
            )

        mkdocs_config = format_code(
            f'''
            site_name: {project_name_str}
            site_url: http://localhost/

            nav:
              - Home: index.md

            theme:
              name: "material"
              palette:
                scheme: slate
                primary: orange
                accent: amber
              features:
                - tabs

            markdown_extensions:
                - toc:
                    permalink: True

            plugins:
              - search
              - mkdocstrings

            extra_css:
              - css/mkdocstrings.css
            '''
            )

        mkdocs_css = format_code(
            '''
            div.doc-contents:not(.first) {
            padding-left: 25px;
            border-left: 4px solid rgba(150, 150, 150);
            margin-bottom: 80px;
            }

            h5.doc-heading {
            text-transform: none !important;
            }

            h6.hidden-toc {
            margin: 0 !important;
            position: relative;
            top: -70px;
            }

            h6.hidden-toc::before {
            margin-top: 0 !important;
            padding-top: 0 !important;
            }

            h6.hidden-toc a.headerlink {
            display: none;
            }

            td code {
            word-break: normal !important;
            }

            td p {
            margin-top: 0 !important;
            margin-bottom: 0 !important;
            }
            '''
            )

        dotenv = format_code(
            f'''
            LOGURU_LEVEL='DEBUG'
            '''
            )

        package_init = format_code(
            f'''
            from dotenv import load_dotenv
            load_dotenv()
            '''
            )

        hydra_config = format_code(
            f'''
            import hydra.experimental as he
            from hydra.core.global_hydra import GlobalHydra
            from omegaconf import OmegaConf

            def serve_config() -> dict:
                GlobalHydra.instance().clear()
                he.initialize(config_path="config")
                return OmegaConf.to_container(he.compose("config"))
            '''
            )

        test_pytest = format_code(
            f'''
            # pytest (create make command to execute test with pytest --html=pytest_report.html)
            class TestClass:
                def test_passed(self):
                    x = "cane"
                    assert "c" in x

                def test_failed(self):
                    x = "gatto"
                    assert hasattr(x, "check")
            '''
            )

        test_loguru = format_code(
            f'''
            from dotenv import load_dotenv
            load_dotenv()
            from loguru import logger

            logger.debug("this is a debugging message")
            logger.info("this is an informational message")
            logger.warning("this is a warning message")
            logger.error("this is an error message")
            logger.critical("this is a critical message")

            print('')

            @logger.catch
            def divide_by(x):
                return 1 / x

            if __name__ == '__main__':
                divide_by(0)
            '''
            )

        # make project root directory
        root_dir = f'{target_dir}/.fire-up-{project_name.replace("_","-")}'
        if not os.path.exists(root_dir):
            os.makedirs(root_dir)

        # make project auxiliary directories
        aux_dirs = [project_name, 'docs', 'data', 'notebooks', 'tests', 'dashboard', 'docker', 'cdk-app']
        for dir_ in aux_dirs:
            new_dir = f'{root_dir}/{dir_}'
            if not os.path.exists(new_dir):
                os.makedirs(new_dir)
            if dir_ == 'docs':
                os.makedirs(f'{new_dir}/css')
                # make `project_name` dir a proper Python package
                with open(f'{new_dir}/css/mkdocstrings.css', 'w') as file:
                    file.write(mkdocs_css)
                    file.close()
            elif dir_ == 'docker':
                os.makedirs(f'{new_dir}/dashboard')
                # initialize Dockerfile
                with open(f'{new_dir}/dashboard/Dockerfile', 'w') as file:
                    file.write(dockerfile)
                    file.close()
            elif dir_ == 'dashboard':
                # initialize sample Streamlit app
                with open(f'{new_dir}/app.py', 'w') as file:
                    file.write(streamlit_app)
                    file.close()
                with open(f'{new_dir}/utils.py', 'w') as file:
                    file.close()

                for dashboard_aux_dir in ['assets', 'components']:
                    dashboard_subdir = f'{new_dir}/{dashboard_aux_dir}'
                    if not os.path.exists(dashboard_subdir):
                        os.makedirs(dashboard_subdir)
                # initialize hydra config
                with open(f'{new_dir}/hydra_config.py', 'w') as file:
                    file.write(hydra_config)
                    file.close()
                config_dir = f'{new_dir}/config'
                os.makedirs(f'{config_dir}/animal')
                with open(f'{config_dir}/config.yaml', 'w') as file:
                    file.write(
                        format_code(
                            f'''
                            defaults:
                              - animal: cane
                            '''
                            )
                        )
                    file.close()
                with open(f'{config_dir}/animal/cane.yaml', 'w') as file:
                    file.write(
                        format_code(
                            f'''
                            # @package _group_
                            nome: fido
                            verso: bau
                            '''
                            )
                        )
                    file.close()
                with open(f'{config_dir}/animal/gatto.yaml', 'w') as file:
                    file.write(
                        format_code(
                            f'''
                            # @package _group_
                            nome: micio
                            verso: miao
                            '''
                            )
                        )
                    file.close()
            elif dir_ == 'tests':
                with open(f'{new_dir}/test_pytest.py', 'w') as file:
                    file.write(test_pytest)
                    file.close()
                with open(f'{new_dir}/test_loguru.py', 'w') as file:
                    file.write(test_loguru)
                    file.close()

        # make `project_name` dir a proper Python package
        with open(f'{root_dir}/{project_name}/__init__.py', 'w') as file:
            file.write(package_init)
            file.close()

        # make project main directories
        main_dirs = ['core', 'utils']
        for dir_ in main_dirs:
            new_dir = f'{root_dir}/{project_name}/{dir_}'
            if not os.path.exists(new_dir):
                os.makedirs(new_dir)
            with open(f'{new_dir}/__init__.py', 'w') as file:
                file.close()

        # initialize README.md
        with open(f'{root_dir}/README.md', 'w', encoding="utf-8") as file:
            file.write(readme)
            file.close()

        # initialize .env
        with open(f'{root_dir}/.env', 'w', encoding="utf-8") as file:
            file.write(dotenv)
            file.close()

        # initialize setup.py
        with open(f'{root_dir}/setup.py', 'w') as file:
            file.write(setup)
            file.close()

        # initialize requirements.txt
        with open(f'{root_dir}/requirements.txt', 'w') as file:
            file.write(requirements)
            file.close()

        # initialize .gitignore
        with open(f'{root_dir}/.gitignore', 'w') as file:
            file.write(gitignore)
            file.close()

        # initialize Dockerfile
        with open(f'{root_dir}/docker-compose.yml', 'w') as file:
            file.write(docker_compose)
            file.close()

        # initialize .dockerignore
        with open(f'{root_dir}/.dockerignore', 'w') as file:
            file.write(dockerignore)
            file.close()

        # initialize mkdocs.yml
        with open(f'{root_dir}/mkdocs.yml', 'w') as file:
            file.write(mkdocs_config)
            file.close()

        # initialize project Makefile
        with open(f'{root_dir}/Makefile', 'w') as file:
            file.write(makefile)
            file.close()

        # initialize project make config
        with open(f'{root_dir}/config.mk', 'w') as file:
            file.write(make_config)
            file.close()

        # initialize sample notebook
        with open(f'{root_dir}/notebooks/{today}_notebook.ipynb', 'w') as file:
            file.write(jupyter_notebook)
            file.close()

        # initialize docs index
        with open(f'{root_dir}/docs/index.md', 'w') as file:
            file.write(f'# Welcome to {project_name_str} documentation\n')
            file.close()

@click.command()
@click.option(
    '--name',
    default='my-project',
    prompt='Project name',
    help='Name for the initialized Python project (will be used for folders and other stuff).'
    )
@click.option(
    '--directory',
    default='.',
    prompt='Target directory',
    help='Directory in which the project must be initialized.'
    )
@click.option(
    '--author',
    default='myself',
    prompt='Author name',
    help="Project's author name."
    )
@click.option(
    '--email',
    default='myself@placeholder.com',
    prompt='Author email',
    help="Project's author email."
    )
def main(name, directory, author, email):
    FireUp(
        target_dir=directory,
        project_name=name,
        author=author,
        email=email
    )

if __name__ == '__main__':
    main()
