# Unsupervised Learning of Narrative Event Chains
> Nathanael Chambers and Dan Jurafsky (2008)
Updated implementation as part of an independent study at the University of Pennsylvania.

## Algorithm
An implementation of (Chambers and Jurafsky, 2008), using updated libaries, classes and functions. Written in Python, using the Stanford CoreNLP library (updated dependency parsing from transition model to neural-based Universal Dependencies). Event chain definition is available in `code/models.py` as well as implementations of Point-Wise Mutual Information approximation of event chains.

## Data
The algorithm is being tested on a subset of the New York Times section of the Gigaword Corpus using the `agiga` maven package.

## Evaluation
Evaluation is performed using the *narrative cloze* Evaluation Task. Implementation can be found in `code/evaluation.py`.
