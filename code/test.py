"""Script for managing the NYT section of the Gigaword Corpus"""
"""Functions of interest: get_events, parse_syntax"""

from models import Event
from data import build_loader
from parse import get_events

"""Data Pre-Processing"""
# loader = build_loader()
# loader.sanity_check()
EXAMPLE = "First, President Bush occupied Iraq. Then, Iraq was offered a deal by him" 

events = get_events(EXAMPLE)
print(len(events))