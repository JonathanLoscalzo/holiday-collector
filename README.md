# holidaycollector #

Console script that collects and parses *.ics files and transforms them to csv format.

Author: Jonathan Loscalzo <<jonathan.r.loscalzo@gmail.com>>

## Installation ##

It is strongly recommended that you use virtualenv/pipsi/conda.
Activate your environment, and then run:

```
    pip install holidaycollector
```

    or

```
    pip install .
```

<!-- This will install `holidaycollector` in the environment's `bin` folder.

[virtualenv]: http://docs.python-guide.org/en/latest/dev/virtualenvs/
[pipsi]: https://github.com/mitsuhiko/pipsi#pipsi
[conda env]: http://conda.pydata.org/docs/using/envs.html -->

NOTE: installation is not needed.

## Usage ##

See `holidaycollector -h`

Execute as a module: 
- `python -m holidaycollector -h`
- `python -m holidaycollector download-and-transform argentina`
...


## License ##

This software is available under the terms of the MIT license. See [LICENSE][]
for details.

## References

- https://dev.to/codemouse92/dead-simple-python-project-structure-and-imports-38c6
- https://realpython.com/python-application-layouts/
- https://github.com/goerz/cookiecutter-pyscript/tree/master/%7B%7Bcookiecutter.project_name%7D%7D

[LICENSE]: LICENSE
