class Event:
    def __init__(self, verb, argument, subject=""):
        self.subject = subject
        self.verb = verb
        self.argument = argument

    def __str__(self):
        return " ".join([self.subject, self.verb, self.argument])