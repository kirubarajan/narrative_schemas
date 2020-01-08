# Unsupervised Learning of Narrative Event Chains
> Nathanael Chambers and Dan Jurafsky (2008)
Updated implementation as part of an independent study at the University of Pennsylvania.

## Algorithm
An implementation of (Chambers and Jurafsky, 2008), using updated libaries, classes and functions. Written in Python, using the Stanford CoreNLP library (updated dependency parsing from transition model to neural-based Universal Dependencies). 

The following libraries are used throughout the study:
1. Stanford CoreNLP Python Implementation
2. SpaCy Dependency Parser and Coreference Resolution 

Future work and extensions include:
1. Word2Vec Google-News Word Embedding Model 
2. PyMagnitude Embedding Format

Event chain definition is available in `code/models.py` as well as implementations of Point-Wise Mutual Information approximation of event chains. The `Event` type supports various native Python functionality such as `hash`, `str` and `eq`. Events can be instantiated in Python as following:

```python
from models import Event

event = Event("Arun", "finished", "project")
print(event == Event("Arun", "finish", "project")) # -> true
```

The parsing module implementation is available at `code/parsing.py`, which 1) parses linguistic features (e.g. parts-of-speech, noun phrase chunks) and 2) parses plaintext into a frequency dictionary of `Events`. Point-wise Mutual Information can be computed as follows:

```python
from models import ppmi_approx

print(ppmi_approx(event1, event2, events)) # where `events` is is a frequency dictionary of events
```

## Data
The algorithm is being tested on a subset of the New York Times section of the Gigaword Corpus using the `agiga` maven package. The data is loaded using a custom `DataLoader` class, which supports cleaning output from the `agiga` package as well as other quality-of-life Python functions (e.g. `sanity_check()`, `len()`).

A Data Loader can be instantiated using the `build_loader()` helper as follows:

```python
from data import build_loader

file_path = "data/agiga/export.txt"
loader = build_loader(file_path)
loader.sanity_check()
```

## Evaluation
Evaluation is performed using the *Narrative Cloze* Evaluation Task. Implementation can be found in `code/evaluation.py`.
