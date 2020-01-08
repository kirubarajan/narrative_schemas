import math

class Event:
    def __init__(self, subject, verb, dependency):
        self.subject = subject
        self.verb = verb
        self.argument = dependency

    def __str__(self):
        return " ".join([self.subject, self.verb, self.argument])

    def __hash__(self):
        return hash(self.__str__())

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

"""joint coreference probability (section 4)"""
# `events` is a frequency dictionary of type event -> integer 
def joint_event_prob(event1, event2, events):
    count = 0
    for event in events:
        if event1.argument == event2.argument and event1.argument == event.argument:
            count += 1
    return count / sum([events[x] for x in events])

"""coreference probability (section 4)"""
def event_prob(event1, events):
    count = 0
    for event in events:
        if event1.argument == event.argument:
            count += 1
    return count / sum([events[x] for x in events])

"""pointwise mutual information approximation"""
def ppmi_approx(event1, event2):
    numerator = math.log(joint_event_prob(event1, event2, chains))
    denominator = math.log(event_prob(event1, events)) + math.log(event_prob(event2, events))
    return math.log(math.exp(joint_event_prob - math.exp(denominator)))