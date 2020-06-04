# bee

bee is a simple project-name generator, using a list of keywords to specify topics, and then coming up with random combinations of words that are related to those topics.

## Requirements

* Python >=v3.6
* [NLTK 3.5](https://www.nltk.org/)

## Installation

`pip` installation can be added; if you're interested in using this project, just ask and I'll roll out a PyPI package. Otherwise `git clone` and use `bee.py` wherever you like. It does not depend on any other files in this repo.

## Usage

Sample keywords file `kw.txt`:

```
python
name
generator
```

Pass `kw.txt` to `bee.py`, asking for 6 different project names:

```bash
./bee.py kw.txt 6

carpet_snakegenerator
place_nameMagneto
anonymDynamo
ApparatusPython
magneto-marque
false_namerock_snake
```

Note that the results will be more varied if more keywords are supplied.

## Help

```
usage: bee.py [-h] file N

Generate random project names based on keywords

positional arguments:
  file        input file containing list of keywords
  N           number of project names to generate

optional arguments:
  -h, --help  show this help message and exit
```
