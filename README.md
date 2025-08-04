# federicos-plots

## Working on the repo

Install pdm - this can be installed globally, since it's a package manager.

```
python -m pdm
```

Within the `federicos-plots` directory, now install the package and its dependencies.
This will create a virtual environment for you within `.venv`

```
pdm install
```

Autobuild the docs!
This uses the `docs` script configured within pyproject.toml
(see the `tool.pdm.scripts` table)

```
pdm run docs
```