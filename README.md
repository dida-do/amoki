# AMoKI

Repository for the AMoKI remote-sensing project.

## Installation
To set up the project on your local machine, follow these steps:

1. **Clone the Repository (assuming you are using ssh)**
   
    ```bash
    git clone git@git.dida.do:dida/amoki.git
    cd amoki
    ```

2. **Install Poetry**

Poetry is used for dependency management. If you don't have Poetry installed, you can install it by following the instructions [here](https://python-poetry.org/docs/).

3. **Install dependencies**
    ```bash
    poetry install
    ```

4. **Activate the virtual environment**
    ```bash
    poetry shell
    ```

You are now ready to start working with the project. For any issues, refer to the docs directory or contact the project maintainers.

## Modifying dependencies
To add dependency X, use

```bash
poetry add X
``` 
or manually add it to the pyproject.toml file. 
To remove a dependency, use:
```bash
poetry remove X
``` 
If you wish to reinstall all the dependencies of the project, use:
```bash
poetry install
``` 

### Repository structure

```
├── amoki                   <- Source code for use in this project.
│   │
│   ├── __init__.py         <- Makes amoki into a Python module
|   ├── utilities
|   |   └── sentinelhub_utils.py
│   └── config.py           <- Configuration file for the project
│   
├── data
│   ├── external            <- Data from third party sources.
│   ├── interim             <- Intermediate data that has been transformed.
│   ├── processed           <- The final, canonical data sets for modelling.
│   └── raw                 <- The original, immutable data dump.
│
├── notebooks               <- Jupyter notebooks
│                               
├── references              <- Data dictionaries, manuals, and all other explanatory materials.
│
├── .gitignore
├── LICENSE                 <- Open-source license if one is chosen
├── poetry.lock             <- Locked package versions
├── pyproject.toml          <- Project configuration file with package metadata for amoki
│                               dependencies, and configuration for tools like black
└── README.md               <- The top-level README for developers using this project.
```

--------

## Accessing SentinelHub
To access Sentinel Hub services, you require an account. More details can be found at SentinelHub.