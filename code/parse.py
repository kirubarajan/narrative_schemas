from collections import defaultdict
import stanfordnlp
import spacy
from spacy.symbols import nsubj, nsubjpass, VERB
from models import Event

"""Dependency Parsing and Coreference Resolution using Stanford NLP Package"""
def parse_stanford():
    nlp = stanfordnlp.Pipeline(processors='tokenize,mwt,pos,lemma,depparse', lang='en')
    doc = nlp(EXAMPLE)

    for sentence in doc.sentences:
        for word in sentence.words:
            print(word.pos, word.text, "->", word. dependency_relation, sentence.words[word.governor - 1].text if word.governor > 0 else 'root')
            
            if word.pos == "VBD":
                verb, argument = word.text, sentence.words[word.governor - 1].text if word.governor > 0 else 'root'
                event = Event(verb, argument)
                events.add(event)
                print(event)

    print(events)

"""Parsing POS and Chunking using SpaCy"""
def parse_syntax():
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(EXAMPLE)

    for token in doc:
        if not token.is_stop and token.dep_ != "punct":
            if token.tag_ == "VBD":
                print("VERB: " + token.text)
            print(token.text, token.dep_, token.tag_)

    for chunk in doc.noun_chunks:
        print(chunk.text, chunk.root.text, chunk.root.dep_, chunk.root.head.text)

        if chunk.root.head.pos_ == "VERB":
            print(chunk.text, chunk.root.head.text, chunk.root.pos_)
            print("HEAD VERB", chunk.root.head.text, chunk.root.head.pos_)

"""Dependency Parsing and Coreference Resolution using SpaCy Package"""
"""Returns a frequency dictionary of type Event -> integer"""
def get_events(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    events = defaultdict(int)

    # Finding a verb with a subject from below
    for possible_subject in doc:
        if possible_subject.dep in {nsubj, nsubjpass} and possible_subject.head.pos == VERB:
            for dependent in possible_subject.head.children:
                if dependent.dep_ == "dobj":
                    event = Event(possible_subject.text, possible_subject.head.text, dependent.text)
                    events[event] += 1
    return events