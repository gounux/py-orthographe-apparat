# py-orthographe-apparat

Un CLI python pour convertir du texte en [orthographe d'apparat](https://fr.wikipedia.org/wiki/Orthographe_d%27apparat), _mne alshughta bigt igt ëwëua !_

Ce projet utilise [`pylirecouleur`](https://pypi.org/project/pylirecouleur/) pour découper le texte français en phonèmes.

## Installation

```text
pip install py-orthographe-apparat
```

## Usage en CLI

```text
$ pyoa "salut la troupe"
Orthographe d'apparat de 'salut la troupe' :
wigtleseu lesigt ghtrrheb
```

## Usage en tant que lib

```python
from pyoa import encode_orthographe_d_apparat

encode_orthographe_d_apparat("salut la troupe")
# "wigtleseu lesigt ghtrrheb"
```

## Développement

- Installer `uv` via `python3 -m pip install uv`.

- Cloner le dépôt et synchroniser via `uv sync`.

- Lancer le CLI via `uv run pyoa "salut la troupe"`.
