# Unsupervised Learning of Narrative Event Chains
> Nathanael Chambers and Dan Jurafsky (2008)
Updated implementation as part of an independent study at the University of Pennsylvania.

## Algorithm
An implementation of (Chambers and Jurafsky, 2008), using updated libaries, classes and functions. Written in Python, using the Stanford CoreNLP library (updated dependency parsing from transition model to neural-based Universal Dependencies). Event chain definition is available in `code/models.py` as well as implementations of Point-Wise Mutual Information approximation of event chains.

The following libraries are used throughout the study:
1. Stanford CoreNLP Python Implementation
2. SpaCy Dependency Parser and Coreference Resolution 

Future work and extensions include:
1. Word2Vec Google-News Word Embedding Model 
2. PyMagnitude Embedding Format

## Data
The algorithm is being tested on a subset of the New York Times section of the Gigaword Corpus using the `agiga` maven package.

## Evaluation
Evaluation is performed using the *Narrative Cloze* Evaluation Task. Implementation can be found in `code/evaluation.py`.
