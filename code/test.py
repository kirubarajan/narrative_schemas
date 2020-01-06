"""Script for managing the NYT section of the Gigaword Corpus"""

import stanfordnlp
from models import Event

nlp = stanfordnlp.Pipeline(processors='tokenize,mwt,pos,lemma,depparse', lang='en')
doc = nlp("First, President Bush occupied Iraq. Then, he offered Iraq a deal.")
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