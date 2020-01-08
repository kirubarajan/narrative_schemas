"""Script for managing the NYT section of the Gigaword Corpus"""
"""Functions of interest: get_events, parse_syntax"""

from models import Event
from data import build_loader
from parse import get_events

"""Data Pre-Processing"""
file_path = "data/agiga/export.txt"
loader = build_loader(file_path)
# loader.sanity_check()
EXAMPLE = "First, President Bush occupied Iraq. Then, Iraq was offered a deal by him" 

events = get_events(EXAMPLE)
for event in events:
    print(event, events[event])