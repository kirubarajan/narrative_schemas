"""Script for managing the NYT section of the Gigaword Corpus"""
import spacy
import stanfordnlp
from models import Event
from data import build_loader


# data pre-processing
EXAMPLE = "First, President Bush occupied Iraq. Then, Iraq was offered a deal by him" 
loader = build_loader()

# [data loading sanity check]: print(loader.get_text()[:200], loader.get_text()[-200:])

"""Dependency Parsing and Coreference Resolution using Stanford NLP Package"""
def parse_stanford():
    nlp = stanfordnlp.Pipeline(processors='tokenize,mwt,pos,lemma,depparse', lang='en')
    doc = nlp(EXAMPLE)
    events = set()

    for sentence in doc.sentences:
        for word in sentence.words:
            print(word.pos, word.text, "->", word. dependency_relation, sentence.words[word.governor - 1].text if word.governor > 0 else 'root')
            
            if word.pos == "VBD":
                verb, argument = word.text, sentence.words[word.governor - 1].text if word.governor > 0 else 'root'
                event = Event(verb, argument)
                events.add(event)
                print(event)

    print(events)

"""Dependency Parsing and Coreference Resolution using SpaCy Package"""
def parse_spacy():
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(EXAMPLE)

    for token in doc:
        if not token.is_stop and token.dep_ != "punct":
            if token.tag_ == "VBD":
                print("VERB: " + token.text)
            print(token.text, token.dep_, token.tag_)
            
parse_spacy()